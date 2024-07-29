from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name

class Technician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/TechnicianProfilePic/', null=True, blank=True)
    address = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20, null=False)
    skill = models.CharField(max_length=500, null=True)
    salary = models.PositiveIntegerField(null=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name

class InternetPlan(models.Model):
    name = models.CharField(max_length=40, null=False)
    description = models.CharField(max_length=500, null=False)
    speed = models.CharField(max_length=20, null=False)
    price = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey('InternetPlan', on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.customer.user.username} - {self.plan.name}"

class UsageLog(models.Model):
    subscription = models.ForeignKey('Subscription', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    usage_gb = models.PositiveIntegerField(null=False)

class SupportTicket(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    technician = models.ForeignKey('Technician', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=False)
    status = models.CharField(max_length=20, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.user.username} - {self.title}"

class Installation(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    technician = models.ForeignKey('Technician', on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey('InternetPlan', on_delete=models.CASCADE, null=True)
    installation_date = models.DateField()
    status = models.CharField(max_length=20, default='Pending')

class Maintenance(models.Model):
    installation = models.ForeignKey('Installation', on_delete=models.CASCADE, null=True)
    technician = models.ForeignKey('Technician', on_delete=models.CASCADE, null=True)
    date = models.DateField()
    description = models.CharField(max_length=500, null=False)

class Report(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=500, null=False)
    generated_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=40)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f"Feedback by {self.by} on {self.date}"

class BillingHistory(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Billing History for {self.customer.user.username} on {self.date}"

class Usage(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateField()
    usage_gb = models.PositiveIntegerField()

    def __str__(self):
        return f"Usage for {self.customer.user.username} on {self.date}"
