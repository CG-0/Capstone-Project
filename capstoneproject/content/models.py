from django.db import models
from django.utils.text import slugify

# Create your models here.
class Seed(models.Model):
    HYBRID = "HYB"
    HEIRLOOM = "HE"
    OPEN_POLLINATED = "OP"

    SEED_TYPES = {
        HYBRID: "Hybrid",
        HEIRLOOM: "Heirloom",
        OPEN_POLLINATED: "Open-Pollinated",
    }

    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=80)
    species = models.CharField(max_length=150)
    seed_type = models.CharField(max_length=3, choices=SEED_TYPES, default=HYBRID)
    continent = models.CharField(max_length=20)
    slug = models.SlugField(max_length=500, null=True, help_text="SEO-friendly URLs")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)