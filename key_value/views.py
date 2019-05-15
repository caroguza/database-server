from django.views.generic import View
from django.http import HttpResponse


stored_key_values = {}


class IndexView(View):
    def get(self, request, *args, **kwargs):
        set_instructions = "Save a key and it's value in memory by doing <i>set?somekey=somevalue</i>"
        get_instructions = "Get the value for and specific key by doing <i>get?key=somekey</i>"
        instructions = f"{set_instructions}<br><br>{get_instructions}"
        return HttpResponse(instructions)


class SetKeyValueView(View):
    """Receives a request and if has key_name=value and stores the values in memory,
    otherwise return a message asking for the values"""
    
    def get(self, request):
        msg = 'Please provide a key and a value to store in memory.'
        if request.GET:
            key = list(request.GET.keys())[0]
            value = list(request.GET.values())[0]
            if value:
                msg = f"The following pair of values was saved! {key} = {value}"
                stored_key_values[key] = value
       
        return HttpResponse(msg)


class GetKeyValueView(View):
    """Receives a request with key=key_name if the key is store in memory return it's value, 
    otherwise returns a message telling if the key doesn't exist or if the url is wrong"""

    def get(self, request):
        response = ''
        if 'key' in request.GET:
            key = request.GET.get('key', False)
            key_value = stored_key_values.get(key, False)
            if not key:
                response = 'Please provide the key whose value you want to get.'
            elif not key_value:
                response = f"The key '{key}' hasn't been stored"
            else:
                response  = f"The value stored for this key is '{key_value}'"
        else:
            response = 'To retrieve a key value you must do key=key_name.'  
        
        return HttpResponse(response)
