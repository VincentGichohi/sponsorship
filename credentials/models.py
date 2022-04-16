from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, ** extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email = self.normalize_email(email, ** extra_fields),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_staffuser(self, email, password, ** extra_fields):
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password, ** extra_fields):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self.db)
        return user
class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True,
    )
    is_active = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)
    is_sponsor = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

