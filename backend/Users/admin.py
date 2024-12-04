from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from Users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    ordering = ("username",)
    search_fields = ("username", "email", "first_name", "last_name")
    fieldsets = (
        (_("Security"), {"fields": ("username", "email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name","date_of_birth","gender","mobile_number","photo")}),
        (_("Social Media"), {"fields": ("linkedin", "github", "facebook")}),
        (_("Objectives"), {"fields": ("objective",)}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser", "user_permissions"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
    exclude = ("UUID",)  # exclude UUID field from CustomUserAdmin form

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
    
admin.site.register(CustomUser, CustomUserAdmin)


admin.site.unregister(Group)

admin.site.site_header = "Portfolio Admin Panel"
admin.site.site_title = "Portfolio Admin Panel"
admin.site.index_title = "Management Panel"


