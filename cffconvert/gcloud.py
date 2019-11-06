from flask import request, Response
from cffconvert import Citation
from cffconvert import version as cffconvert_version


def get_help_text():
    return """<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css?family=Roboto:300&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Ubuntu+Mono&display=swap" rel="stylesheet">
    <style>
    body {
       font-family: 'Roboto', sans-serif;
       line-height: 1.6em;
       width: 60em;
       background-color: #2f4f4f;
       color: #f0ffff;
       font-size: large;
    }

    body a {
       color: #7fffd4;
       text-decoration: none;
    }

    body a:hover {
       color: #7fffd4;
       text-decoration: underline;
    }

    body a:visited {
       color: #3fd6cf;
       text-decoration: none;
    }

    .code {
       font-family: 'Ubuntu Mono', monospace;
    }
    </style>
    <title>cffconvert</title>
    </head>
<body>


<h1>cffconvert</h1>
This page is an online equivalent of the command line tool <span
style="font-family:monospace"><a
href="https://pypi.org/project/cffconvert/">cffconvert</a></span>.

With this page, you can read a CFF formatted CITATION file from a supplied
string or a GitHub url, and convert it to BibTeX, EndNote, Codemeta, RIS, schema.org,
plain JSON, Zenodo JSON. The way to do that is by supplying various
combinations of arguments as query parameters in the URL (see examples 
below).

<h2>Authorized arguments</h2>

Try adding <a href="?verbose"><span
style="font-family:monospace">?verbose</span></a> to the URL to see which
arguments exist.

<h2>Converting from a GitHub URL</h2>

For the examples below, we use the repository
<a href="https://github.com/citation-file-format/cff-converter-python">
https://github.com/citation-file-format/cff-converter-python</a> as the source
from which to read the CITATION data. By using the
<span style="font-family:monospace">outputformat</span> parameter,  we can
convert to various other formats, as follows.

<ul>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=codemeta"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=codemeta</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=endnote"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=endnote</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=schema.org"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=schema.org</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=ris"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=ris</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=zenodo"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=zenodo</span></a></li>
</ul>

Or if you just want to check the CITATION.cff for a certain repository,
simply set the <span style="font-family:monospace">outputformat</span>
parameter to <span style="font-family:monospace">cff</span>:
<ul>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=cff"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=cff</span></a></li>
</ul>


The following GitHub URL formats are supported:
<ul>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=cff"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=cff</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python/commit/03fd5c1bdbf3cd81e29c8f117526661d61076f28&outputformat=cff"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python/commit/03fd5c1bdbf3cd81e29c8f117526661d61076f28&outputformat=cff</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python/tree/master&outputformat=cff"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python/tree/master&outputformat=cff</span></a></li>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python/tree/1.2.1&outputformat=cff"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python/tree/1.2.1&outputformat=cff</span></a></li>
</ul>

<h2>Converting from a supplied string</h2>
Instead of a GitHub URL, it's also possible to use a string as the data
source. For this, you need to make sure that the CFF data (which is in YAML
format) has been encoded as a URL string, for example using an online
service like <a
href="https://onlineyamltools.com/url-encode-yaml">https://onlineyamltools.com/url-encode-yaml</a>.

The way this works is very similar to using <span
style="font-family:monospace">outputformat</span>, except now the data is
part of the URL, like so:
<ul>
<li><a href="?cffstr=%23%20YAML%201.2%0A---%0Aauthors%3A%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Netherlands%20eScience%20Center%22%0A%20%20%20%20family-names%3A%20Spaaks%0A%20%20%20%20given-names%3A%20Jurriaan%20H.%0A%20%20%20%20orcid%3A%20https%3A%2F%2Forcid.org%2F0000-0002-7064-4069%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Netherlands%20eScience%20Center%22%0A%20%20%20%20family-names%3A%20Klaver%0A%20%20%20%20given-names%3A%20Tom%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Netherlands%20eScience%20Center%22%0A%20%20%20%20family-names%3A%20Verhoeven%0A%20%20%20%20given-names%3A%20Stefan%0A%20%20%20%20orcid%3A%20https%3A%2F%2Forcid.org%2F0000-0002-5821-2060%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Humboldt-Universit%C3%A4t%20zu%20Berlin%22%0A%20%20%20%20family-names%3A%20Druskat%0A%20%20%20%20given-names%3A%20Stephan%0A%20%20%20%20orcid%3A%20https%3A%2F%2Forcid.org%2F0000-0003-4925-7248%0Acff-version%3A%20%221.0.3%22%0Adate-released%3A%202019-07-16%0Adoi%3A%2010.5281%2Fzenodo.1162057%0Akeywords%3A%0A%20%20-%20%22citation%22%0A%20%20-%20%22bibliography%22%0A%20%20-%20%22cff%22%0A%20%20-%20%22CITATION.cff%22%0Alicense%3A%20Apache-2.0%0Amessage%3A%20%22If%20you%20use%20this%20software%2C%20please%20cite%20it%20using%20these%20metadata.%22%0Arepository-code%3A%20%22https%3A%2F%2Fgithub.com%2Fcitation-file-format%2Fcff-converter-python%22%0Atitle%3A%20cffconvert%0Aversion%3A%20%221.2.1%22%0A&outputformat=zenodo"><span style="font-family:monospace">?cffstr=%23%20YAML%201.2%0A---%0Aauthors%3A%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Netherlands%20eScience%20Center%22%0A%20%20%20%20family-names%3A%20Spaaks%0A%20%20%20%20given-names%3A%20Jurriaan%20H.%0A%20%20%20%20orcid%3A%20https%3A%2F%2Forcid.org%2F0000-0002-7064-4069%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Netherlands%20eScience%20Center%22%0A%20%20%20%20family-names%3A%20Klaver%0A%20%20%20%20given-names%3A%20Tom%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Netherlands%20eScience%20Center%22%0A%20%20%20%20family-names%3A%20Verhoeven%0A%20%20%20%20given-names%3A%20Stefan%0A%20%20%20%20orcid%3A%20https%3A%2F%2Forcid.org%2F0000-0002-5821-2060%0A%20%20-%0A%20%20%20%20affiliation%3A%20%22Humboldt-Universit%C3%A4t%20zu%20Berlin%22%0A%20%20%20%20family-names%3A%20Druskat%0A%20%20%20%20given-names%3A%20Stephan%0A%20%20%20%20orcid%3A%20https%3A%2F%2Forcid.org%2F0000-0003-4925-7248%0Acff-version%3A%20%221.0.3%22%0Adate-released%3A%202019-07-16%0Adoi%3A%2010.5281%2Fzenodo.1162057%0Akeywords%3A%0A%20%20-%20%22citation%22%0A%20%20-%20%22bibliography%22%0A%20%20-%20%22cff%22%0A%20%20-%20%22CITATION.cff%22%0Alicense%3A%20Apache-2.0%0Amessage%3A%20%22If%20you%20use%20this%20software%2C%20please%20cite%20it%20using%20these%20metadata.%22%0Arepository-code%3A%20%22https%3A%2F%2Fgithub.com%2Fcitation-file-format%2Fcff-converter-python%22%0Atitle%3A%20cffconvert%0Aversion%3A%20%221.2.1%22%0A&outputformat=zenodo</span></a></li>
</li>
</ul>

Oftentimes, the version information found in a CITATION.cff file is out of date.
When converting it can be convenient to ignore some suspect keys like <span
style="font-family:monospace">date-released</span>, <span
style="font-family:monospace">commit</span>, and 
<span
style="font-family:monospace">version</span>, by using the <span
style="font-family:monospace">ignore_suspect_keys</span> parameter, as follows:

<ul>
<li><a href="?url=https://github.com/citation-file-format/cff-converter-python&outputformat=zenodo&ignore_suspect_keys"><span
style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&outputformat=zenodo&ignore_suspect_keys</span></a>
</li></ul>

<h2>Validating</h2>
Validation is also supported. Just include the <span
style="font-family:monospace">validate</span> parameter, as follows

<ul><li><a href="?url=https://github.com/citation-file-format/cff-converter-python&validate"><span style="font-family:monospace">?url=https://github.com/citation-file-format/cff-converter-python&validate</span></a></li></ul>

</body>
</html>
"""


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
        return Response(get_help_text(), mimetype='text/html')

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
                            remove=remove, suspect_keys=suspect_keys, validate=validate, raise_exception=True)
    except Exception as e:
        if str(e) == "Provided CITATION.cff does not seem valid YAML.":
            outstr += "\n\nError: Provided 'cffstr' does not seem valid YAML."
        else:
            outstr += "\n\nError: " + str(e)
        return Response(outstr, mimetype='text/plain')

    acceptable_output_formats = ["bibtex", "cff", "codemeta", "endnote", "schema.org", "ris", "zenodo"]
    if validate:
        pass
    elif outputformat not in acceptable_output_formats:
        outstr += "\n\n'outputformat' should be one of [{0}]".format(", ".join(acceptable_output_formats))
        return Response(outstr, mimetype='text/plain')

    if outputformat is None:
        return
    elif outputformat == "bibtex":
        outstr += citation.as_bibtex()
    elif outputformat == "cff":
        outstr += citation.cffstr
    elif outputformat == "codemeta":
        outstr += citation.as_codemeta()
    elif outputformat == "endnote":
        outstr += citation.as_enw()
    elif outputformat == "ris":
        outstr += citation.as_ris()
    elif outputformat == "schema.org":
        outstr += citation.as_schema_dot_org()
    elif outputformat == "zenodo":
        outstr += citation.as_zenodojson()

    return Response(outstr, mimetype='text/plain')
