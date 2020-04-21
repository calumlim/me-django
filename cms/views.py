from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Portfolio, ClientTestimony

# Create your views here.
class HomePageView(TemplateView):
    template_name = "homepage.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.all()
        context['testimonies'] = ClientTestimony.objects.all()
        return context
