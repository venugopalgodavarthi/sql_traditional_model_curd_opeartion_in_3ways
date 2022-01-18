
from django.contrib import admin
from django.urls import path
from pro7 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sample/',views.sample,name='sample'),
    path('insert/',views.insert,name='insert'),
    path('dyinsert/<id>/<name>/<email>/',views.dyinsert,name='dyinsert'),
    path('finsert/',views.finsert,name='finsert'),
    path('select/',views.select,name='select'),
    path('update/',views.update,name='update'),
    path('dyupdate/<id>/<name>/<email>/',views.dyupdate,name='dyupdate'),
    path('fupdate/<data>/',views.fupdate,name='fupdate'),
    path('delete/',views.delete,name='delete'),
    path('dydelete/<id>/',views.dydelete,name='dydelete'),
    path('fdelete/',views.fdelete,name='fdelete'),
    
    
    
    
]
