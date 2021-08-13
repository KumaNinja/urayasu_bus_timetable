from django.urls import path
import urayasubustimetable.views as timetable
 
urlpatterns = [
    path('', timetable.index, name='index'),
    path('test', timetable.test, name="test"),
    ]
