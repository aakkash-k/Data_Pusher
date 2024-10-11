from django.db import models

class Destination(models.Model):
    account_id = models.CharField(max_length=20, blank=False)
    url = models.URLField(blank=False)
    http_method = models.CharField(blank=False, max_length=10, choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT')])
    headers = models.JSONField(blank=False) 

   
