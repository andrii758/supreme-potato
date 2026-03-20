from django.urls import reverse_lazy, reverse
from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Profile
from .forms import SignUpForm, ProfileUpdateForm

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

class ProfileEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = ProfileUpdateForm
    template_name = "profile_edit.html"
    # it cannot add the username dynamically
    # success_url = reverse_lazy('profile')
    success_message = "Your profile is updated successfully"

    def get_object(self):
        # this tells django to use the logged-in user
        # instead of looking for a pk/slug in the URL
        return self.request.user.profile

    def get_success_url(self):
        # we take the username of current user and transfer it to reverse()
        return reverse('profile', kwargs={'username': self.request.user.username})
