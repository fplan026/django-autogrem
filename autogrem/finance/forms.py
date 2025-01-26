from django import forms
from .models import RecurringBill

class NewBill(forms.ModelForm):
    
    class Meta:
        model = RecurringBill
        fields = ['name', 'amount', 'start_date', 'is_indefinate', 'end_date',
                  'duration', 'duration_unit', ]