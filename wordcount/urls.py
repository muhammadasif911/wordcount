from django.urls import path
from . import veiws
urlpatterns = [
    path('',veiws.homepage,name='home'),
    path('aboutus/',veiws.aboutus,name='aboutus'),
    path('count/',veiws.count,name='count'),

]
