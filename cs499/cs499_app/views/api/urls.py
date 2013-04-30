from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

#********* Purpose *********#
# maps the url input to the corresponding function for the url.
# The only one in this file is for handling the POST request

urlpatterns = patterns('',
    # Test
    (r'^post/?$', 'cs499.cs499_app.views.api.post.api_request'), 
)