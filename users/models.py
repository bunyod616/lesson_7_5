from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint

# Create your models here.
ORDINARY_USER, ADMIN, MANAGER = ('ordinary_user', 'admin', 'manager')
VIA_EMAIL, VIA_PHONE = ('via_email', 'via_phone')
NEW, CONFIRM, DONE, DONE_PHOTO = ('new', 'confirm', 'done', 'done_photo')
MALE, FEMALE = ('male', 'female')


class User(AbstractUser):
    USER_ROLL = (
        (ORDINARY_USER, ORDINARY_USER),
        (ADMIN, ADMIN),
        (MANAGER, MANAGER),
    )
    USER_TYPES = (
        (VIA_EMAIL, VIA_EMAIL),
        (VIA_PHONE, VIA_PHONE),
    )

    USER_STATUS = (
        (NEW, NEW),        (CONFIRM, CONFIRM),
        (DONE, DONE),
        (DONE_PHOTO, DONE_PHOTO),
    )
    GENDER = (
        (MALE, MALE),
        (FEMALE, FEMALE),
    )

    user_roll = models.CharField(max_length=20, choices=USER_ROLL, default=ORDINARY_USER)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    user_status = models.CharField(max_length=20, choices=USER_STATUS)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='user_photo', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER)

    def __str__(self):
        return self.first_name


class Code(models.Model):
    code = models.CharField(max_length=20)
    is_confirm = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    user_roll = models.CharField(max_length=20, choices=User.USER_ROLL)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(str(randint(1, 100) % 10) for _ in range(4))
            print("kod = ", self.code)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Done(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='done_entries')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=User.GENDER)
    password = models.CharField(max_length=128)
