from .views import *
from django.urls import path


urlpatterns =[
    path('homepage/',homepageview,name="homepage"),
    path('login/validate/',loginuser,name="loginuser"),
    path('',loginview,name="loginpage"),
    path('success/',successview,name="success"),
    path('designer/',addDesigner,name="designer"),


    path('customers/',customersview ,name="customersview"),
    path('addcustomer/',addcustomer,name="addcustomer"),
    path('searchcustomer/',searchcustomer,name="searchcustomer"),
    path('editcustomer/<int:pk>/',editcustomer,name="editcustomer"),
   
    path('products/',productsview,name="products"),
    path('addproduct/',addproduct,name="addproduct"),
    path('addproductcat/',addproductcat,name="addproductcat"),
    path('searchproduct/',searchproduct,name="searchproduct"),
    path('editproduct/<int:pk>/',editproduct,name="editproduct"),
    path('deleteproduct/<int:pk>/',deleteproduct,name="deleteproduct"),
    
   

    path('accessories/',accessoriesview, name='accessoriesview'),
    path('addaccessories/',addaccessories,name="addaccessories"),
    path('addaccessoriescat/',addaccessoriescat,name="addaccessoriescat"),
    path('searchaccessories/',searchaccessories,name="searchaccessories"),
    path('editaccessories/<int:pk>/',editaccessories,name="editaccessories"),
    path('deleteaccessories/<int:pk>/',deleteaccessories,name="deleteaccessories"),

    path('orders/<int:pk>',orders,name="orders"),

   
    path('payment/<int:pk>',paymentview,name="payment"),

    path('installment/<int:pk>/',installmentview,name="installment"),
    path('installment/<int:custid>/save/',installmentsave),

    path('invoice/<int:pk>/',invoiceview,name='invoice'),
    path('receipt/<int:pk>/',receiptview,name='receipt'),
    
    
]
