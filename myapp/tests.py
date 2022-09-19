
from tkinter import NO
from urllib import response
from django.urls import reverse, resolve
from django.test import TestCase, SimpleTestCase, Client

# for url testing
from myapp.views import *

# for view testing
from myapp.models import *

#  testing url 
class TestUrls(SimpleTestCase):

    def test_home_url(self):
        
        url = reverse(home)
        self.assertEquals(resolve(url).func, home)

    def test_findbus_url(self):

        url = reverse(findbus)
        self.assertEquals(resolve(url).func, findbus)

    def test_bookings_url(self):

        url = reverse(bookings)
        self.assertEquals(resolve(url).func, bookings)

    def test_cancellings_url(self):

        url = reverse(cancellings)
        self.assertEquals(resolve(url).func, cancellings)

    def test_seekbookings_url(self):

        url = reverse(seebookings)
        self.assertEquals(resolve(url).func, seebookings)
    
    def test_signup_url(self):

        url = reverse(signup)
        self.assertEquals(resolve(url).func, signup)
    
    def test_signin_url(self):

        url = reverse(signin)
        self.assertEquals(resolve(url).func, signin)
    
    def test_success_url(self):

        url = reverse(success)
        self.assertEquals(resolve(url).func, success)

