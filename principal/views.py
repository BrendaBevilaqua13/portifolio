from django.shortcuts import render
from django.views.generic import TemplateView
from principal.models import Contact
import ipdb

class HomeTemplateView(TemplateView):
    template_name = 'principal\pages\home.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.first()
        context['lista'] = [1,2,3]

        return context