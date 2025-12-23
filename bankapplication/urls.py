
from django.contrib import admin
from django.urls import path
from bankapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_account/',views.new_account,name='new_accountv'),
    path('home/',views.home,name='homev'),
    path('balance/',views.balance,name='balancev'),
    path('balance_success/',views.balance_success,name='balance_successv'),
    path('deposit/',views.deposit,name='depositv'),
    path('deposit_success/',views.deposit_success,name='deposit_successv'),
    path('withdraw/',views.withdraw,name='withdrawv'),
    path('withdraw_success/',views.withdraw_success,name='withdraw_successv'),
    path('transfer/',views.transfer,name='transferv'),
    path('close_account/',views.close_account,name='close_accountv'),
    path('about_us/',views.about_us,name='about_usv'),
]
