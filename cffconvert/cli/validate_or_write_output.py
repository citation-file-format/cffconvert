import click
from jsonschema.exceptions import ValidationError as JsonschemaSchemaError
from pykwalify.errors import SchemaError as PykwalifySchemaError


def validate_or_write_output(outfile, outputformat, validate_only, citation):
    condition = (validate_only, outputformat is not None)
    if condition == (True, False):
        # just validate, there is no target outputformat
        citation.validate()
        print(f"Citation metadata are valid according to schema version {citation.cffversion}.")
    elif condition == (True, True):
        # just validate, ignore the target outputformat
        citation.validate()
        print(f"Ignoring output format. Citation metadata are valid according to schema version {citation.cffversion}.")
    elif condition == (False, False):
        # user hasn't indicated what they want
        print('Indicate whether you want to validate or convert the citation metadata.')
    elif condition == (False, True):
        # validate the input, then write to target outputformat
        try:
            citation.validate()
        except (PykwalifySchemaError, JsonschemaSchemaError):
            print(f"'{citation.src}' does not pass validation. Conversion aborted.")
            ctx = click.get_current_context()
            ctx.exit()
        outstr = {
            "apalike": citation.as_apalike,
            "bibtex": citation.as_bibtex,
            "cff": citation.as_cff,
            "codemeta": citation.as_codemeta,
            "endnote": citation.as_endnote,
            "ris": citation.as_ris,
            "schema.org": citation.as_schemaorg,
            "zenodo": citation.as_zenodo
        }[outputformat]()
        if outfile is None:
            print(outstr, end='')
        else:
            with open(outfile, "w", encoding="utf8") as fid:
                fid.write(outstr)
    else:
        # shouldn't happen
        raise ValueError('Something went wrong validating or writing the output')
