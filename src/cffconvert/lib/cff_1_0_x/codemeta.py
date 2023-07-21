from cffconvert.lib.cff_1_0_x.schemaorg import SchemaorgObject


class CodemetaObject(SchemaorgObject):

    def __init__(self, cffobj, context="https://doi.org/10.5063/schema/codemeta-2.0", initialize_empty=False):
        super().__init__(cffobj, context=context, initialize_empty=initialize_empty)
