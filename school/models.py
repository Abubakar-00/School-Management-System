from django.db import models
from django.contrib.auth.models import User

class TeacherExtra(models.Model):
    CLASS_CHOICES = [
        (None, 'null'),
        ('one', 'One'),
        ('two', 'Two'),
        ('three', 'Three'),
        ('four', 'Four'),
        ('five', 'Five'),
        ('six', 'Six'),
        ('seven', 'Seven'),
        ('eight', 'Eight'),
        ('nine', 'Nine'),
        ('ten', 'Ten'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_incharge = models.CharField(max_length=10, choices=CLASS_CHOICES, default=None, null=True, blank=True, unique=True)
    salary = models.PositiveIntegerField(null=True, default=None)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    cnic = models.CharField(max_length=15, null=True)
    father = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

classes=[('one','one'),('two','two'),('three','three'),
('four','four'),('five','five'),('six','six'),('seven','seven'),('eight','eight'),('nine','nine'),('ten','ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10, unique=True, null=True, blank=True)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    status = models.BooleanField(default=False)
    cnic = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=200, null=True)
    father = models.CharField(max_length=200, null=True)
    fcnic = models.CharField(max_length=15, null=True)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name
    def save(self, *args, **kwargs):
        if not self.roll:
            # Generate the roll based on class and existing count
            class_roll_count = StudentExtra.objects.filter(cl=self.cl).count() + 1
            self.roll = f"{self.cl}-{class_roll_count}"
        super().save(*args, **kwargs)

class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)


class FeeRecord(models.Model):
    student = models.ForeignKey(StudentExtra, on_delete=models.CASCADE)
    month = models.CharField(max_length=9)  # Example: 'January 2023'
    year = models.IntegerField(default=2023)  # Add the 'year' field
    status = models.CharField(max_length=7, choices=[('Paid', 'Paid'), ('Unpaid', 'Unpaid')], default='Unpaid')
    amount = models.IntegerField(default=0)

    class Meta:
        unique_together = ('student', 'month', 'year')  # Update unique_together constraint

    def __str__(self):
        return f"{self.student.get_name()}'s fee for {self.month}"

class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)