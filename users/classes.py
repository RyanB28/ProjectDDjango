from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm
from django import forms
from django.contrib.auth import password_validation 

# Override Authentication form, hierin kan je aanpassingen doen aan de authenticatie, 
class OverrideAuthenticationForm(AuthenticationForm):
    username = UsernameField(label="Gebruikernaam",widget=forms.TextInput(attrs={'autofocus': True, 'class':'form-control'}))
    password = forms.CharField(
        label=("Wachtwoord"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autofocus': True, 'class':'form-control'})
    )

    error_messages = {
        'invalid_login': (
            " Inlog gegevens zijn incorrect! "
            " Voer de correcte inloggegevens in, of druk op wachtwoord vergeten "
        ),  
        'inactive': ("Deze gebruiker is niet meer actief!"),
    }

    # hierin wordt de login form aangeroepen, en die neemt authenticatie over, alleen die hebben wij aangepast   
    # daarom dat het hier ook overreden wordt met loginView
class OverrideLogin(auth_views.LoginView):
    form_class = OverrideAuthenticationForm
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    