from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import Profile
from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # Save the user
        response = super().form_valid(form)

        # Create a profile for the user
        Profile.objects.create(user=self.object)
        # (Optional) Automatically login the user
        login(self.request, self.object)

        return response

class ProfileView(DetailView):
    model = Profile
    template_name = "profile.html"

    # specify the name for data in HTML
    context_object_name = "profile_obj"

    # tell django to find the profile not by ID, but by username field
    slug_field = "user__username"
    slug_url_kwarg = "username"
