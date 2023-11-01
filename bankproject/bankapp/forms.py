from.models import registration
from django import forms
class regform(forms.ModelForm):
    class Meta:
        model=registration
        # fields=['name','email','ph','dob','gender','address','actype','material','state','district','branch']

        fields = '__all__'