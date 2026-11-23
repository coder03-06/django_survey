
from django.db import models


class SurveyResponse(models.Model):

    TECHNOLOGY_CHOICES = [
        ('Python', 'Python'),
        ('Java', 'Java'),
        ('JavaScript', 'JavaScript'),
        ('Django', 'Django'),
        ('Other', 'Other'),
    ]

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    name = models.CharField(max_length=100)

    email = models.EmailField()

    technology = models.CharField(
        max_length=30,
        choices=TECHNOLOGY_CHOICES
    )

    rating = models.IntegerField(
        choices=RATING_CHOICES
    )

    feedback = models.TextField()

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
