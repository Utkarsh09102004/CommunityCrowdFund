from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    aadhar_number = models.CharField(max_length=12, unique=True, validators=[RegexValidator(regex='^\d{12}$', message='Aadhar number must be 12 digits long.')])
    phone_number = models.CharField(max_length=15, unique=True, validators=[RegexValidator(regex='^\+?1?\d{9,15}$', message='Phone number must be valid.')])
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Initiative(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)

    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='initiative_images/', null=True, blank=True)
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.title

# class Contribution(models.Model):
#     contributor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     payment_id = models.CharField(max_length=100, blank=True, null=True)
#     payment_status = models.CharField(max_length=50, blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.contributor.username} - {self.initiative.title}"

