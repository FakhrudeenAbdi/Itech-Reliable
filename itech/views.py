from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.db.models import Sum, Q
from . import forms, models

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'itech/index.html')

# For showing signup/login button for customers
def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'itech/customerclick.html')

# For showing signup/login button for technicians
def techniciansclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'itech/techniciansclick.html')

# For showing signup/login button for ADMIN
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.urls import reverse
from . import forms

def customer_signup_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save(commit=False)
            user.set_password(userForm.cleaned_data['password'])
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
            return HttpResponseRedirect(reverse('customerlogin'))
        else:
            # Print errors for debugging
            print("User form errors: ", userForm.errors)
            print("Customer form errors: ", customerForm.errors)
            mydict['userForm'] = userForm
            mydict['customerForm'] = customerForm
    
    return render(request, 'itech/customersignup.html', context=mydict)


def technician_signup_view(request):
    userForm = forms.TechnicianUserForm()
    technicianForm = forms.TechnicianForm()
    mydict = {'userForm': userForm, 'technicianForm': technicianForm}
    
    if request.method == 'POST':
        userForm = forms.TechnicianUserForm(request.POST)
        technicianForm = forms.TechnicianForm(request.POST, request.FILES)
        
        if userForm.is_valid() and technicianForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            technician = technicianForm.save(commit=False)
            technician.user = user
            technician.save()
            my_technician_group = Group.objects.get_or_create(name='TECHNICIAN')
            my_technician_group[0].user_set.add(user)
            return HttpResponseRedirect('technicianlogin')
    
    return render(request, 'itech/techniciansignup.html', context=mydict)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

def is_technician(user):
    return user.groups.filter(name='TECHNICIAN').exists()

def afterlogin_view(request):
    if is_customer(request.user):
        return redirect('customer-dashboard')
    elif is_technician(request.user):
        accountapproval = models.Technician.objects.filter(user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('technician-dashboard')
        else:
            return render(request, 'itech/technician_wait_for_approval.html')
    else:
        return redirect('admin-dashboard')

# ADMIN RELATED views start
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    enquiries = models.SupportTicket.objects.all().order_by('-id')
    customers = []
    for enq in enquiries:
        customer = models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    
    dict = {
        'total_customer': models.Customer.objects.count(),
        'total_technician': models.Technician.objects.count(),
        'total_request': models.SupportTicket.objects.count(),
        'total_feedback': models.Feedback.objects.count(),
        'data': zip(customers, enquiries),
    }
    return render(request, 'itech/admin_dashboard.html', context=dict)

@login_required(login_url='adminlogin')
def admin_customer_view(request):
    return render(request, 'itech/admin_customer.html')

@login_required(login_url='adminlogin')
def admin_view_customer_view(request):
    customers = models.Customer.objects.all()
    return render(request, 'itech/admin_view_customer.html', {'customers': customers})

@login_required(login_url='adminlogin')
def delete_customer_view(request, pk):
    customer = models.Customer.objects.get(id=pk)
    user = models.User.objects.get(id=customer.user_id)
    user.delete()
    customer.delete()
    return redirect('admin-view-customer')

@login_required(login_url='adminlogin')
def update_customer_view(request, pk):
    customer = models.Customer.objects.get(id=pk)
    user = models.User.objects.get(id=customer.user_id)
    userForm = forms.CustomerUserForm(instance=user)
    customerForm = forms.CustomerForm(request.FILES, instance=customer)
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST, instance=user)
        customerForm = forms.CustomerForm(request.POST, request.FILES, instance=customer)
        
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customerForm.save()
            return redirect('admin-view-customer')
    
    return render(request, 'itech/update_customer.html', context=mydict)

@login_required(login_url='adminlogin')
def admin_add_customer_view(request):
    userForm = forms.CustomerUserForm()
    customerForm = forms.CustomerForm()
    mydict = {'userForm': userForm, 'customerForm': customerForm}
    
    if request.method == 'POST':
        userForm = forms.CustomerUserForm(request.POST)
        customerForm = forms.CustomerForm(request.POST, request.FILES)
        
        if userForm.is_valid() and customerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            customer = customerForm.save(commit=False)
            customer.user = user
            customer.save()
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
            return HttpResponseRedirect('/admin-view-customer')
    
    return render(request, 'itech/admin_add_customer.html', context=mydict)

@login_required(login_url='adminlogin')
def admin_view_customer_enquiry_view(request):
    enquiries = models.SupportTicket.objects.all().order_by('-id')
    customers = []
    for enq in enquiries:
        customer = models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    
    return render(request, 'itech/admin_view_customer_enquiry.html', {'data': zip(customers, enquiries)})

@login_required(login_url='adminlogin')
def admin_view_customer_invoice_view(request):
    enquiries = models.SupportTicket.objects.values('customer_id').annotate(Sum('cost'))
    customers = []
    for enq in enquiries:
        customer = models.Customer.objects.get(id=enq['customer_id'])
        customers.append(customer)
    
    return render(request, 'itech/admin_view_customer_invoice.html', {'data': zip(customers, enquiries)})

@login_required(login_url='adminlogin')
def admin_technician_view(request):
    return render(request, 'itech/admin_technician.html')

@login_required(login_url='adminlogin')
def admin_approve_technician_view(request):
    technicians = models.Technician.objects.filter(status=False)
    return render(request, 'itech/admin_approve_technician.html', {'technicians': technicians})

@login_required(login_url='adminlogin')
def approve_technician_view(request, pk):
    technicianSalary = forms.MechanicSalaryForm()
    if request.method == 'POST':
        technicianSalary = forms.MechanicSalaryForm(request.POST)
        if technicianSalary.is_valid():
            technician = models.Technician.objects.get(id=pk)
            technician.salary = technicianSalary.cleaned_data['salary']
            technician.status = True
            technician.save()
            return HttpResponseRedirect('/admin-approve-technician')
    
    return render(request, 'itech/admin_approve_technician_details.html', {'technicianSalary': technicianSalary})

@login_required(login_url='adminlogin')
def delete_technician_view(request, pk):
    technician = models.Technician.objects.get(id=pk)
    user = models.User.objects.get(id=technician.user_id)
    user.delete()
    technician.delete()
    return redirect('admin-approve-technician')

@login_required(login_url='adminlogin')
def admin_add_technician_view(request):
    userForm = forms.TechnicianUserForm()
    technicianForm = forms.TechnicianForm()
    technicianSalary = forms.TechnicianForm()
    mydict = {'userForm': userForm, 'technicianForm': technicianForm, 'technicianSalary': technicianSalary}
    
    if request.method == 'POST':
        userForm = forms.TechnicianUserForm(request.POST)
        technicianForm = forms.TechnicianForm(request.POST, request.FILES)
        technicianSalary = forms.MechanicSalaryForm(request.POST)
        
        if userForm.is_valid() and technicianForm.is_valid() and technicianSalary.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            technician = technicianForm.save(commit=False)
            technician.user = user
            technician.status = True
            technician.salary = technicianSalary.cleaned_data['salary']
            technician.save()
            my_technician_group = Group.objects.get_or_create(name='TECHNICIAN')
            my_technician_group[0].user_set.add(user)
            return HttpResponseRedirect('admin-view-technician')
    
    return render(request, 'itech/admin_add_technician.html', context=mydict)

@login_required(login_url='adminlogin')
def admin_view_technician_view(request):
    technicians = models.Technician.objects.all()
    return render(request, 'itech/admin_view_technician.html', {'technicians': technicians})

@login_required(login_url='adminlogin')
def update_technician_view(request, pk):
    technician = models.Technician.objects.get(id=pk)
    user = models.User.objects.get(id=technician.user_id)
    userForm = forms.TechnicianUserForm(instance=user)
    technicianForm = forms.TechnicianForm(request.FILES, instance=technician)
    mydict = {'userForm': userForm, 'technicianForm': technicianForm}
    
    if request.method == 'POST':
        userForm = forms.TechnicianUserForm(request.POST, instance=user)
        technicianForm = forms.TechnicianForm(request.POST, request.FILES, instance=technician)
        
        if userForm.is_valid() and technicianForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            technicianForm.save()
            return redirect('admin-view-technician')
    
    return render(request, 'itech/update_technician.html', context=mydict)

@login_required(login_url='adminlogin')
def admin_view_technician_salary_view(request):
    technicians = models.Technician.objects.all()
    return render(request, 'itech/admin_view_technician_salary.html', {'technicians': technicians})

@login_required(login_url='adminlogin')
def update_salary_view(request, pk):
    technicianSalary = forms.MechanicSalaryForm()
    if request.method == 'POST':
        technicianSalary = forms.MechanicSalaryForm(request.POST)
        if technicianSalary.is_valid():
            technician = models.Technician.objects.get(id=pk)
            technician.salary = technicianSalary.cleaned_data['salary']
            technician.save()
            return HttpResponseRedirect('/admin-view-technician-salary')
    
    return render(request, 'itech/admin_approve_technician_details.html', {'technicianSalary': technicianSalary})

@login_required(login_url='adminlogin')
def admin_request_view(request):
    return render(request, 'itech/admin_request.html')

@login_required(login_url='adminlogin')
def admin_view_request_view(request):
    enquiries = models.SupportTicket.objects.all().order_by('-id')
    customers = []
    for enq in enquiries:
        customer = models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    
    return render(request, 'itech/admin_view_request.html', {'data': zip(customers, enquiries)})

@login_required(login_url='adminlogin')
def change_status_view(request, pk):
    adminenquiry = forms.AdminApproveRequestForm()
    if request.method == 'POST':
        adminenquiry = forms.AdminApproveRequestForm(request.POST)
        if adminenquiry.is_valid():
            enquiry_x = models.SupportTicket.objects.get(id=pk)
            enquiry_x.mechanic = adminenquiry.cleaned_data['mechanic']
            enquiry_x.cost = adminenquiry.cleaned_data['cost']
            enquiry_x.status = adminenquiry.cleaned_data['status']
            enquiry_x.save()
            return HttpResponseRedirect('/admin-view-request')
    
    return render(request, 'itech/admin_approve_request_details.html', {'adminenquiry': adminenquiry})

@login_required(login_url='adminlogin')
def admin_delete_request_view(request, pk):
    request_obj = models.SupportTicket.objects.get(id=pk)
    request_obj.delete()
    return redirect('admin-view-request')

@login_required(login_url='adminlogin')
def admin_add_request_view(request):
    enquiry = forms.AdminRequestForm()
    adminenquiry = forms.AdminRequestForm()
    mydict = {'enquiry': enquiry, 'adminenquiry': adminenquiry}
    
    if request.method == 'POST':
        enquiry = forms.AdminRequestForm(request.POST)
        adminenquiry = forms.AdminRequestForm(request.POST)
        
        if enquiry.is_valid() and adminenquiry.is_valid():
            enquiry_x = enquiry.save(commit=False)
            enquiry_x.customer = adminenquiry.cleaned_data['customer']
            enquiry_x.mechanic = adminenquiry.cleaned_data['mechanic']
            enquiry_x.cost = adminenquiry.cleaned_data['cost']
            enquiry_x.status = 'Approved'
            enquiry_x.save()
            return HttpResponseRedirect('admin-view-request')
    
    return render(request, 'itech/admin_add_request.html', context=mydict)

@login_required(login_url='adminlogin')
def admin_approve_request_view(request):
    enquiries = models.SupportTicket.objects.filter(status='Pending')
    return render(request, 'itech/admin_approve_request.html', {'enquiries': enquiries})

@login_required(login_url='adminlogin')
def approve_request_view(request, pk):
    adminenquiry = forms.AdminApproveRequestForm()
    if request.method == 'POST':
        adminenquiry = forms.AdminApproveRequestForm(request.POST)
        if adminenquiry.is_valid():
            enquiry_x = models.SupportTicket.objects.get(id=pk)
            enquiry_x.mechanic = adminenquiry.cleaned_data['mechanic']
            enquiry_x.cost = adminenquiry.cleaned_data['cost']
            enquiry_x.status = adminenquiry.cleaned_data['status']
            enquiry_x.save()
            return HttpResponseRedirect('/admin-approve-request')
    
    return render(request, 'itech/admin_approve_request_details.html', {'adminenquiry': adminenquiry})

@login_required(login_url='adminlogin')
def admin_view_service_cost_view(request):
    enquiries = models.SupportTicket.objects.all().order_by('-id')
    customers = []
    for enq in enquiries:
        customer = models.Customer.objects.get(id=enq.customer_id)
        customers.append(customer)
    
    return render(request, 'itech/admin_view_service_cost.html', {'data': zip(customers, enquiries)})

@login_required(login_url='adminlogin')
def update_cost_view(request, pk):
    updateCostForm = forms.UpdateCostForm()
    if request.method == 'POST':
        updateCostForm = forms.UpdateCostForm(request.POST)
        if updateCostForm.is_valid():
            enquiry_x = models.SupportTicket.objects.get(id=pk)
            enquiry_x.cost = updateCostForm.cleaned_data['cost']
            enquiry_x.save()
            return HttpResponseRedirect('/admin-view-service-cost')
    
    return render(request, 'itech/update_cost.html', {'updateCostForm': updateCostForm})

@login_required(login_url='adminlogin')
def admin_technician_attendance_view(request):
    return render(request, 'itech/admin_technician_attendance.html')

@login_required(login_url='adminlogin')
def admin_take_attendance_view(request):
    technicians = models.Technician.objects.filter(status=True)
    aform = forms.AttendanceForm()
    
    if request.method == 'POST':
        form = forms.AttendanceForm(request.POST)
        if form.is_valid():
            Attendances = request.POST.getlist('present_status')
            date = form.cleaned_data['date']
            for i in range(len(Attendances)):
                AttendanceModel = models.Attendance()
                AttendanceModel.date = date
                AttendanceModel.present_status = Attendances[i]
                technician = models.Technician.objects.get(id=int(technicians[i].id))
                AttendanceModel.technician = technician
                AttendanceModel.save()
            return redirect('admin-view-attendance')
    
    return render(request, 'itech/admin_take_attendance.html', {'technicians': technicians, 'aform': aform})

@login_required(login_url='adminlogin')
def admin_view_attendance_view(request):
    form = forms.AskDateForm()
    if request.method == 'POST':
        form = forms.AskDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            attendancedata = models.Attendance.objects.filter(date=date)
            techniciandata = models.Technician.objects.filter(status=True)
            mylist = zip(attendancedata, techniciandata)
            return render(request, 'itech/admin_view_attendance_page.html', {'mylist': mylist, 'date': date})
    
    return render(request, 'itech/admin_view_attendance_ask_date.html', {'form': form})

@login_required(login_url='adminlogin')
def admin_report_view(request):
    reports = models.SupportTicket.objects.filter(Q(status="Repairing Done") | Q(status="Released"))
    dict = {'reports': reports}
    return render(request, 'itech/admin_report.html', context=dict)

@login_required(login_url='adminlogin')
def admin_feedback_view(request):
    feedback = models.Feedback.objects.all().order_by('-id')
    return render(request, 'itech/admin_feedback.html', {'feedback': feedback})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Sum
from . import models, forms

# CUSTOMER RELATED views start
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q, Sum
from . import models
from . import forms
from .forms import SupportTicketForm, SubscriptionForm
from .models import InternetPlan, Subscription, Usage, BillingHistory, SupportTicket

# Function to check if the user is a customer
def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

# CUSTOMER RELATED views start
@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_dashboard_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    work_in_progress = models.SupportTicket.objects.filter(customer_id=customer.id, status='Repairing').count()
    work_completed = models.SupportTicket.objects.filter(customer_id=customer.id).filter(Q(status="Repairing Done") | Q(status="Released")).count()
    new_request_made = models.Request.objects.filter(customer_id=customer.id).filter(Q(status="Pending") | Q(status="Approved")).count()
    
    # Calculate the total bill
    bill = models.SupportTicket.objects.filter(customer_id=customer.id, status__in=['Repairing Done', 'Released']).aggregate(total_bill=Sum('cost'))['total_bill']
    if bill is None:
        bill = 0
    
    return render(request, 'itech/customer_dashboard.html', {
        'work_in_progress': work_in_progress,
        'work_completed': work_completed,
        'new_request_made': new_request_made,
        'bill': bill
    })

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_add_request_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    request_form = forms.RequestForm()
    
    if request.method == 'POST':
        request_form = forms.RequestForm(request.POST)
        if request_form.is_valid():
            request_instance = request_form.save(commit=False)
            request_instance.customer = customer
            request_instance.status = 'Pending'
            request_instance.save()
            return redirect('customer-view-request')  # Ensure this URL matches your URL configuration
    
    return render(request, 'itech/customer_add_request.html', {'request_form': request_form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    return render(request, 'itech/customer_profile.html', {'customer': customer})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_customer_profile_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    user = request.user
    user_form = forms.CustomerUserForm(instance=user)
    customer_form = forms.CustomerForm(instance=customer)
    
    if request.method == 'POST':
        user_form = forms.CustomerUserForm(request.POST, instance=user)
        customer_form = forms.CustomerForm(request.POST, request.FILES, instance=customer)
        
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            return redirect('customer-profile')  # Ensure this URL matches your URL configuration
    
    return render(request, 'itech/edit_customer_profile.html', {'user_form': user_form, 'customer_form': customer_form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_feedback_view(request):
    feedback_form = forms.FeedbackForm()
    
    if request.method == 'POST':
        feedback_form = forms.FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance = feedback_form.save(commit=False)
            feedback_instance.by = request.user.username
            feedback_instance.save()
            return redirect('customer-dashboard')  # Ensure this URL matches your URL configuration
    
    return render(request, 'itech/customer_feedback.html', {'feedback_form': feedback_form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_invoice_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    invoices = models.SupportTicket.objects.filter(customer_id=customer.id).filter(Q(status="Repairing Done") | Q(status="Released"))
    return render(request, 'itech/customer_invoice.html', {'invoices': invoices})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_approved_request_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    approved_requests = models.Request.objects.filter(customer_id=customer.id, status="Approved")
    return render(request, 'itech/customer_view_approved_request.html', {'approved_requests': approved_requests})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_delete_request_view(request, pk):
    request_instance = models.SupportTicket.objects.get(id=pk)
    request_instance.delete()
    return redirect('customer-view-request')  # Ensure this URL matches your URL configuration

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_approved_request_invoice_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    approved_requests = models.SupportTicket.objects.filter(customer_id=customer.id, status="Approved")
    return render(request, 'itech/customer_view_approved_request_invoice.html', {'approved_requests': approved_requests})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def raise_ticket_view(request):
    if request.method == 'POST':
        form = SupportTicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.customer = models.Customer.objects.get(user=request.user)
            ticket.save()
            return redirect('customer-view-request')  # Redirect to a page where user can view their tickets
    else:
        form = SupportTicketForm()
    return render(request, 'itech/raise_ticket.html', {'form': form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def browse_plans(request):
    plans = InternetPlan.objects.all()
    return render(request, 'itech/plans.html', {'plans': plans})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def manage_subscription(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.customer = customer
            subscription.save()
            return redirect('subscription-details')
    else:
        form = SubscriptionForm()
    return render(request, 'itech/subscribe_plan.html', {'form': form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def subscription_details(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    subscription = Subscription.objects.filter(customer=customer).first()
    return render(request, 'itech/subscription_details.html', {'subscription': subscription})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def track_usage(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    usage = Usage.objects.filter(customer=customer)
    billing_history = BillingHistory.objects.filter(customer=customer)
    return render(request, 'itech/usage_details.html', {'usage': usage, 'billing_history': billing_history})

# TECHNICIAN RELATED views start
@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_dashboard_view(request):
    technician = models.Technician.objects.get(user_id=request.user.id)
    assigned_requests = models.SupportTicket.objects.filter(mechanic=technician)
    return render(request, 'itech/technician_dashboard.html', {'assigned_requests': assigned_requests})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_work_assigned_view(request):
    technician = models.Technician.objects.get(user_id=request.user.id)
    assigned_requests = models.SupportTicket.objects.filter(mechanic=technician)
    return render(request, 'itech/technician_work_assigned.html', {'assigned_requests': assigned_requests})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_update_status_view(request, pk):
    request_instance = models.SupportTicket.objects.get(id=pk)
    status_form = forms.MechanicUpdateStatusForm()
    
    if request.method == 'POST':
        status_form = forms.MechanicUpdateStatusForm(request.POST)
        if status_form.is_valid():
            request_instance.status = status_form.cleaned_data['status']
            request_instance.save()
            return redirect('technician-dashboard')
    
    return render(request, 'itech/technician_update_status.html', {'request_instance': request_instance, 'status_form': status_form})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_feedback_view(request):
    feedback_form = forms.FeedbackForm()
    
    if request.method == 'POST':
        feedback_form = forms.FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance = feedback_form.save(commit=False)
            feedback_instance.by = request.user.username
            feedback_instance.save()
            return redirect('technician-dashboard')
    
    return render(request, 'itech/technician_feedback.html', {'feedback_form': feedback_form})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_salary_view(request):
    technician = models.Technician.objects.get(user_id=request.user.id)
    return render(request, 'itech/technician_salary.html', {'technician': technician})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_profile_view(request):
    technician = models.Technician.objects.get(user_id=request.user.id)
    return render(request, 'itech/technician_profile.html', {'technician': technician})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def edit_technician_profile_view(request):
    technician = models.Technician.objects.get(user_id=request.user.id)
    user = request.user
    user_form = forms.TechnicianUserForm(instance=user)
    technician_form = forms.TechnicianForm(instance=technician)
    
    if request.method == 'POST':
        user_form = forms.TechnicianUserForm(request.POST, instance=user)
        technician_form = forms.TechnicianForm(request.POST, request.FILES, instance=technician)
        
        if user_form.is_valid() and technician_form.is_valid():
            user_form.save()
            technician_form.save()
            return redirect('technician-profile')
    
    return render(request, 'itech/edit_technician_profile.html', {'user_form': user_form, 'technician_form': technician_form})

# Additional views can be added here as needed
@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_dashboard_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    subscriptions = models.Subscription.objects.filter(customer_id=customer.id)
    support_tickets = models.SupportTicket.objects.filter(customer_id=customer.id)

    mydict = {
        'subscriptions': subscriptions,
        'support_tickets': support_tickets,
    }
    return render(request, 'itech/customer_dashboard.html', context=mydict)

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'itech/customer_request.html',{'customer':customer})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_add_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    request_form=forms.AdminRequestForm()
    if request.method=='POST':
        request_form=forms.RequestForm(request.POST)
        if request_form.is_valid():
            request_instance=request_form.save(commit=False)
            request_instance.customer=customer
            request_instance.status='Pending'
            request_instance.save()
            return redirect('customer-view-request')
    return render(request,'itech/customer_add_request.html',{'request_form':request_form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    requests=models.SupportTicket.objects.all().filter(customer_id=customer.id)
    return render(request,'itech/customer_view_request.html',{'requests':requests})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_delete_request_view(request,pk):
    request=models.SupportTicket.objects.get(id=pk)
    request.delete()
    return redirect('customer-view-request')

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_approved_request_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    approved_requests=models.Request.objects.filter(customer_id=customer.id,status="Approved")
    return render(request,'itech/customer_view_approved_request.html',{'approved_requests':approved_requests})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    return render(request,'itech/customer_profile.html',{'customer':customer})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def edit_customer_profile_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    user=request.user
    userForm=forms.CustomerUserForm(instance=user)
    customerForm=forms.CustomerForm(instance=customer)
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        userForm=forms.CustomerUserForm(request.POST,instance=user)
        customerForm=forms.CustomerForm(request.POST,request.FILES,instance=customer)
        if userForm.is_valid() and customerForm.is_valid():
            user=userForm.save()
            customerForm.save()
            return redirect('customer-profile')
    return render(request,'itech/edit_customer_profile.html',context=mydict)

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_feedback_view(request):
    feedback_form=forms.FeedbackForm()
    if request.method=='POST':
        feedback_form=forms.FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance=feedback_form.save(commit=False)
            feedback_instance.by=request.user.username
            feedback_instance.save()
            return redirect('customer-dashboard')
    return render(request,'itech/customer_feedback.html',{'feedback_form':feedback_form})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_invoice_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    invoices=models.SupportTicket.objects.filter(customer_id=customer.id).filter(Q(status="Repairing Done") | Q(status="Released"))
    return render(request,'itech/customer_invoice.html',{'invoices':invoices})

@login_required(login_url='customerlogin')
@user_passes_test(is_customer)
def customer_view_approved_request_invoice_view(request):
    customer=models.Customer.objects.get(user_id=request.user.id)
    approved_requests=models.Request.objects.filter(customer_id=customer.id,status="Approved")
    return render(request,'itech/customer_view_approved_request_invoice.html',{'approved_requests':approved_requests})

# TECHNICIAN RELATED views start
@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_dashboard_view(request):
    technician=models.Technician.objects.get(user_id=request.user.id)
    assigned_requests=models.SupportTicket.objects.filter(mechanic=technician)
    return render(request,'itech/technician_dashboard.html',{'assigned_requests':assigned_requests})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_work_assigned_view(request):
    technician=models.Technician.objects.get(user_id=request.user.id)
    assigned_requests=models.SupportTicket.objects.filter(mechanic=technician)
    return render(request,'itech/technician_work_assigned.html',{'assigned_requests':assigned_requests})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_update_status_view(request,pk):
    request_instance=models.SupportTicket.objects.get(id=pk)
    status_form=forms.MechanicUpdateStatusForm()
    if request.method=='POST':
        status_form=forms.MechanicUpdateStatusForm(request.POST)
        if status_form.is_valid():
            request_instance.status=status_form.cleaned_data['status']
            request_instance.save()
            return redirect('technician-dashboard')
    return render(request,'itech/technician_update_status.html',{'request_instance':request_instance,'status_form':status_form})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_feedback_view(request):
    feedback_form=forms.FeedbackForm()
    if request.method=='POST':
        feedback_form=forms.FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance=feedback_form.save(commit=False)
            feedback_instance.by=request.user.username
            feedback_instance.save()
            return redirect('technician-dashboard')
    return render(request,'itech/technician_feedback.html',{'feedback_form':feedback_form})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_salary_view(request):
    technician=models.Technician.objects.get(user_id=request.user.id)
    return render(request,'itech/technician_salary.html',{'technician':technician})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def technician_profile_view(request):
    technician=models.Technician.objects.get(user_id=request.user.id)
    return render(request,'itech/technician_profile.html',{'technician':technician})

@login_required(login_url='technicianlogin')
@user_passes_test(is_technician)
def edit_technician_profile_view(request):
    technician=models.Technician.objects.get(user_id=request.user.id)
    user=request.user
    userForm=forms.TechnicianUserForm(instance=user)
    technicianForm=forms.TechnicianForm(instance=technician)
    mydict={'userForm':userForm,'technicianForm':technicianForm}
    if request.method=='POST':
        userForm=forms.TechnicianUserForm(request.POST,instance=user)
        technicianForm=forms.TechnicianForm(request.POST,request.FILES,instance=technician)
        if userForm.is_valid() and technicianForm.is_valid():
            user=userForm.save()
            technicianForm.save()
            return redirect('technician-profile')
    return render(request,'itech/edit_technician_profile.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_technician_attendance_view(request):
    return render(request,'itech/admin_technician_attendance.html')

@login_required(login_url='adminlogin')
def admin_take_attendance_view(request):
    technicians=models.Technician.objects.filter(status=True)
    aform=forms.AttendanceForm()
    if request.method=='POST':
        form=forms.AttendanceForm(request.POST)
        if form.is_valid():
            Attendances=request.POST.getlist('present_status')
            date=form.cleaned_data['date']
            for i in range(len(Attendances)):
                AttendanceModel=models.Attendance()
                AttendanceModel.date=date
                AttendanceModel.present_status=Attendances[i]
                technician=models.Technician.objects.get(id=int(technicians[i].id))
                AttendanceModel.technician=technician
                AttendanceModel.save()
            return redirect('admin-view-attendance')
    return render(request,'itech/admin_take_attendance.html',{'technicians':technicians,'aform':aform})

@login_required(login_url='adminlogin')
def admin_view_attendance_view(request):
    form=forms.AskDateForm()
    if request.method=='POST':
        form=forms.AskDateForm(request.POST)
        if form.is_valid():
            date=form.cleaned_data['date']
            attendancedata=models.Attendance.objects.filter(date=date)
            techniciandata=models.Technician.objects.filter(status=True)
            mylist=zip(attendancedata,techniciandata)
            return render(request,'itech/admin_view_attendance_page.html',{'mylist':mylist,'date':date})
    return render(request,'itech/admin_view_attendance_ask_date.html',{'form':form})

@login_required(login_url='adminlogin')
def admin_report_view(request):
    reports=models.SupportTicket.objects.filter(Q(status="Repairing Done") | Q(status="Released"))
    dict={'reports':reports}
    return render(request,'itech/admin_report.html',context=dict)

@login_required(login_url='adminlogin')
def admin_feedback_view(request):
    feedback=models.Feedback.objects.all().order_by('-id')
    return render(request,'itech/admin_feedback.html',{'feedback':feedback})

from django.core.mail import send_mail

def aboutus_view(request):
    return render(request,'itech/aboutus.html')
from django.conf import settings 
def contactus_view(request):
    sub = forms.ContactUsForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'itech/contactussuccess.html')
    return render(request, 'itech/contactus.html', {'form':sub})
