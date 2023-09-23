from django.urls import path
from .views import GetMember

urlpatterns = [
    path('',GetMember.as_view(),name = 'member_list')
]
