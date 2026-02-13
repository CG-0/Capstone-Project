from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Seed(models.Model):
    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=80)
    species = models.CharField(max_length=150)
    seed_type = models.CharField(max_length=15)
    continent = models.CharField(max_length=20)
    slug = models.SlugField(max_length=500, null=True, db_index=True, help_text="SEO-friendly URLs")

    def get_absolute_url(self):
        return reverse("seeds-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)