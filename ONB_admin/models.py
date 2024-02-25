# My Django imports
from django.db import models

# My App imports
from ONB_auth.models import Accounts

# Create your models here.
class Notification(models.Model):
    created_by = models.ForeignKey(to=Accounts, on_delete=models.CASCADE, blank=True, null=True, related_name="created_by")
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(null=True, upload_to='uploads/')
    description = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name_plural = 'Notifications'
        db_table = 'Notifications'

    def __str__(self):
        return f'TITLE: {self.title} | CREATED: {self.created_by}'

class Comment(models.Model):
    posted_by = models.ForeignKey(to=Accounts, on_delete=models.CASCADE, blank=True, null=True, related_name="posted_by")
    commented_on = models.ForeignKey(to=Notification, on_delete=models.CASCADE, blank=True, null=True, related_name="commented_on")
    comment = models.TextField(max_length=1000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Comments'
        db_table = 'Comments'

    def __str__(self):
        return f'{self.posted_by.username}: made a comment on {self.commented_on.title}'