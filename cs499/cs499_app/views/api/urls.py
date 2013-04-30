from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

<<<<<<< HEAD
#********* Purpose *********#
# maps the url input to the corresponding function for the url.
# The only one in this file is for handling the POST request

urlpatterns = patterns('',
    # Test
    (r'^post/?$', 'cs499.cs499_app.views.api.post.api_request'), 
)
=======
urlpatterns = patterns('',
    # Test
    (r'^test/?$',
        'cs499.cs499_app.views.api.test.hello_world'),
    
 #    # (r'^login/', include(admin.site.urls)),
 #    (r'^login/', 'cs499.cs499_app.views.api.views.login'),
 #    # (r'^login/', 'django.contrib.auth.views.login'),
 #    # (r'^accounts/',include('registration.backends.default.urls')),
 #    (r'^register/', 'cs499.cs499_app.views.api.views.register'),
 #    (r'^base/', 'cs499.cs499_app.views.api.views.base'),
 #    (r'^validate', 'cs499.cs499_app.views.api.views.validate'),
 #    url(r'^authenticate/(?P<service>[a-z]+)/$', 'authenticate_redirect',name='authenticate_redirect'),
	# url(r'^authorize/callback/$', 'authorize_callback',	name='authorize_callback'),

 #    # (r'^creatingUser/$','cs499.cs499_app.views.api.viewNewUser.new_users'),    
    # (r'^files/$','cs499.cs499_app.views.api.viewFiles.user_files'),    
)

# {% url 'django.contrib.auth.views.login' %}

>>>>>>> 11315b61f739cbec77d8c1b402ba235432d88cb4
