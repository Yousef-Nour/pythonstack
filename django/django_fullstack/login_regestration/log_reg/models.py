from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        if len(postData['fname']) < 2 :
            errors["fname-length"] = "First Name should be at least 2 characters"
        if not NAME_REGEX.match(postData['fname']):
            errors["fname-char"] = "First Name should only contain characters"
        if len(postData['lname']) < 2:
            errors["lname-length"] = "Last Name should be at least 2 characters"
        if not NAME_REGEX.match(postData['lname']):
            errors["lname-char"] = "Last Name should only contain characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['passwd']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['passwd'] != postData['confpasswd']:
            errors['confpasswd'] = "Password doesn't match Confirm Password"
        return errors
    def login_validator(self,postData):
        errors = {}
        users = User.objects.filter(Email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not len(users):
            errors['email'] = "Email not Found!"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        elif not bcrypt.checkpw(postData['passwd'].encode(), users[0].Password.encode()):
            errors["password"] = "Wrong Password!"
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    Email = models.CharField(max_length=225)
    Password = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

def create_user(first_name,last_name,email,passwd):
    return User.objects.create(first_name=first_name,last_name=last_name,Email=email,Password=passwd)

def get_user(email):
    users = User.objects.filter(Email=email)
    if len(users) > 0:
        return users[0]
    return None