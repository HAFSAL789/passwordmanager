from .models import AddItem
from django.forms import ModelForm, formset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class User_create_form(UserCreationForm):
    pass


class login_form(AuthenticationForm):
    pass


class Add_item_form(ModelForm):
    class Meta:
        model = AddItem
        fields = ['Title', 'password',]


class Display_Item_Form(ModelForm):
    delete_item = forms.BooleanField()

    def save(self):
        if self.cleaned_data['delete_item']:
            self.instance.delete()
        else:
            self.instance.save()
    class Meta:
        model = AddItem
        fields = ['Title', 'password',]



Display_formset = formset_factory(Display_Item_Form, extra=0)
