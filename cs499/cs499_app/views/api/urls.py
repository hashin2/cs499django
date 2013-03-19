from django.conf.urls.defaults import patterns

urlpatterns = patterns('',

    # Test
    (r'^test/?$',
        'cs499.cs499_app.views.api.test.hello_world'),
    (r'^login/$','cs499.cs499_app.views.api.views.login_users'), 
    (r'^newuser/$','cs499.cs499_app.views.api.viewNewUser.new_users'), 
    (r'^files/$','cs499.cs499_app.views.api.viewFiles.user_files'),    
)