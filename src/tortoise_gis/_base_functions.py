from pypika.terms import Function


_DEFAULT_SRID = 4326


class Area(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_Area", term, alias=alias)


class AsBinary(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_AsBinary", term, alias=alias)


class AsGeoJSON(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_AsGeoJSON", term, alias=alias)


class AsMVT(Function):
    def __init__(self, term, alias=None):
        super().__init__("ST_AsMVT", term, alias=alias)


class GeomFromText(Function):
    def __init__(self, term, alias=None, srid=None):
        super().__init__("ST_GeomFromText", str(term), srid or _DEFAULT_SRID, alias=alias)
