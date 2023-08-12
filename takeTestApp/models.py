from django.db import models


class TestCenter(models.Model):
    name = models.CharField(max_length=100)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    startTiming = models.TimeField()
    endTiming = models.TimeField()
    totalSeats = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} {self.location_lat} {self.location_long}"



class Registration(models.Model):
    name = models.CharField(max_length=255)
    # testCenter = models.ManyToManyField(TestCenter)
    test_date = models.DateField()
    test_timing = models.TimeField()
    test_duration = models.DurationField()


