from django.shortcuts import redirect, render
from .forms import *
from django.db.models.functions import Lower
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.db.models import Sum,F
from datetime import date



# Create your views here.

def loginview(request):
    return render(request,"login.html")

def loginuser(request):
    #user=User.objects.create_user('Sanjivini','a@123','sanjivini123').save()
    username=request.POST['username']
    password=request.POST['password']
   
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect("homepage")
    else:
       
        messages.add_message(request, messages.INFO, 'Invalid Login.')
        return redirect(request.META['HTTP_REFERER'])

def homepageview(request):
    fullcust=CustomerModel.objects.filter(customer_type__contains='Full').count()
    retail=CustomerModel.objects.filter(customer_type__contains='Retail').count()
    product =OrderModel.objects.aggregate(co=Count('accessories'))
    acc =OrderModel.objects.aggregate(po =Count('product'))
    amount=OrderModel.objects.aggregate(the_sum = Sum(F('product__mrp')+F('accessories__mrp')))
    cust=CustomerModel.objects.filter(walk_in_date__contains=date.today()).count()
    acc_graph = OrderModel.objects.values('product_id').order_by('product_id').annotate(cou=Count('product'))
    params={'retail':retail,'fullcust':fullcust,'product':product,'acc':acc,'cust':cust,'amount':amount,'data':acc_graph}
    return render(request,'homepage.html',params)

def successview(request):
    return render(request,"success.html")


def accessoriesview(request):
    return render(request,"accessories.html")



def customersview(request):
    
    customers= CustomerModel.objects.all().order_by(Lower('fname'))
    context ={'customers':customers}
    return render(request,"customers.html" ,context)

def addcustomer(request):
    form = Customer()
    if request.method == 'POST':
        form=Customer(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context ={'form':form}
    return render(request,"addcustomer.html",context)


def searchcustomer(request):
    query = request.GET['searchcustomer']
    allcustomers = CustomerModel.objects.filter(fname__icontains=query)
    params ={'allcustomers':allcustomers,'query':query}
    return render(request,"searchcustomer.html",params)

def editcustomer(request,pk):
    customer =CustomerModel.objects.get(id=pk)
    form = Customer(instance=customer)
    if request.method == 'POST':
        form=Customer(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return render(request,'success.html')

    context = {'form':form}
    return render(request,"addcustomer.html",context)

def productsview(request):  
    products= productModel.objects.all()
    context ={'products':products}
    return render(request,"products.html" ,context)

def addproductcat(request):
    form = productcat()
    if request.method == 'POST':
        form=productcat(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context ={'form':form}
    return render(request,"addproductcat.html",context)

def addproduct(request):
    form = product()
    if request.method == 'POST':
        form=product(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context ={'form':form}
    return render(request,"addproduct.html",context)


def searchproduct(request):
    query = request.GET['searchproduct']
    allproducts = productModel.objects.filter(name__icontains=query)
    params ={'allproducts':allproducts,'query':query}
    return render(request,"searchproduct.html",params)

def editproduct(request,pk):
    Product =productModel.objects.get(id=pk)
    form = product(instance=Product)
    if request.method == 'POST':
        form=product(request.POST,instance=Product)
        if form.is_valid():
            form.save()
            return render(request,'success.html')

    context = {'form':form}
    return render(request,"addproduct.html",context)

def deleteproduct(request,pk):
    Product =productModel.objects.get(id=pk)
    Product.delete()
    return render(request,'success.html')


def accessoriesview(request):  
    accessories= accessoriesModel.objects.all()
    context ={'accessories':accessories}
    return render(request,"accessories.html" ,context)

def addaccessoriescat(request):
    form = accessoriescat()
    if request.method == 'POST':
        form=accessoriescat(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context ={'form':form}
    return render(request,"addaccessoriescat.html",context)

def addaccessories(request):
    form = accessories()
    if request.method == 'POST':
        form=accessories(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])

    context ={'form':form}
    return render(request,"addaccessories.html",context)


def searchaccessories(request):
    query = request.GET['searchaccessories']
    allaccessories = accessoriesModel.objects.filter(code__icontains=query)
    params ={'allaccessories':allaccessories,'query':query}
    return render(request,"searchaccessories.html",params)

def editaccessories(request,pk):
    Accessories =accessoriesModel.objects.get(id=pk)
    form = accessories(instance=Accessories)
    if request.method == 'POST':
        form=accessories(request.POST,instance=Accessories)
        if form.is_valid():
            form.save()
            return render(request,'success.html')

    context = {'form':form}
    return render(request,"addaccessories.html",context)

def deleteaccessories(request,pk):
    accessories =accessoriesModel.objects.get(id=pk)
    accessories.delete()
    return render(request,'success.html')

def addDesigner(request):
    form = Designer
    if request.method == 'POST':
        form=Designer(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META['HTTP_REFERER'])
    
    designers= DesignerModel.objects.all().order_by(Lower('dname'))
    params ={'designers':designers,'form':form}
    
    return render(request,"designer.html",params)

def orders(request,pk):
    OrderFormSet = inlineformset_factory(CustomerModel,OrderModel,fields=('product','accessories'),extra=15)
    customer = CustomerModel.objects.get(id=pk)
    custom =CustomerModel.objects.filter(pk=pk)
    formset = OrderFormSet(queryset=OrderModel.objects.none(),instance=customer)
    if request.method == 'POST':
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect(request.META['HTTP_REFERER'])

    orders = OrderModel.objects.filter(customer_id=pk)
    params ={'formset':formset,'custom':custom,'orders':orders}

    return render(request,"orders.html",params)

def invoiceview(request,pk):
    order=OrderModel.objects.filter(customer_id=pk)
    customer = CustomerModel.objects.filter(pk=pk)
    amount=OrderModel.objects.filter(customer_id=pk).aggregate(the_sum = Sum(F('product__mrp')+F('accessories__mrp')))
    
    
    params={'order':order,'customer':customer,'amount':amount}
    return render(request,"invoice.html",params)


def paymentview(request,pk):
    customer = CustomerModel.objects.get(id=pk)
    amount=OrderModel.objects.filter(customer_id=pk).aggregate(the_sum = Sum(F('product__mrp')+F('accessories__mrp')))
    
  
    params={'customer':customer,'amount':amount}
    return render(request,"payment.html",params)

def installmentview(request,pk):
    customer = CustomerModel.objects.get(id=pk)
    
    """ form = InstallForm(instance=customer)
    if request.method == 'POST':
        form=InstallForm(request.POST,instance=customer)
        if form.is_valid():
            print("debug")
            form.save()
            return redirect(request.META['HTTP_REFERER'])"""

    install =InstallModel.objects.filter(payid_id=pk)
    balance =OrderModel.objects.filter(customer_id=pk).aggregate(the_sum = (Sum(F('product__mrp')+F('accessories__mrp'))))
    params={'customer':customer,'install':install,'balance':balance}
    return render(request,"installment.html",params)

   

def installmentsave(request,custid):
    customer = CustomerModel.objects.get(id = custid)
    amount = request.POST['amount']
    pdate = request.POST['pdate']
    mop = request.POST['mop']
    cheque = request.POST['cheque']
    InstallModel(payid = customer,amount_paid = amount,date = pdate,mode_of_pay = mop,chequeno = cheque).save()
    return redirect(request.META['HTTP_REFERER'])

def receiptview(request,pk):
    install =InstallModel.objects.get(id=pk)
    params={'install':install}
    return render(request,"receipt.html",params)
