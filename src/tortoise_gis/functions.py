from tortoise.functions import Function

from . import _base_functions as fn


class ST_Area(Function):
    database_func = fn.Area


class ST_AsBinary(Function):
    database_func = fn.AsBinary


class ST_AsGeoJSON(Function):
    database_func = fn.AsGeoJSON


class ST_AsMVT(Function):
    database_func = fn.AsMVT


class ST_GeomFromText(Function):
    database_func = fn.GeomFromText


class ST_DistanceSpheroid(Function):
    database_func = fn.DistanceSpheroid
