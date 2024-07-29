from django import forms
from django.contrib.auth.models import User
from . import models

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = ['address', 'phone_number', 'profile_pic']

class TechnicianUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

class TechnicianForm(forms.ModelForm):
    class Meta:
        model = models.Technician
        fields = ['address', 'phone_number', 'profile_pic', 'skill']

class InternetPlanForm(forms.ModelForm):
    class Meta:
        model = models.InternetPlan
        fields = ['name', 'description', 'speed', 'price']

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = models.Subscription
        fields = ['plan', 'start_date', 'end_date']

class SupportTicketForm(forms.ModelForm):
    class Meta:
        model = models.SupportTicket
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

class AdminRequestForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=models.Customer.objects.all(), empty_label="Customer Name", to_field_name='id')
    technician = forms.ModelChoiceField(queryset=models.Technician.objects.all(), empty_label="Technician Name", to_field_name='id')
    cost = forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    technician = forms.ModelChoiceField(queryset=models.Technician.objects.all(), empty_label="Technician Name", to_field_name='id')
    cost = forms.IntegerField()
    status_choices = (('Pending', 'Pending'), ('Approved', 'Approved'), ('Completed', 'Completed'))
    status = forms.ChoiceField(choices=status_choices)

class UpdateCostForm(forms.Form):
    cost = forms.IntegerField()

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

# For Attendance related form
presence_choices = (('Present', 'Present'), ('Absent', 'Absent'))
class AttendanceForm(forms.Form):
    present_status = forms.ChoiceField(choices=presence_choices)
    date = forms.DateField()

class AskDateForm(forms.Form):
    date = forms.DateField()

# For contact us page
class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
