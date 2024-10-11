from django.db import models

class Account(models.Model):
    email_id = models.EmailField(unique=True, blank=False)
    account_id = models.CharField(unique=True,  max_length=20, blank=False)
    account_name = models.CharField(max_length=200, blank=False)
    app_token  = models.CharField(max_length=40, blank=False)
    website =  models.URLField(blank=True)


