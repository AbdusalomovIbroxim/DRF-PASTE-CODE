from django.db import models
import random
import string


def generate_code():
    while True:
        code = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) for _ in range(3))
        if not Task.objects.filter(code=code).exists():
            return code


class Task(models.Model):
    code = models.URLField(max_length=10, blank=True, null=True, unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_code()
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.pk
