import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from iam.models import User

def setup_admin():
    username = 'admin'
    password = '1234'
    email = 'admin@example.com'
    
    if not User.objects.filter(username=username).exists():
        print(f"Creating superuser {username}...")
        User.objects.create_superuser(username=username, password=password, email=email, role='admin')
        print("Superuser created successfully.")
    else:
        print(f"Superuser {username} already exists.")

if __name__ == "__main__":
    setup_admin()
