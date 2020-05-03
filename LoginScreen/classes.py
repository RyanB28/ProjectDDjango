# This file is to inherit classes from, 
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm
from django.contrib.auth import password_validation
from django import forms
from django.contrib.auth import password_validation 

# Authentication form class
# Deze class zorgt ervoor dat we de juiste layout hebben, en de juiste error message
class OverrideAuthenticationForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class':'form-control'})
    )
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'id':'customCheck1', 'class':'custom-control-input'}))

    error_messages = {
        'invalid_login': (
            " Inlog gegevens zijn incorrect! "
            " Voer de correcte inloggegevens in, of druk op wachtwoord vergeten "
        ),  
        'inactive': ("Deze gebruiker is niet meer actief!"),
    }

# Password change form, dit zorgt ervoor dat we de juiste layout hebben,
class OverridePasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(OverridePasswordChangeForm, self).__init__(*args, **kwargs)
        for fieldname in ['old_password', 'new_password1', 'new_password2']:
            self.fields[fieldname].help_text = None

    error_messages = {
        'password_mismatch': ("De 2 wachtwoorden zijn niet gelijk, voer dezelfde wachtwoord in,"),
        'password_incorrect' : ("Het oude wachtwoord is incorrect, als u dit vergeten bent kunt u uitloggen en een nieuwe wachtwoord aanvragen."),
        'required' : ("Dit veld is nodig om verder te gaan!"),
        'password_too_similar' : ("Wachtwoord en gebruikers naam lijken teveel op elkaar")
        }
    new_password1 = forms.CharField(
        label=("Nieuw wachtwoord"),
        widget=forms.PasswordInput(attrs={'id':"inputOldPassword", 'class':"form-control", "placeholder":"Nieuw wachtwoord"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=("Bevestiging van nieuwe wachtwoord"),
        strip=False,
        widget=forms.PasswordInput(attrs={'id':"inputOldPassword", 'class':"form-control", "placeholder":"Nieuw wachtwoord"}),
    )

    old_password = forms.CharField(
        label=("Oud Wachtwoord"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'id':"inputOldPassword", 'class':"form-control", "placeholder":"Huidige wachtwoord"}),
    )

class OverridePasswordResetForm(PasswordResetForm):
    pass