``` Python
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
