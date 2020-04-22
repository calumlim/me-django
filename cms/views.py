from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail

from django.conf import settings
from .models import Portfolio, ClientTestimony
from .forms import ContactForm

# Create your views here.
class HomePageView(FormView):
    form_class = ContactForm
    template_name = "homepage.html"
    success_url = reverse_lazy('cms:homepage')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = Portfolio.objects.all()
        context['testimonies'] = ClientTestimony.objects.all()
        return context
    
    def form_valid(self, form):
        content = "From {first_name} {last_name} / {email} said:\n {message}".format(
            first_name = form.cleaned_data.get('first_name'),
            last_name = form.cleaned_data.get('last_name'),
            email = form.cleaned_data.get('email'),
            message = form.cleaned_data.get('content')
        )
        user_email = form.cleaned_data.get('email')
        subject = form.cleaned_data.get('subject')

        send_mail(
            subject = subject,
            message = content,
            from_email = user_email,
            recipient_list = settings.LIST_OF_EMAIL_RECIPIENTS,
            fail_silently = False
        )
        return super(HomePageView, self).form_valid(form)
    def form_invalid(self, form):
        
        return super(HomePageView, self).form_invalid(form)

class RedirectPortfolio(DetailView):
    model = Portfolio
    template_name = "portfolio-redirect.html"
    
