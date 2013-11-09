from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models import F


@python_2_unicode_compatible
class Link(models.Model):
    """
    Class for storing links.
    """
    slug = models.SlugField(primary_key=True)
    url = models.URLField()
    hit_count = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    def update_counter(self):
        self.hit_count = F('hit_count') + 1
        self.save(update_fields=['hit_count'])

    def save(self, *args, **kwargs):
        """
        Generate a random slug. Confusing characters are not included,
        which gives 55 unique characters. This allows for 27,680,640,625
        unique keys with a 6 character slug.
        """
        # Create random slug for new Links only
        if not self.slug:
            self.slug = User.objects.make_random_password(length=6)

            while Link.objects.filter(slug=self.slug):
                self.slug = User.objects.make_random_password(length=6)

        super(Link, self).save(*args, **kwargs)
