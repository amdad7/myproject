from django.test import TestCase,Client
from .models import *
from django.utils import timezone
from django.urls import reverse
# Create your tests here.

"""testing loging system """

class User_model_test(TestCase):
    def test_create_user(self):
        """testing whether we can create user"""
        u=User(user_text='blah',password="1234")
        self.assertIs(u.password=='1234',True)
        self.assertIs(u.user_text=='blah',True)

"""testing views"""

def user_create(user_name,password):
    u=User(user_text=user_name,password=password,pub_date=timezone.now())
    return u
u1=User('person1',1234)

class indecvtest(TestCase):
    def test_page_status(self):
        """testing the index view"""
        response=self.client.get(reverse('polls:index'))
        self.assertIs(response.status_code,200)

class logintest(TestCase):
    def test_user_login_sccs(self):
        """succesful login"""
        c=Client()
        response=c.post(reverse('datac:login'),{'username':'person1','password':1234})
        self.assertEqual(response.status_code,200)
    def test_user_login_fail(self):
        """wrong user name or pass word"""
        c=Client()
        response=c.post(reverse('datac:login'),{'username':'person1','password':1234})
        self.assertRedirects(response,'/datac/'+str(u1.id)+'/',
            target_status_code=200)
