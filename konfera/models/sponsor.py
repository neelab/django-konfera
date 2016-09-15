from django.db import models
from konfera.models import Event

SPONSOR_TYPE = (
    ('platinum', 'Platinum'),
    ('gold', 'Gold'),
    ('silver', 'Silver'),
    ('bronze', 'Bronze'),
    ('other', 'Other'),
    ('django_girls', 'Django girls'),
)


class Sponsor(models.Model):
    title = models.CharField(max_length=128)
    type = models.CharField(choices=SPONSOR_TYPE, max_length=32)
    logo = models.FileField()
    url = models.URLField()
    about_us = models.TextField()
    event = models.ForeignKey(Event, null=False)

    def __str__(self):
        return self.title