from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', '管理员'),
        ('user', '普通用户'),
        ('viewer', '游客'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="手机号")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="头像")
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user', verbose_name="角色")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = '用户管理'

    def __str__(self):
        return self.username