from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from register.forms import RegisterForm

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ads:all')
    success_message = 'Welcome to AdSpace, %(username)s! Login to sell your idea!'
    template_name = 'register/signup.html'
