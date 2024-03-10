#python manage.py test courses
#Ran 5 tests in 0.954s
#OK
#Code I wrote
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Course
from .forms import CourseForm

class CourseModelTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='teacher', email='teacher@example.com', password='pass')

    def test_course_creation(self):
        course = Course.objects.create(
            title='Test Course',
            description='Test description.',
            teacher=self.user,
        )
        self.assertEqual(course.title, 'Test Course')
        self.assertEqual(course.description, 'Test description.')
        self.assertEqual(course.teacher, self.user)

class CourseFormTests(TestCase):

    def test_valid_form(self):
        teacher = get_user_model().objects.create_user(username='teacher', email='teacher@example.com', password='password')
        data = {
            'title': 'Valid Course',
            'description': 'Valid description.',
            'teacher': teacher.id,  # Assuming the form accepts teacher ID
        }
        form = CourseForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {}
        form = CourseForm(data=data)
        self.assertFalse(form.is_valid())

class CourseViewsTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='secret')
        self.teacher = get_user_model().objects.create_user(username='teacher', email='teacher@example.com', password='pass')
        self.course = Course.objects.create(title='Enrollable Course', description='A course to enroll in.', teacher=self.teacher)

    def test_create_course_view(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('courses:create_course'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('courses:create_course'), {
            'title': 'New Test Course',
            'description': 'Test Course Description.',
            'teacher': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Course.objects.filter(title='New Test Course').exists())

    def test_course_list_view(self):
        response = self.client.get(reverse('courses:list_courses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'courses/list_courses.html')

# End of Code I wrote