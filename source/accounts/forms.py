from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from accounts.models import Signatures


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label=_('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise forms.ValidationError(_('You entered an invalid password.'))

        return password


class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label=_('Username'))

    @property
    def field_order(self):
        return ['username', 'password', 'remember_me']

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(_('You entered an invalid username.'))

        if not user.is_active:
            raise forms.ValidationError(_('This account is not active.'))

        self.user_cache = user

        return username


class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Last name'), max_length=150, required=False)


class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signatures
        fields = ("img",)
