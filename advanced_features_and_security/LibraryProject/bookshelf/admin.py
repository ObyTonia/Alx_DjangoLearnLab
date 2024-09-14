from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

"CUSTOM USER"
# bookshelf/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)


"Create and Configure Groups with Assigned Permissions"



from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

# Create groups
editors_group, created = Group.objects.get_or_create(name='Editors')
viewers_group, created = Group.objects.get_or_create(name='Viewers')
admins_group, created = Group.objects.get_or_create(name='Admins')

# Get content type for the Book model
book_content_type = ContentType.objects.get_for_model(Book)

# Assign permissions
can_view = Permission.objects.get(codename='can_view', content_type=book_content_type)
can_create = Permission.objects.get(codename='can_create', content_type=book_content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=book_content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=book_content_type)

# Assign permissions to groups
editors_group.permissions.add(can_create, can_edit)
viewers_group.permissions.add(can_view)
admins_group.permissions.add(can_view, can_create, can_edit, can_delete)
