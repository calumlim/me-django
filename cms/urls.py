from django.urls import path
from . import views

app_name = "cms"
urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("portfolio/<int:pk>", views.RedirectPortfolio.as_view(), name='redirect'),
]