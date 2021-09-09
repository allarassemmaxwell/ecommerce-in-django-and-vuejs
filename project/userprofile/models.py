from django.contrib.auth.models import User
from django.db import models




# USER PROFILE MODEL 
class Userprofile(models.Model):
    user 		 = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    address 	 = models.CharField(max_length=255, blank=True, null=True)
    zipcode 	 = models.CharField(max_length=255, blank=True, null=True)
    place 		 = models.CharField(max_length=255, blank=True, null=True)
    phone 		 = models.CharField(max_length=255, blank=True, null=True)
    date_added   = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return '%s' % self.user.username
User.userprofile = property(lambda u:Userprofile.objects.get_or_create(user=u)[0])