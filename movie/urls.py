from django.urls import path, register_converter
from . import views
import datetime
from django.conf.urls import url

class DateConverter:
    regex = '\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value):
        return value

register_converter(DateConverter, 'yyyy')


urlpatterns=[
    path("",views.index,name='index'),
    path("page",views.page,name='page'),
    path("login",views.login,name='login'),
    path("signup",views.signup,name='signup'),
    path("confirmation",views.confirmation,name='confirmation'),
    path("logout",views.logout,name='logout'),
    path("prebooking",views.prebooking,name='prebooking'),
    path("detail_page/<int:id>",views.detail_page,name='detail_page'),
    path('booking/<str:movie>/<str:date>/',views.booking,name='booking')
]