from django.db import models

class GenerationLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    length = models.IntegerField()
    entropy_bits = models.FloatField()
    breach_count = models.IntegerField(default=0)

class GenerationPolicy(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField(default=16)
    use_symbols = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
