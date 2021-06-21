from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import DateInput
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
  
class Customer(ModelForm):
    class Meta:
        model = CustomerModel
        fields =fields='__all__'
        widgets = {
            'walk_in_date':DateInput(),
            'visit_date':DateInput(),
            'measure_date' :DateInput(),
            'login_date' :DateInput(),
            'dispatch_date' :DateInput(),
            'install_date':DateInput(),
        }
        
class Designer(ModelForm):
    class Meta:
        model =DesignerModel
        fields ='__all__'

class product(ModelForm):
    class Meta:
        model = productModel
        fields ='__all__'

class productcat(ModelForm):
    class Meta:
        model = productCategoryModel
        fields ='__all__'

class accessories(ModelForm):
    class Meta:
        model = accessoriesModel
        fields ='__all__'

class accessoriescat(ModelForm):
    class Meta:
        model = accessoriesCategoryModel
        fields ='__all__'

class OrderForm(ModelForm):
    class Meta:
        model =OrderModel
        fields ='__all__'

