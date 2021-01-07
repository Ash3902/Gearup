from django.db import models

# Create your models here.
class Career(models.Model):
    heading = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    apply_link = models.URLField()
    job_posted = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.heading
    class Meta:
        ordering = ("apply_link",)