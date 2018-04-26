from allauth.account.forms import LoginForm
from crispy_forms.helper import FormHelper

class BLoginForm(LoginForm):
    helper = FormHelper()

