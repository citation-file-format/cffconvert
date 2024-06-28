# pylint: disable=too-many-return-statements
import os
from flask import Response
from jsonschema.exceptions import ValidationError as JsonschemaSchemaError
from pykwalify.errors import SchemaError as PykwalifySchemaError
from cffconvert import Citation
from cffconvert.cli import version as cffconvert_version
from cffconvert.cli.read_from_url import read_from_url


def get_help_text():
    p = os.path.join(os.path.dirname(__file__), "index.html")
    with open(p, "rt", encoding="utf-8") as fid:
        return fid.read()


def cffconvert(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """

    mimetype_plain = "text/plain"
    mimetype_html = "text/html"

    outstr = ""

    if not request.args or "help" in request.args.keys():
        return Response(get_help_text(), mimetype=mimetype_html)

    cffstr = request.args.get("cffstr", None)
    outputformat = request.args.get("outputformat", None)
    url = request.args.get("url", None)
    validate = "validate" in request.args.keys()
    version = "version" in request.args.keys()

    if version is True:
        outstr += f"{cffconvert_version.__version__}\n"
        return Response(outstr, mimetype=mimetype_plain)

    condition = (url is None, cffstr is None)
    if condition == (False, False):
        outstr += "\n\nError: can't have both url and cffstr.\n"
        return Response(outstr, mimetype=mimetype_plain)
    if condition == (True, True):
        outstr += "\n\nError: you must specify either url or cffstr.\n"
        return Response(outstr, mimetype=mimetype_plain)
    if condition == (False, True):
        cffstr = read_from_url(url)

    citation = Citation(cffstr=cffstr)
    try:
        citation.validate()
    except (PykwalifySchemaError, JsonschemaSchemaError):
        outstr += "Data does not pass validation according to Citation "
        outstr += f"File Format schema version {citation.cffversion}."
        return Response(outstr, mimetype=mimetype_plain)

    if validate:
        outstr += f"Data passes validation according to Citation File Format schema version {citation.cffversion}."
        return Response(outstr, mimetype=mimetype_plain)

    acceptable_output_formats = ["apalike", "biblatex", "bibtex", "cff", "codemeta", "endnote", "schema.org", "ris", "zenodo"]
    if outputformat not in acceptable_output_formats:
        outstr += f"\n\n'outputformat' should be one of [{', '.join(acceptable_output_formats)}]"
        return Response(outstr, mimetype=mimetype_plain)

    outstr += {
        "apalike": citation.as_apalike,
        "biblatex": citation.as_biblatex,
        "bibtex": citation.as_bibtex,
        "cff": citation.as_cff,
        "codemeta": citation.as_codemeta,
        "endnote": citation.as_endnote,
        "ris": citation.as_ris,
        "schema.org": citation.as_schemaorg,
        "zenodo": citation.as_zenodo
    }[outputformat]()

    return Response(outstr, mimetype=mimetype_plain)
