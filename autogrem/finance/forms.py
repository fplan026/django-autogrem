from django import forms
from .models import Bill

class NewBill(forms.ModelForm):
    
    class Meta:
        model = Bill
        fields = ['name', 'amount', 'start_date', 'is_indefinate', 'end_date',
                  'duration', 'duration_unit', ]