from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from home.forms import RegisterForm

# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations

class SignUpView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('ads:all')
    success_message = 'Welcome to AdSpace, %(username)s! Login to sell your idea!'
    template_name = 'registration/signup.html'
