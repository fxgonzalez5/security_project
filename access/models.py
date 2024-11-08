from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    code_generated_at = models.DateTimeField(null=True, blank=True)
    roles = models.ManyToManyField('Role', through='UserRole')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.roles.exists():
            cliente_role, created = Role.objects.get_or_create(description="Cliente")
            UserRole.objects.get_or_create(user=self, role=cliente_role)

    def __str__(self):
        return "Usuario: %s - %s - %s - %s" % (self.name, self.username, self.password, self.status)


class Role(models.Model):
    description = models.CharField(max_length=45)
    users = models.ManyToManyField('User', through='UserRole')
    functions = models.ManyToManyField('Function', through='RoleFunction')

    def __str__(self):
        return "Rol: %s" % self.description


class Function(models.Model):
    description = models.CharField(max_length=45)
    roles = models.ManyToManyField('Role', through='RoleFunction')

    def __str__(self):
        return "Función: %s" % self.description


class UserRole(models.Model):
    user = models.ForeignKey(User, related_name='losroles', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, related_name='losroles', on_delete=models.CASCADE)

    def __str__(self):
        return "Roles del usuario %s: %s" % (self.user.name, self.role)


class RoleFunction(models.Model):
    role = models.ForeignKey(Role, related_name='lasfunciones', on_delete=models.CASCADE)
    function = models.ForeignKey(Function, related_name='lasfunciones', on_delete=models.CASCADE)

    def __str__(self):
        return "Funciones que pertenecen al rol de %s: %s" % (self.role.description, self.function)
