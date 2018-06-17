from django.conf.urls import url
from project.hi.views import HelloView


urlpatterns = [
    url(r'^', HelloView.as_view(), name='home'),
]
