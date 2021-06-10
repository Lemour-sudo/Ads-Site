from django.urls import reverse_lazy
from django.views.generic import CreateView
from register.forms import RegisterForm

class SignUpView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ads')
    template_name = 'register/signup.html'
