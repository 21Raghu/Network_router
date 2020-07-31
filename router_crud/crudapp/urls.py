from django.urls import path, include
from rest_framework import routers
from .views import GetRouterList, RouterData, AddData

urlpatterns = [
    path('', GetRouterList.as_view()),
    path('get_router/<int:router_id>/', RouterData.as_view()),
    path('add/', AddData.as_view()),
    path('update/<int:router_id>', RouterData.as_view()),
    path('delete/<int:router_id>/', GetRouterList.as_view()),
]
