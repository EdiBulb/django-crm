from django import forms
from .models import Sale
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
User = get_user_model()

# 모델폼으로 하면 더 간단해진다. 모델폼은 장고에서 가져와서 사용하면 된다.
class SaleModelForm(forms.ModelForm):
    class Meta: # 메타클래스가 가져와서 어떤 모델을 사용할지 지정하면 된다. 
        model = Sale
        # 필드만 지정해주면 된다. 
        fields = (
            'first_name',
            'last_name',
            'age',
            'person',
        )


class SaleForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)


class 우리만의UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}