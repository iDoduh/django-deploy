from django.http import HttpResponse
from .serializers import JSONSerializer


def json_response(func):
    """
    A decorator thats takes a view response and turns it
    into json. If a callback is added through GET or POST
    the response is JSONP.
    """

    def decorator(request, *args, **kwargs):
        objects = func(request, *args, **kwargs)

        json_serializer = JSONSerializer()

        if isinstance(objects, HttpResponse):
            return objects
        try:
            data = json_serializer.serialize(objects)
            if 'callback' in request.REQUEST:
                # a jsonp response!
                data = '%s(%s);' % (request.REQUEST['callback'], data)
                return HttpResponse(data, "text/javascript")
        except:
            data = json_serializer.serialize(str(objects))
        return HttpResponse(data, "application/json")

    return decorator





