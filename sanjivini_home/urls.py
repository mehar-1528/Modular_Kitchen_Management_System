from .views import customersview,loginview,productview,accessoriesview,paymentview,installmentview,invoiceview,receiptview
from django.urls import path

urlpatterns =[
    path('customers/',customersview),
    path('login/',loginview),
    path('products/',productview),
    path('accessories/',accessoriesview),
    path('payment/',paymentview),
    path('installment/',installmentview),
    path('invoice/',invoiceview),
    path('receipt/',receiptview),
]
