from django import forms
from user.models import Profile


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=150, widget=forms.PasswordInput)

    age = forms.IntegerField()
    avatar = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_confirm = cleaned_data['password_confirm']
        age = cleaned_data['age']
        if password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают')
        if age < 1:
            raise forms.ValidationError('Нельзя указать возраст ниже 1')
        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'avatar', 'bio']

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 1:
            raise forms.ValidationError('Возраст не может быть меньше 1')
        return age

class SMSCodeForm(forms.Form):
    code = forms.CharField(max_length=4)