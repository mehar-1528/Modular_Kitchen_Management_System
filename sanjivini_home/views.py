from django.shortcuts import render

# Create your views here.
def customersview(request):
    return render(request,"customers.html")

def loginview(request):
    return render(request,"login.html")

def productview(request):
    return render(request,"products.html")

def accessoriesview(request):
    return render(request,"accessories.html")

def paymentview(request):
    return render(request,"payment.html")

def installmentview(request):
    return render(request,"installment.html")

def invoiceview(request):
    return render(request,"invoice.html")

def receiptview(request):
    return render(request,"receipt.html")
