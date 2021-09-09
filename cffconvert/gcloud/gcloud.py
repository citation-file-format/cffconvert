import os
from flask import Response
from cffconvert import Citation
from cffconvert import version as cffconvert_version


def get_help_text():
    p = os.path.join(os.path.dirname(__file__), "index.html")
    with open(p, 'rt') as fid:
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

    cffstr = None
    outputformat = None
    url = None
    validate = False
    version = False

    outstr = ''

    if request.args:

        if 'cffstr' in request.args:
            cffstr = request.args.get('cffstr')
        if 'outputformat' in request.args:
            outputformat = request.args.get('outputformat')
        if 'url' in request.args:
            url = request.args.get('url')
        if 'validate' in request.args:
            validate = True
        if 'version' in request.args:
            version = True
    else:
        return Response(get_help_text(), mimetype='text/html')

    if version is True:
        outstr += "{0}\n".format(cffconvert_version.__version__)
        return Response(outstr, mimetype='text/plain')

    if url is not None and cffstr is not None:
        outstr += "\n\n{0}\n".format("Error: can't have both url and cffstr.")
        return Response(outstr, mimetype='text/plain')

    try:
        citation = Citation(cffstr=cffstr, src=url)
    except Exception as e:
        if str(e) == "Provided CITATION.cff does not seem valid YAML.":
            outstr += "\n\nError: Provided 'cffstr' does not seem valid YAML."
        else:
            outstr += "\n\nError: " + str(e)
        return Response(outstr, mimetype='text/plain')

    acceptable_output_formats = ["bibtex", "cff", "codemeta", "endnote", "schema.org", "ris", "zenodo"]
    if validate:
        # when validating, there's no need to convert to anything yet
        pass
    elif outputformat not in acceptable_output_formats:
        outstr += "\n\n'outputformat' should be one of [{0}]".format(", ".join(acceptable_output_formats))
        return Response(outstr, mimetype='text/plain')

    if outputformat is None:
        return Response(outstr, mimetype='text/plain')

    outstr += {
        "apalike": citation.as_apalike,
        "bibtex": citation.as_bibtex,
        "cff": citation.as_cff,
        "codemeta": citation.as_codemeta,
        "endnote": citation.as_endnote,
        "ris": citation.as_ris,
        "schema.org": citation.as_schemaorg,
        "zenodo": citation.as_zenodo
    }[outputformat]()

    return Response(outstr, mimetype='text/plain')
