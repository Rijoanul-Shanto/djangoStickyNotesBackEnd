from django.db import models

class Topic(models.Model):
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='contents')
    subTopic = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.subTopic