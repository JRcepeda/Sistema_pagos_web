
from django.urls import path 
from .views import fuente,datos_sql,datos_sql2,datos_trans,datos_trans2

#urls relacionadas con tareas/ rutas

urlpatterns = [path('',fuente,name='fuente'),
               path('new/',datos_sql,name='datos_sql'),
               path('new2/',datos_sql2,name='datos_sql2'),
               path('new3/',datos_trans,name='datos_trans'),
               path('new4/',datos_trans2,name='datos_trans2')]#si se le coloca una ruta en '' no llega directo a consulta
