
from . import YappiProfiler

def getMetaData():
    return {    }


def register(app):
    return { "extension":  YappiProfiler.YappiProfiler()}
