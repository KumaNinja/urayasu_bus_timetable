<<<<<<< HEAD
from django.urls import path
from urayasubustimetable import views
import urayasubustimetable.views as timetable
 
urlpatterns = [
    path('', timetable.index, name='index'),
    path('test', views.test, name="test"),
=======
from django.urls import path
from urayasubustimetable import views
import urayasubustimetable.views as timetable
 
urlpatterns = [
    path('', timetable.index, name='index'),
    path('test', views.test, name="test"),
>>>>>>> origin/master
]