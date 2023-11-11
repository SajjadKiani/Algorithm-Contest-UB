from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=255, verbose_name="نام تیم")
    university = models.CharField(max_length=255, verbose_name="نام دانشگاه", null=True, blank=True)
    language = models.CharField(max_length=120, verbose_name="زبان برنامه نویسیس")
    agree = models.BooleanField(default=False, verbose_name="موافقت نامه")
    GENDER_CHOICES = [
        ('M', 'مرد'),
        ('F', 'زن'),
    ]
    first_name1 = models.CharField(max_length=255)
    last_name1 = models.CharField(max_length=255)
    gender1 = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone1 = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^\d{11}$', 'Enter a valid 11-digit phone number.')]
    )
    email1 = models.CharField(max_length=255)
    education1 = models.CharField(max_length=255, null=True, blank=True)
    student_number1 = models.CharField(max_length=20, null=True, blank=True)

    first_name2 = models.CharField(max_length=255)
    last_name2 = models.CharField(max_length=255)
    gender2 = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone2 = models.CharField(
        max_length=11,
        validators=[RegexValidator(r'^\d{11}$', 'Enter a valid 11-digit phone number.')]
    )
    email2 = models.CharField(max_length=255)
    education2 = models.CharField(max_length=255, null=True, blank=True)
    student_number2 = models.CharField(max_length=20, null=True, blank=True)

    first_name3 = models.CharField(max_length=255, null=True, blank=True)
    last_name3 = models.CharField(max_length=255, null=True, blank=True)
    gender3 = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    phone3 = models.CharField(max_length=11, null=True, blank=True)
    email3 = models.CharField(max_length=255, null=True, blank=True)
    education3 = models.CharField(max_length=255, null=True, blank=True)
    student_number3 = models.CharField(max_length=20, null=True, blank=True)


    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date", "team_name", "language"]
        verbose_name = "تیم"
        verbose_name_plural = "تیم ها"
    def __str__(self):
        return self.team_name


class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=100, null=True, blank=True, default=None)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return "{} - {}".format(self.name, self.subject)


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
