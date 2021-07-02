from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class LoginView(LoginView):

    form_class = AuthenticationForm
    template_name = 'account/login.html'

login = LoginView.as_view()