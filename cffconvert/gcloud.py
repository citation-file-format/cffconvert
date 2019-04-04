from flask import request, Response
from cffconvert import Citation
from cffconvert import version as cffconvert_version


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
    ignore_suspect_keys = False
    verbose = False
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
        if 'ignore_suspect_keys' in request.args:
            ignore_suspect_keys = True
        if 'verbose' in request.args:
            verbose = True
        if 'version' in request.args:
            version = True
    else:
        outstr += "You should supply a few arguments. Try adding '?verbose' to the URL to see which arguments exist."
        return Response(outstr, mimetype='text/plain')

    if version is True:
        outstr += "{0}\n".format(cffconvert_version.__version__)
        return Response(outstr, mimetype='text/plain')

    if verbose is True:
        outstr += "{0} = {1}\n".format("cffstr", cffstr)
        outstr += "{0} = {1}\n".format("outputformat", outputformat)
        outstr += "{0} = {1}\n".format("url", url)
        outstr += "{0} = {1}\n".format("validate", validate)
        outstr += "{0} = {1}\n".format("ignore_suspect_keys", ignore_suspect_keys)
        outstr += "{0} = {1}\n".format("verbose", verbose)
        outstr += "{0} = {1}\n".format("version", version)

    if url is not None and cffstr is not None:
        outstr += "\n\n{0}\n".format("Error: can't have both url and cffstr.")
        return Response(outstr, mimetype='text/plain')

    remove = None
    override = None
    suspect_keys = None

    try:
        citation = Citation(url=url, cffstr=cffstr, ignore_suspect_keys=ignore_suspect_keys, override=override,
                            remove=remove, suspect_keys=suspect_keys, validate=validate)
    except Exception as e:
        if str(e) == "Provided CITATION.cff does not seem valid YAML.":
            outstr += "\n\nError: Provided 'cffstr' does not seem valid YAML."
        else:
            outstr += "\n\nError: " + str(e)
        return Response(outstr, mimetype='text/plain')

    acceptable_output_formats = ["bibtex", "cff", "codemeta", "endnote", "ris", "zenodo"]
    if validate:
        pass
    elif outputformat not in acceptable_output_formats:
        outstr += "\n\n'outputformat' should be one of [{0}]".format(", ".join(acceptable_output_formats))
        return Response(outstr, mimetype='text/plain')

    if outputformat is None:
        return
    elif outputformat == "bibtex":
        outstr += citation.as_bibtex()
    elif outputformat == "codemeta":
        outstr += citation.as_codemeta()
    elif outputformat == "endnote":
        outstr += citation.as_enw()
    elif outputformat == "ris":
        outstr += citation.as_ris()
    elif outputformat == "zenodo":
        outstr += citation.as_zenodojson()
    elif outputformat == "cff":
        outstr += citation.cffstr

    return Response(outstr, mimetype='text/plain')
