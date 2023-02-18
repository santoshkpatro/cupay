from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login

from .forms import LoginForm


class LoginView(TemplateView):
    template_name = "accounts/login.html"

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(data=request.POST)

        if not login_form.is_valid():
            return super().get(request, *args, **kwargs)

        data = login_form.cleaned_data
        print(data)
        return super().get(request, *args, **kwargs)