from django.db import models
from django.contrib.auth.models import User


class Write(models.Model):
    choice = (
        ('tech', '#tech'),
        ('politics', '#politics'),
        ('history', '#history'),
        ('health', '#health'),
        ('education', '#education'),
        ('sports', '#sports'),
        ('family', '#family'),
        ('food', '#food'),
        ('news', '#news'),
    )
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    category = models.CharField(max_length=50, choices=choice, default='tech')
    image = models.ImageField(upload_to="images/")
    upvotes_total = models.IntegerField(default=1)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
