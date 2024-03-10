# python manage.py test users
# Ran 2 tests in 0.270s
# OK
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
# Test User creation
class UserAccountTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            username='testuser'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='supertest@example.com',
            password='testpass123',
            username='adminuser'
        )
        self.assertEqual(admin_user.email, 'supertest@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

# Test user authentication
def test_user_login(self):
    User = get_user_model()
    User.objects.create_user(email='user@example.com', password='testpass123', username='normaluser')
    response = self.client.post('/users/login/', {'username': 'normaluser', 'password': 'testpass123'})
    self.assertEqual(response.status_code, 302)
