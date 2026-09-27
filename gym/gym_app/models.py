from django.db import models
import re

class UserManager(models.manager):
    def reg_validation(postData):
        errors={}
        username = postData.get('username', '').strip()
        first_name = postData.get('first_name', '').strip()
        last_name = postData.get('last_name', '').strip()
        email = postData.get('email', '').strip()
        phone = postData.get('phone', '').strip()
        password = postData.get('password', '')
        confirm_pw = postData.get('confirm_pw', '')

        if len(postData['username']) == 0:
            errors["usernameerror"] = "username is required"
        if len(postData['first_name']) == 0:
            errors["firstnameerror"] = "firstname is required"
        if len(postData['last_name']) == 0:
            errors["lastnameerror"] = "lastname is required"
        if len(postData['email']) == 0:
            errors["emailerror"] = "email is required"
        if len(postData['phone']) == 0:
            errors["phoneerror"] = "phone is required"
        if len(postData['password']) == 0:
            errors["passworderror"] = "password is required"
        if len(postData['confirm_pw']) == 0:
            errors["confirm_pwerror"] = "confirm_pw is required"
        if len(postData['first_name']) < 4:
            errors["firstnameerror"] = "firstname must be at least 4 characters"
        if len(postData['last_name']) <4:
             errors["lastnameerror"] = "lastname must be at least 4 characters"
        if len(postData['password']) > 7:
            errors["passworderror"] = "password must be at least 4 characters"

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['emailerror'] = "Invalid email address!"

        if password != confirm_pw:
            errors["confirm_pwerror"] = "Passwords do not match."

        return errors



class User(models.Model):
    username=models.CharField(max_length=200,unique=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phonenumber=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_pw=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=UserManager()

class Participant(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    user=models.ForeignKey(  User , related_name="participants",on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
