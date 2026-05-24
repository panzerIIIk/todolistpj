from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=True)

    def __str__(self):
        created = self.created.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.id}. {self.title} 時間:{created}"
