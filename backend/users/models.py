from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
            self, first_name, last_name, email, phone_number,
            password, is_waiter=False, is_cooker=False, is_admin=False
    ):
        if not email:
            raise ValueError('Email is required!')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            is_waiter=is_waiter,
            is_cooker=is_cooker,
            is_admin=is_admin,
            phone_number=phone_number,
        )

        if is_admin:
            user.is_waiter = False
            user.is_cooker = False
            user.role = 1
        elif is_waiter:
            user.is_cooker = False
            user.role = 2
        elif is_cooker:
            user.role = 3
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, phone_number, password):
        user = self.create_user(first_name, last_name, email, phone_number, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    Admin = 1
    Waiter = 2
    Cooker = 3

    ROLE_CHOICES = (
        (Admin, 'Admin'),
        (Waiter, 'Waiter'),
        (Cooker, 'Cooker'),
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number should have format '+375xxxxxxxxx'")

    first_name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Surname', max_length=100)
    email = models.EmailField('Email', max_length=200, unique=True)
    phone_number = models.CharField('Phone number', max_length=100, validators=[phone_regex],
                                    null=True, blank=True,unique=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    is_waiter = models.BooleanField('Waiter', default=False, blank=True)
    is_cooker = models.BooleanField('Cooker', default=False, blank=True)
    is_admin = models.BooleanField('Administrator', default=False, blank=True)
    is_active = models.BooleanField('Active', default=True)
    is_staff = models.BooleanField('Staff', default=True)
    is_superuser = models.BooleanField('Superuser', default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()
