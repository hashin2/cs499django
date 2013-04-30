from django.http import HttpResponseNotAllowed, HttpResponseBadRequest, HttpResponse
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder

import json
import traceback


#********* Purpose *********#
# This file has helper functions to handle formating data into
# a json objects and vice versa change json to its regular data form.
# This code was provided to us by our customer Chris Allen.


# Exception used on bogus json.
class JSONDecodeError(ValueError):
    """
    Exception for when the user sends us bogus json.
    """
    json = ''

    def __init__(self, json, *args, **kwargs):
        self.json = json
        super(JSONDecodeError,self).__init__(*args, **kwargs)

# DSL-ish way to test if the client will accept the given mimetype
def client_accepts(request, mime_type):
    return mime_type in request.META.get('HTTP_ACCEPT')

# Decodes a json string, and raises a JSONDecodeError exception if the json is
# bogus.
def dejsonify(json_str):
    try:
        return json.loads(json_str)
    except ValueError as ve:
        raise JSONDecodeError(json_str, ve.message)

# Converts dict d into json for the api.  query_params is the query parameter
# dict from the request that this json is being used in response to. this
# defaults to None.
def jsonify(d, query_params=None):
    # Set default behavior for parameters
    human = False
    jsonp = None

    # Inspect the query parameters
    if query_params:
        human = bool(__get_int_param(query_params, 'human', 0))
        jsonp = query_params.get('jsonp', None)

    # If nice is set, set indention on the json to four spaces
    if human:
        indent = 4
    else:
        indent = None

    # Make the json.
    json_obj = json.dumps(d, indent=indent, cls=DjangoJSONEncoder)

    # If jsonp is set, then wrap the json in the function call the client
    # passed us.
    if jsonp:
        json_obj = '{jsonp_func}({json_obj})'.format(
            jsonp_func = jsonp,
            json_obj = json_obj)

    # Return the json.
    return json_obj

# Inspects an integer param, and returns it's value as an integer or the 
# default passed in.
def __get_int_param(query_params, param_name, default):
    try:
        value = int(query_params.get(param_name, default))
    except ValueError:
        value = default

    return value


# A request handler that fans out to functions according to http method.
def rest_mux(request, handlers, *args, **kwargs):
    """
    - request is an HttpRequest object.
    - handlers is a dict mapping http methods to callables that handle the 
    request for that method (which should return an HttpResponse object)

    If handler doesn't exist for the OPTION method, one will be added that
    calls __cross_site_preflight_response with default parameters.  If you wish
    to make view not respond to OPTION, pass in the value of 'pass' for
    the 'OPTION' key of the handlers dict.

    The request's query parameters are passed to the handler in the 
    'query_params' kwarg.  The handler can grab them if it cares about them.
    """
    # NOTE for xdr.
    #Tack on a handler for OPTION if there isn't one already.
    #def generate_preflight_response(request, *args, **kwargs):
    #    return __cross_site_preflight_response()
    #handlers.setdefault('OPTIONS', generate_preflight_response)
    
    # Get the request handler per the request's method.
    request_handler = handlers.get(request.method, None)

    if request_handler == None or request_handler == 'pass':
        # NOTE for xdr
        # The method isn't allowed.
        #methods = handlers.keys()
        #if handlers.get('OPTIONS', 'pass') == 'pass':
        #    # The caller wanted to disallow OPTION, so take it out of the
        #    # methods list we'll return in the Allow header.
        #    methods = filter(lambda m: m != 'OPTION', methods)
        return HttpResponseNotAllowed(handlers.keys())
    else:
        # The method is allowed, so call it's handler.
        query_params = request.REQUEST
        try:
            response =  request_handler(
                request, *args, query_params=query_params, **kwargs)
            #response['Access-Control-Allow-Origin'] = '*'; # NOTE for xdr
            return response
        except JSONDecodeError as jde:
            return json_400_bad_request(jde, custom_message=jde.json)
        except ValidationError as ve:
            return json_400_bad_request(ve)

# A quick way to generate a response with status 400, bad request.  This takes
# one string argument that will be returned in the json error message of the
# form: '{"error": "message"}'.  The message should be something about why the
# request was bogus.
def json_400_bad_request(exception, custom_message=None):
    messages = traceback.format_exception_only(type(exception), exception)
    if custom_message:
        messages.append(custom_message)
    return HttpResponseBadRequest(
        jsonify({'errors': messages}), mimetype='application/json')

# A quick way to generate a response with status 401, unauthorized.
def json_401_unauthorized():
    response = HttpResponse(
        jsonify({'error': 'Unauthorized, please login first.'}),
        mimetype='application/json')
    response.status_code = 401
    return response


# Generates a response to an OPTIONS request in preflight cross-site ajax
# requests.  Tells the client that it's okay to send us requests even when
# the javascript that's talking to us came from off our site.  Only do this
# if you know what you're doing.  
# allow_origin is a list of domains for which cross-site requests are allowed.
# this defaults to '*' (all domains).  allow_methods is a list of http methods
# that are allowed for cross-site requests.  this defaults to 'GET, PUT, POST,
# DELETE, OPTIONS'.  max_age is a number of seconds for which this preflight
# request may be cached.  this defaults to '300'.  allow_headers is a list of
# http headers that may be included in cross-site requests.  this defaults to
# none ('').
# NOTE For xdr.
#def __cross_site_preflight_response(
#    allow_origin='*', 
#    allow_methods='GET, PUT, POST, DELETE, OPTIONS',
#    max_age='300',
#    allow_headers='X-Requested-With'
#):
#    response = HttpResponse()
#    response['Access-Control-Allow-Origin'] = allow_origin
#    response['Access-Control-Allow-Methods'] = allow_methods
#    response['Access-Control-Max_Age'] = max_age
#    response['Access-Control-Allow-Headers'] = allow_headers
#
#    return response
