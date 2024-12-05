from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label="Введите логин")
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Введите пароль")
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label="Повторите пароль")
    age = forms.IntegerField(min_value=0, max_value=999, label="Введите свой возраст")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password != repeat_password:
            raise forms.ValidationError("Пароли не совпадают")
        return cleaned_data