from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from core.base.models import BaseModel
from core.users.managers import UserManager


class User(BaseModel, AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(verbose_name="full name", max_length=200)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    is_active = models.BooleanField(verbose_name="active status", default=True)
    password_reset_required = models.BooleanField(
        verbose_name="password reset status", default=False
    )
    is_admin = models.BooleanField(verbose_name="admin status", default=False)

    google_id = models.CharField(max_length=50, blank=True, null=True)

    last_login = models.DateTimeField(verbose_name="last login", blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(
        verbose_name="last login ip", blank=True, null=True
    )

    date_joined = models.DateTimeField(
        verbose_name="date joined", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name"]

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.email

    # Admin Settings
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# class Member(BaseModel):
#     class Role(models.TextChoices):
#         ADMIN = ("owner", "OWNER")
#         STAFF = ("staff", "STAFF")

#     merchant = models.ForeignKey(
#         Merchant, on_delete=models.CASCADE, related_name="members"
#     )
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="merchant_members"
#     )
#     role = models.CharField(max_length=10, default=Role.STAFF)

#     class Meta:
#         db_table = "members"

#     def __str__(self) -> str:
#         return str(self.id)
