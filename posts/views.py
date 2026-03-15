from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from articles.models import Article

def redirect_view(request):
    response = redirect(reverse_lazy('home'))
    return response

class HomePageView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "home.html"


