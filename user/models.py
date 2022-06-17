from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    # User
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('username must not be empty')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Super User
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField("이메일", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=50)
    fullname = models.CharField("이름", max_length=50)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="사용자", on_delete=models.CASCADE)
    description = models.TextField("한 줄 소개", max_length=256)
    age = models.IntegerField("나이")
    category = models.OneToOneField(Category, verbose_name="카테고리", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.fullname} 님의 프로필"