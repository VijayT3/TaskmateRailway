from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
#  any name, foreighkey creates connection bet task and user,
#  we want to create conn with user model
#  if user is del, all his tasks will be deleted

    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)
