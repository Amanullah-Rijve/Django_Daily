from django import forms 

from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-group'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-group'}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and len(password) <= 8:
            self.add_error('password', 'Password should be minimum 8 characters.')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')



class LoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={'required': 'Email is required.'},
        widget=forms.EmailInput(attrs={'class': 'form-group'})
    )
    password = forms.CharField(
        required=True,
        error_messages={'required': 'Password is required.'},
        widget=forms.PasswordInput(attrs={'class': 'form-group'})
    )

    
    
    