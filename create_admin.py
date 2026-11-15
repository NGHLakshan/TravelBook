import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("Admin user created: username: admin / password: admin123")
    else:
        u = User.objects.get(username='admin')
        u.set_password('admin123')
        u.is_superuser = True
        u.is_staff = True
        u.save()
        print("Admin user updated: username: admin / password: admin123")

if __name__ == '__main__':
    create_admin()

