from django.contrib.auth import get_user_model

# Get the user model
User = get_user_model()

# Example: Retrieve a user instance by username
try:
    user_instance = User.objects.get(username='example_username')
    print(user_instance)
except User.DoesNotExist:
    print("User does not exist")
    user_instance = User.objects.filter(username='example_username').first()
    if user_instance:
        print(user_instance)
    else:
        print("User does not exist")