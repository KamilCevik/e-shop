from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, help_text='(5xx-xxx-xx-xx)')
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    image = models.ImageField( upload_to='images/users/', default='images/users/defaultprofile.jpeg')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + ']'

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" width="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'city', 'country', 'image']
