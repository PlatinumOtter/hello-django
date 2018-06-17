from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HelloView(View):

    def dispatch(request, *args):
        response_html = "<html><head><title>Hello World!</title></head><body><h1>Hello World</h1></body></html>"
        return HttpResponse(response_html)
