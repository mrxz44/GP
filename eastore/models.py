from django.db import models
from django.utils.text import slugify
from django.shortcuts import redirect
from django.db import models
from django.urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField

class TradingRobots(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    key_words = models.CharField(max_length=555, blank=True)
    description = models.CharField(max_length=1555, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    class Meta:
        verbose_name = "TradingRobot"
        verbose_name_plural = "TradingRobots"
        ordering = ['-time_create', ]
