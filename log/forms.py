from django import forms
from log.models import CustomUser, UserRole


# Create your forms here.


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder': 'password'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'placeholder': 'Confirm password'}), label='Confirm Password')
    role = forms.ModelChoiceField(queryset= UserRole.objects.all().order_by('name'), to_field_name="id")
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','mobile_number','role','password']

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
                raise forms.ValidationError("Password and Confirm Password Does Not Match")

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',widget = forms.PasswordInput(attrs={'class':'form-control'}))