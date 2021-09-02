import os
from pykwalify.core import Core
from ruamel.yaml import YAML
from cffconvert.contracts.citation import Contract
from cffconvert.root import get_package_root
from cffconvert.behavior_1_1_x.bibtex import BibtexObject


class Citation_1_1_x(Contract):

    supported_cff_versions = [
        "1.1.0"
    ]

    def __init__(self, cffstr, cffversion):
        self.cffstr = cffstr
        self.cffversion = cffversion
        self.cffobj = self._parse()
        self.schema = self._get_schema()

    def _get_schema(self):
        schema_path = os.path.join(get_package_root(), "schemas", self.cffversion, "schema.yaml")
        with open(schema_path, "rt") as fid:
            return YAML(typ="safe").load(fid.read())

    def _parse(self):
        cffobj = YAML(typ="safe").load(self.cffstr)
        if not isinstance(cffobj, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")
        return cffobj

    def as_bibtex(self, reference='YourReferenceHere'):
        return BibtexObject(self.cffobj).print(reference)

    def validate(self):
        # validation using YAML based schema
        Core(source_data=self.cffobj, schema_data=self.schema).validate(raise_exception=True)
