from django.conf.urls import include, url
from django.contrib import admin
#admin.autodiscover()

from .views import HomePageView, SignUpView, LoginView, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', HomePageView.as_view(), name='home'),
    url(r'^accounts/register/$', SignUpView.as_view(), name='sign_up'),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),

    url(r'^talks/', include('talks.urls', namespace='talks')),
]
