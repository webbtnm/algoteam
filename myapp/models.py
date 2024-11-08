from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents', null = True, blank = True)

    def __str__(self):
        return self.title()


