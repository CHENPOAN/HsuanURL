from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, URLRedirectView

# DO NOT DO
# from shortener import views
# from another_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$', URLRedirectView.as_view(), name='scode'),  # $為結尾字符,此url在$不會有參數

    # DO NOT DO
    # url(r'^abc/$', views.HsuanURL),
]
