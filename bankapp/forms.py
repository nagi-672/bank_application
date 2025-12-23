from django import forms
from bankapp.models import Banking

class bankForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Banking
        fields=['account_no','name','password','amount','address','mob_no']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password!= confirm_password:
            raise forms.ValidationError("Password and confirm passsword do not match")
        return cleaned_data

class balanceForm(forms.ModelForm):
    password= forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = Banking
        fields = ['account_no','name','password']

class depositForm(forms.Form):
    account_no = forms.IntegerField()
    name = forms.CharField(max_length=40)
    password= forms.CharField(widget = forms.PasswordInput)
    amount = forms.FloatField()
    

class withdrawalForm(forms.Form):
    account_no = forms.IntegerField()
    name = forms.CharField(max_length=40)
    password= forms.CharField(widget = forms.PasswordInput)
    amount = forms.FloatField()
    

class transferForm(forms.Form): 
    account_no = forms.IntegerField()
    name= forms.CharField(max_length=40)
    password = forms.CharField(widget = forms.PasswordInput)
    target_account_no = forms.IntegerField(label="Target account No")
    amount = forms.FloatField()

class closeAccountForm(forms.Form):
    account_no = forms.IntegerField()
    name = forms.CharField(max_length=40)
    password= forms.CharField(widget=forms.PasswordInput)
    
    

