from django import template
from django.contrib.auth.forms import AuthenticationForm

from personal_account.forms import  RegisterUserForm, LoginUserForm

register = template.Library()

@register.inclusion_tag('tmptag/modal_window_reg.html')
def show_modal_reg():
    # form = RegUser()
    form = RegisterUserForm()
    return {"form": form,}

@register.inclusion_tag('tmptag/modal_window_in.html')
def show_modal_in():
    form = LoginUserForm()
    return {"form": form,}



