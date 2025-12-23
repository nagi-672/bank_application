from django.shortcuts import render,redirect
from bankapp.models import Banking
from bankapp.forms import bankForm, balanceForm,depositForm,withdrawalForm,transferForm,closeAccountForm
from django.http import HttpResponse
from django.http import HttpRequest
# Create your views here.
def new_account(request):
    form = bankForm()
    bank = Banking.objects.all()
    msg=""
    if request.method=="POST":
        form = bankForm(request.POST)  
        if form.is_valid():
            form.save()
            return render(request,'new_account_success.html',{"form":form})
        return render(request,'new_account.html',{"form":form})
    else:
        form = bankForm()
    return render(request,'new_account.html',{"form":form})

def home(request):
    return render(request,'home.html')

def balance(request):
    form = balanceForm()
    bank = Banking.objects.all()
    if request.method=="POST":
        form = balanceForm(request.POST)
        account_no = request.POST['account_no']
        name = request.POST['name']
        password = request.POST['password']
        bank = Banking.objects.filter(
            account_no=account_no,
            name=name,
            password=password,
        ).first()
        if bank:
            return render(request,"balance_success.html",{"bank":bank})
        else:
            return HttpResponse("Invalid details")
    return render(request,'balance.html',{"form":form})

def balance_success(request):
    return render(request,"balance_success.html",{"banking":Banking})

def deposit(request):
    bank = Banking.objects.all()
    form = depositForm()
    if request.method == "POST":
        form = depositForm(request.POST)
        if form.is_valid():
          cd = form.cleaned_data
          account_no = cd['account_no']
          name = cd['name']
          password = cd['password']
          try:
             bank=Banking.objects.get(
               account_no=account_no,
               name=name,
               password =password
             )
          except Banking.DoesNotExist:
              return render(request,'deposit.html',{
                  "form":form,
                  "error": "Invalid account or Password"
              }) 
          existing_amount=bank.amount
          deposit_amount=cd['amount']
          bank.amount = existing_amount + deposit_amount
          bank.save()
          return render(request,'deposit_success.html',{'existing_amount':existing_amount,'deposit_amount':deposit_amount,'account':bank},)
        return render(request,'deposit.html',{"form":form})
    else:
          form = depositForm()
    return render(request,'deposit.html',{"form":form})
def deposit_success(request):
    return render(request,'deposit_success.html')

def withdraw(request): 
    bank = Banking.objects.all
    msg = ""
    form = withdrawalForm()
    if request.method == "POST":
        form = withdrawalForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            account_no = cd['account_no']
            name = cd['name']
            password = cd['password']
            try:
                bank = Banking.objects.get(
                    account_no = account_no,
                    name = name,
                    password = password
                )
            except Banking.DoesNotExist:
                return render(request,'withdraw.html',{
                    "form":form,
                    "error":"Invalid Account or Password"
                })    
            
            existed_amount = bank.amount
            withdraw_amount = cd['amount']
            if existed_amount<withdraw_amount:
                msg = "Insufficient balance"
                return render(request,'withdraw.html',{"form":form,"msg":msg})
            bank.amount = existed_amount-withdraw_amount
            bank.save()
            return render(request,'withdraw_success.html',{
                "withdraw_amount":withdraw_amount,
                "existed_amount":existed_amount,
                "bank":bank
            })
    else:
        withdrawalForm()       
    return render(request,'withdraw.html',{"form":form,"msg":msg})
def withdraw_success(request):
    return render(request,'withdrwa_success.html')

def transfer(request):
    msg=""
    source = Banking.objects.all()
    form = transferForm()
    if request.method=="POST":
        form = transferForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            account_no=cd['account_no']
            name=cd['name']
            password=cd['password']
            target_account_no=cd['target_account_no']
            amount= cd['amount']
            try:
                source=Banking.objects.get(
                    account_no=account_no,
                    name=name,
                    password=password
                )
            except Banking.DoesNotExist:
                msg="Invalid Account Number or Password"
                return render(request,'transfer.html',{
                    "form":form,
                    "msg":msg,
              })  
            try:
                target=Banking.objects.get(account_no=target_account_no)
            except Banking.DoesNotExist:
                msg = "Target Account Does not exist"
                return render(request,'transfer.html',{"form":form,"msg":msg})
            if source.amount < amount:
                msg = "Insufficient balance"
                return render(request, "transfer.html", {"form": form, "msg": msg})
            before_source = source.amount
            before_target = target.amount

            source.amount = before_source - amount
            target.amount = before_target + amount

            source.save()
            target.save()

            return render(request,'transfer_success.html',{
                    "target_deposit_amount":amount,
                    "target_existed_amount":before_target,
                    "existed_amount":before_source,
                    "after_transfer_balance":source.amount,
                    "target_balance":target.amount
                })
    else:
        form = transferForm()        
    return render(request,'transfer.html',{"form":form})

def close_account(request):
    msg=""
    source = Banking.objects.all()
    form = closeAccountForm()
    if request.method=="POST":
        form = closeAccountForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            account_no=cd['account_no']
            name=cd['name']
            password=cd['password']
            
            try:
                bank=Banking.objects.get(
                    account_no=account_no,
                    name=name,
                    password=password
                )
            except Banking.DoesNotExist:
                msg="Invalid Account Number or Password"
                return render(request,'close_account.html',{
                    "form":form,
                    "msg":msg,
              })  
            closing_balance = bank.amount
            bank.delete()
            return render(request,'close_account_success.html',{
                "account_no":account_no,
                "name":name,
                "closing_balance":closing_balance
            })
    else:
        form = closeAccountForm()    
    return render(request,'close_account.html',{"form":form,"msg":msg})

def about_us(request):
    return render(request,'about_us.html')




