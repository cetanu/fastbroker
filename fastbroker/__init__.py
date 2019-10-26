import json
from pkg_resources import get_distribution
try:
    import ujson
except ImportError:
    import starlette.responses
    starlette.responses.ujson = json
    ujson = json


__versionstr__ = get_distribution('fastbroker').version
