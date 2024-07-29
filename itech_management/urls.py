from django.contrib import admin
from django.urls import path
from itech import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='home'),

    path('adminclick/', views.adminclick_view, name='adminclick'),
    path('customerclick/', views.customerclick_view, name='customerclick'),
    path('techniciansclick/', views.techniciansclick_view, name='techniciansclick'),

    path('customersignup/', views.customer_signup_view, name='customersignup'),
    path('techniciansignup/', views.technician_signup_view, name='techniciansignup'),

    path('customerlogin/', LoginView.as_view(template_name='itech/customerlogin.html'), name='customerlogin'),
    path('technicianlogin/', LoginView.as_view(template_name='itech/technicianlogin.html'), name='technicianlogin'),
    path('adminlogin/', LoginView.as_view(template_name='itech/adminlogin.html'), name='adminlogin'),

    path('admin-dashboard/', views.admin_dashboard_view, name='admin-dashboard'),

    path('admin-customer/', views.admin_customer_view, name='admin-customer'),
    path('admin-view-customer/', views.admin_view_customer_view, name='admin-view-customer'),
    path('delete-customer/<int:pk>/', views.delete_customer_view, name='delete-customer'),
    path('update-customer/<int:pk>/', views.update_customer_view, name='update-customer'),
    path('admin-add-customer/', views.admin_add_customer_view, name='admin-add-customer'),
    path('admin-view-customer-enquiry/', views.admin_view_customer_enquiry_view, name='admin-view-customer-enquiry'),
    path('admin-view-customer-invoice/', views.admin_view_customer_invoice_view, name='admin-view-customer-invoice'),

    path('admin-request/', views.admin_request_view, name='admin-request'),
    path('admin-view-request/', views.admin_view_request_view, name='admin-view-request'),
    path('change-status/<int:pk>/', views.change_status_view, name='change-status'),
    path('admin-delete-request/<int:pk>/', views.admin_delete_request_view, name='admin-delete-request'),
    path('admin-add-request/', views.admin_add_request_view, name='admin-add-request'),
    path('admin-approve-request/', views.admin_approve_request_view, name='admin-approve-request'),
    path('approve-request/<int:pk>/', views.approve_request_view, name='approve-request'),
    
    path('admin-view-service-cost/', views.admin_view_service_cost_view, name='admin-view-service-cost'),
    path('update-cost/<int:pk>/', views.update_cost_view, name='update-cost'),

    path('admin-technician/', views.admin_technician_view, name='admin-technician'),
    path('admin-view-technician/', views.admin_view_technician_view, name='admin-view-technician'),
    path('delete-technician/<int:pk>/', views.delete_technician_view, name='delete-technician'),
    path('update-technician/<int:pk>/', views.update_technician_view, name='update-technician'),
    path('admin-add-technician/', views.admin_add_technician_view, name='admin-add-technician'),
    path('admin-approve-technician/', views.admin_approve_technician_view, name='admin-approve-technician'),
    path('approve-technician/<int:pk>/', views.approve_technician_view, name='approve-technician'),
    path('admin-view-technician-salary/', views.admin_view_technician_salary_view, name='admin-view-technician-salary'),
    path('update-salary/<int:pk>/', views.update_salary_view, name='update-salary'),

    path('admin-technician-attendance/', views.admin_technician_attendance_view, name='admin-technician-attendance'),
    path('admin-take-attendance/', views.admin_take_attendance_view, name='admin-take-attendance'),
    path('admin-view-attendance/', views.admin_view_attendance_view, name='admin-view-attendance'),
    path('admin-feedback/', views.admin_feedback_view, name='admin-feedback'),

    path('admin-report/', views.admin_report_view, name='admin-report'),

    path('technician-dashboard/', views.technician_dashboard_view, name='technician-dashboard'),
    path('technician-work-assigned/', views.technician_work_assigned_view, name='technician-work-assigned'),
    path('technician-update-status/<int:pk>/', views.technician_update_status_view, name='technician-update-status'),
    path('technician-feedback/', views.technician_feedback_view, name='technician-feedback'),
    path('technician-salary/', views.technician_salary_view, name='technician-salary'),
    path('technician-profile/', views.technician_profile_view, name='technician-profile'),
    path('edit-technician-profile/', views.edit_technician_profile_view, name='edit-technician-profile'),

    path('customer-dashboard/', views.customer_dashboard_view, name='customer-dashboard'),
    path('customer-request/', views.customer_request_view, name='customer-request'),
    path('customer-add-request/', views.customer_add_request_view, name='customer-add-request'),

    path('customer-profile/', views.customer_profile_view, name='customer-profile'),
    path('edit-customer-profile/', views.edit_customer_profile_view, name='edit-customer-profile'),
    path('customer-feedback/', views.customer_feedback_view, name='customer-feedback'),
    path('customer-invoice/', views.customer_invoice_view, name='customer-invoice'),
    path('customer-view-request/', views.customer_view_request_view, name='customer-view-request'),
    path('customer-delete-request/<int:pk>/', views.customer_delete_request_view, name='customer-delete-request'),
    path('customer-view-approved-request/', views.customer_view_approved_request_view, name='customer-view-approved-request'),
    path('customer-view-approved-request-invoice/', views.customer_view_approved_request_invoice_view, name='customer-view-approved-request-invoice'),

    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='itech/index.html'), name='logout'),

    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('contactus/', views.contactus_view, name='contactus'),
]
