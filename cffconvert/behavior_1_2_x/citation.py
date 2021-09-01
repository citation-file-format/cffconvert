import jsonschema
import json
import os
from ruamel.yaml import YAML
from cffconvert.contracts.citation import Contract
from cffconvert.root import get_package_root


class Citation_1_2_x(Contract):

    SUPPORTED_CFF_VERSIONS = [
        "1.2.0"
    ]

    def __init__(self, cffstr, cffversion):
        self.cffstr = cffstr
        self.cffversion = cffversion
        self.cffobj = self._parse()
        self.schema = self._get_schema()

    def _get_schema(self):
        schema_path = os.path.join(get_package_root(), "schemas", "1.2.0", "schema.json")
        with open(schema_path, "rt") as fid:
            return json.loads(fid.read())

    def _parse(self):
        # instantiate the YAML module:
        yaml = YAML(typ="safe")

        # while loading, convert timestamps to string
        yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:timestamp'] = \
            yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:str']

        cffobj = yaml.load(self.cffstr)

        if not isinstance(cffobj, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")

        return cffobj

    def validate(self):
        jsonschema.validate(instance=self.cffobj, schema=self.schema, format_checker=jsonschema.FormatChecker())
