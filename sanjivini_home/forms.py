from django.db.models import fields
from django.forms import ModelForm
from .models import *

class Customer(ModelForm):
    class Meta:
        model = CustomerModel
        fields ='__all__'
        
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

