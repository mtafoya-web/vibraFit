#validation + input rendering
from django import forms

class LoginForm(forms.Form):
    ### Creates a text field and handles validation ### "Required"
    username = forms.CharField(
        max_length=150,
        ### render as <input type = "text"> ###
        widget=forms.TextInput
        ### Adds html attributes to the input tag ###
        (attrs={
            "placeholder": "username",
            "class": "login-box",
            "autocomplete": "username",
        })
    )

    password = forms.CharField(
        ### render as <input type="password" ###
        widget = forms.PasswordInput(attrs={
            "placeholder": "password",
            "class": "login-box",
            "autocomplete": "current-password",
        })
    )