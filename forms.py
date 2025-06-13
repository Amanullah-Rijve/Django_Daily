from django import forms

class regform(forms.Form):
    
    name= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':"form-control" ,'id':"name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))
    confirm_password = forms.CharField( widget=forms.PasswordInput(attrs={'class': "form-control"}))
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if  password and len(password) <= 8:
            self.add_error('password','password should be  minimum 8 charcter')
            
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match.')    