from cffconvert.behavior_1_2_x.schemaorg_object import SchemaorgObject


class CodemetaObject(SchemaorgObject):

    supported_cff_versions = [
        '1.2.0'
    ]
    supported_codemeta_props = SchemaorgObject.supported_schemaorg_props

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty, context="https://doi.org/10.5063/schema/codemeta-2.0")
