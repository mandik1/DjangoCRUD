from django.forms import ModelForm
from core1.models import Emp


class ArticleForm(ModelForm):
    class Meta:
        model=Emp
        fields = ['emp_name','emp_position','dept']

