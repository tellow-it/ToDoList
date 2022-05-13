from django.db import models


class ToDo(models.Model):
    CHOICES_CATEGORY = (
        ('University', 'University'),
        ('Study', 'Study'),
        ('Self education', 'Self education'),
        ('Other charge', 'Other charge')
    )

    CHOICES_IMPORTANT = (('Important', 'Important'),
                         ('Normal', 'Normal'),
                         ('Not big deal', 'Not big deal'))
    important = models.CharField(max_length=100, choices=CHOICES_IMPORTANT)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(choices=CHOICES_CATEGORY, max_length=20)
    description = models.TextField()
    deadline = models.DateTimeField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#test