from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cow(models.Model):
    HEALTH_CHOICES = [
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor'),
        ('sick', 'Sick')
    ]
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tag_number = models.CharField(max_length=50, unique=True)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    health_condition = models.CharField(max_length=20, choices=HEALTH_CHOICES, default='good')
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} ({self.tag_number})"

class HealthRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.FloatField()
    heart_rate = models.IntegerField()
    appetite = models.CharField(max_length=20, choices=[
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    ])
    notes = models.TextField(blank=True)

class FeedRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    feed_type = models.CharField(max_length=100)
    quantity = models.FloatField()
    protein_content = models.FloatField()
    energy_content = models.FloatField()

class ProductionRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    morning_yield = models.FloatField()
    evening_yield = models.FloatField()
    
    @property
    def daily_yield(self):
        return self.morning_yield + self.evening_yield

class DailyFeedRecord(models.Model):
    cow = models.ForeignKey(Cow, on_delete=models.CASCADE)
    date = models.DateField()
    day_name = models.CharField(max_length=10)
    protein_feed = models.FloatField()
    silage = models.FloatField()
    minerals = models.FloatField()
    milk_yield = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Pending')
    is_ai_recommended = models.BooleanField(default=False)
    week_start_date = models.DateField(default=timezone.now)  # Track which week this belongs to
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        unique_together = ['cow', 'date']
        ordering = ['date']
