import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.db import connection

def setup_admin():
    username = 'admin'
    password = '1234'
    email = 'admin@example.com'
    
    # Check if the table exists
    if "iam_user" not in connection.introspection.table_names():
        print("Table 'iam_user' does not exist yet. Skipping superuser creation.")
        return

    try:
        from iam.models import User
        if not User.objects.filter(username=username).exists():
            print(f"Creating superuser {username}...")
            User.objects.create_superuser(username=username, password=password, email=email, role='admin')
            print("Superuser created successfully.")
        else:
            print(f"Superuser {username} already exists.")
    except Exception as e:
        print(f"Error during superuser creation: {e}")

if __name__ == "__main__":
    setup_admin()
