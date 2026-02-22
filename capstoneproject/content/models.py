from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Use(models.Model):
    uses = models.CharField(max_length=50)

    def __str__(self):
        return self.uses

class DonorProfile(models.Model):
    bio = models.TextField()

    def __str__(self):
        if hasattr(self, 'donor'):
            return f"Profile for {self.donor}"
        else:
            return "Unassigned Profile"
    
    class Meta:
        verbose_name_plural = "Donor Profiles"

class Donor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile = models.OneToOneField(DonorProfile, on_delete=models.CASCADE, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Seed(models.Model):
    HYBRID = "HYB"
    OPEN_POLLINATED = "OP"
    HEIRLOOM = "HE"

    SEED_TYPE_CHOICES = {
        HYBRID: 'Hybrid',
        OPEN_POLLINATED: 'Open-Pollinated',
        HEIRLOOM: 'Heirloom',
    }

    name = models.CharField(max_length=100)
    genus = models.CharField(max_length=80)
    species = models.CharField(max_length=150)
    seed_type = models.CharField(max_length=3, choices=SEED_TYPE_CHOICES, default=HYBRID)
    continent = models.CharField(max_length=20)
    use = models.ForeignKey(Use, on_delete=models.SET_NULL, null=True, related_name="seeds")
    donors = models.ManyToManyField(Donor, related_name="seeds")
    slug = models.SlugField(max_length=500, null=True, db_index=True, help_text="SEO-friendly URLs")

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("seeds-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)