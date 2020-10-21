from django.test import SimpleTestCase
from accounts.forms import UserLoginForm,UserProfileDetailsForm

class TestForms(SimpleTestCase):
    def test_userLoginForm(self):
        form = UserLoginForm({})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
    
    def test_userProfileDetailsForm(self):
        form = UserProfileDetailsForm({})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)

    def test_userProfileDetailsFormValid(self):
        form = UserProfileDetailsForm({
            'bio' : 'Todo',
            'dob' : '1980-10-10'
        })
        self.assertTrue(form.is_valid())
        self.assertEquals(form.data['bio'],'Todo')

