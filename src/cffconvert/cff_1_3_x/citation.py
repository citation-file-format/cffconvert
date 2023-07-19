import json
import os
import jsonschema
from jsonschema.exceptions import ValidationError
from ruamel.yaml import YAML
from cffconvert.cff_1_3_x.apalike import ApalikeObject
from cffconvert.cff_1_3_x.bibtex import BibtexObject
from cffconvert.cff_1_3_x.codemeta import CodemetaObject
from cffconvert.cff_1_3_x.endnote import EndnoteObject
from cffconvert.cff_1_3_x.ris import RisObject
from cffconvert.cff_1_3_x.schemaorg import SchemaorgObject
from cffconvert.cff_1_3_x.zenodo import ZenodoObject
from cffconvert.contracts.citation import Contract
from cffconvert.root import get_package_root


class Citation_1_3_x(Contract):  # noqa

    supported_cff_versions = [
        "1.3.0"
    ]

    def __init__(self, cffstr, cffversion):
        self.cffstr = cffstr
        self.cffversion = cffversion
        self.cffobj = self._parse()
        self.schema = self._get_schema()

    def _get_schema(self):
        schema_path = os.path.join(get_package_root(), "schemas", "1.3.0", "schema.json")
        with open(schema_path, "rt", encoding="utf-8") as fid:
            return json.loads(fid.read())

    def _parse(self):
        # instantiate the YAML module:
        yaml = YAML(typ="safe")

        # while loading, convert timestamps to string
        yaml.constructor.yaml_constructors["tag:yaml.org,2002:timestamp"] = \
            yaml.constructor.yaml_constructors["tag:yaml.org,2002:str"]

        cffobj = yaml.load(self.cffstr)

        if not isinstance(cffobj, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")

        return cffobj

    def as_apalike(self):
        return ApalikeObject(self.cffobj).as_string()

    def as_bibtex(self):
        return BibtexObject(self.cffobj).as_string()

    def as_cff(self):
        return self.cffstr

    def as_codemeta(self):
        return CodemetaObject(self.cffobj).as_string()

    def as_endnote(self):
        return EndnoteObject(self.cffobj).as_string()

    def as_ris(self):
        return RisObject(self.cffobj).as_string()

    def as_schemaorg(self):
        return SchemaorgObject(self.cffobj).as_string()

    def as_zenodo(self):
        return ZenodoObject(self.cffobj).as_string()

    def validate(self, verbose=True):
        try:
            jsonschema.validate(instance=self.cffobj, schema=self.schema, format_checker=jsonschema.FormatChecker())
        except ValidationError as error:
            error_lines = str(error).splitlines()
            n_lines_max = 15
            is_long = len(error_lines) > n_lines_max
            if is_long and not verbose:
                truncated_message = "\n".join([
                    *error_lines[:n_lines_max],
                    "",
                    "...truncated output...",
                    "Add --verbose flag for full output."
                ])
                # pylint:disable = raise-missing-from
                raise ValidationError(truncated_message)
            raise
