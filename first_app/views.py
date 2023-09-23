# from django.shortcuts import render
from django.views.generic import ListView
from .models import Member
# Create your views here.

class GetMember(ListView):
    model = Member
    context_object_name = 'members'
    template_name = 'templates/member_list.html'