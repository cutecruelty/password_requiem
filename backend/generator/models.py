from django.db import models

class GenerationLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField()
    entropy_bits = models.FloatField()
    breach_count = models.IntegerField(default=0)
    