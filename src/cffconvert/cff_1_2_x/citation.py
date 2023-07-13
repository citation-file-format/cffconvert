import json
import os
import jsonschema
from jsonschema.exceptions import ValidationError
from ruamel.yaml import YAML
from cffconvert.cff_1_2_x.apalike_object import ApalikeObject
from cffconvert.cff_1_2_x.bibtex_object import BibtexObject
from cffconvert.cff_1_2_x.codemeta_object import CodemetaObject
from cffconvert.cff_1_2_x.endnote_object import EndnoteObject
from cffconvert.cff_1_2_x.ris_object import RisObject
from cffconvert.cff_1_2_x.schemaorg_object import SchemaorgObject
from cffconvert.cff_1_2_x.zenodo_object import ZenodoObject
from cffconvert.contracts.citation import Contract
from cffconvert.root import get_package_root


# pylint: disable=invalid-name
class Citation_1_2_x(Contract):  # nopep8

    supported_cff_versions = [
        "1.2.0"
    ]

    def __init__(self, cffstr, cffversion):
        self.cffstr = cffstr
        self.cffversion = cffversion
        self.cffobj = self._parse()
        self.schema = self._get_schema()

    def _get_schema(self):
        schema_path = os.path.join(get_package_root(), "schemas", "1.2.0", "schema.json")
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
                raise ValidationError(truncated_message) from error
            raise
