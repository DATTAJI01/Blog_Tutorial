
from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_view,name='list_view'),
    path('<int:pk>/',views.detail_view,name='detail_view')
]
