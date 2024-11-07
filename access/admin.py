from django.contrib import admin
from .models import *


# Register your models here.
# Inline para la relación ManyToMany entre Role y Function a través de RoleFunction
class RoleFunctionInline(admin.TabularInline):
    model = RoleFunction
    extra = 1
    verbose_name = "Función"
    verbose_name_plural = "Funciones"


# Inline para la relación ManyToMany entre User y Role a través de UserRole
class UserRoleInline(admin.TabularInline):
    model = UserRole
    extra = 1
    verbose_name = "Rol"
    verbose_name_plural = "Roles"


# Vista de administración para el modelo Usuario
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'status')
    inlines = [UserRoleInline]  # Inline para roles
    search_fields = ('name', 'username')
    list_filter = ('status',)
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"


admin.site.register(User, UserAdmin)


# Vista de administración para el modelo Rol
class RoleAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    inlines = [RoleFunctionInline]  # Inline para funciones
    verbose_name = "Rol"
    verbose_name_plural = "Roles"


admin.site.register(Role, RoleAdmin)


# Vista de administración para el modelo UserRole (si es necesario directamente en el admin)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__name', 'role__description')
    verbose_name = "Asignación de Rol"
    verbose_name_plural = "Asignaciones de Roles"


admin.site.register(UserRole, UserRoleAdmin)


# Vista de administración para el modelo Function
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)
    verbose_name = "Función"
    verbose_name_plural = "Funciones"


admin.site.register(Function, FunctionAdmin)


# Vista de administración para el modelo RoleFunction (si es necesario directamente en el admin)
class RoleFunctionAdmin(admin.ModelAdmin):
    list_display = ('role', 'function')
    search_fields = ('role__description', 'function__name')
    verbose_name = "Asignación de Función"
    verbose_name_plural = "Asignaciones de Funciones"


admin.site.register(RoleFunction, RoleFunctionAdmin)
