from django.forms import Form
class UserAuthLoginForm(Form):
    email = EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        widgets = {
            "email":forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}),
            "password":forms.TextInput(attrs={'placeholder':'Mot de Passe ','class':'form-control'}),
        }
	    
