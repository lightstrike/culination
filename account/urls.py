"""
URLconf for registration and activation, cloned django-registration's
one-step backend.

This will also automatically set up the views in
``django.contrib.auth`` at sensible default locations.
"""


from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from registration.views import activate, register
from .views import *
from .forms import LoginForm


urlpatterns = patterns('',
                       url(r'^register/$',
                           register,
                           {'backend': 'account.backends.RegistrationBackend'},
                           name='register'),
                       url(r'^register/closed/$',
                           direct_to_template,
                           {'template': 'registration/registration_closed.html'},
                           name='registration_disallowed'),
                       url(r'^password_reset/$', password_reset, name="password_reset"),
                       (r'^login/?$','django.contrib.auth.views.login',{ 'authentication_form':LoginForm}),

                       (r'', include('registration.auth_urls')),
                       )