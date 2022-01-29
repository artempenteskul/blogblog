from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True, db_index=True, verbose_name='Title')
    slug = models.SlugField(max_length=250, null=True, blank=True)
    text = models.TextField(verbose_name='Text')
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
