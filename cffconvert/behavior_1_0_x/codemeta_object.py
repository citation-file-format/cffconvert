from cffconvert.behavior_1_0_x.schemaorg_object import SchemaorgObject


class CodemetaObject(SchemaorgObject):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]
    supported_codemeta_props = SchemaorgObject.supported_schemaorg_props

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty, context="https://doi.org/10.5063/schema/codemeta-2.0")
