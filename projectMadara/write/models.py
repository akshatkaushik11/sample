# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
#for slug field
from django.db.models.signals import pre_save
from django.utils.text import slugify

from django.utils import timezone


class TotoManager(models.Manager):
    def active(self, *args, **kwargs):  #this allows to list all the valid totos @ Toto.objects.active()
        # In a way, Toto.objects.all() = super(TotoManager, self).all()
        return super(TotoManager, self).filter(draft=False).filter(publish__lte=timezone.now())

    def draft(self, *args, **kwargs):
        return super(TotoManager, self).filter(draft=True)


def upload_location(instance, filename):
    return "totos/%s/%s" %(instance.slug, filename)


# Create your models here.
class Toto(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, default=1 )
    title        = models.CharField(max_length=200, unique=True, blank=False, null=False)
    slug         = models.SlugField(unique=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    content      = models.TextField()

    author       = models.CharField(max_length=150, unique=False)
    cover_photo  = models.ImageField(upload_to=upload_location,
                            blank=True,
                            null=True, 
                            width_field="width_field",
                            height_field="height_field")
    width_field  = models.IntegerField(default=0, null=True)
    height_field = models.IntegerField(default=0, null=True)

    draft        = models.BooleanField(default=False)
    publish      = models.DateTimeField(auto_now=True)

    objects = TotoManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse("toto:detail", kwargs={"id":self.id})
        return reverse("toto:detail", kwargs={"slug" : self.slug})
    class Meta:
        ordering = ["-timestamp" , "-last_updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    qs = Toto.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


# signal receiver
def pre_save_toto_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_toto_receiver, sender=Toto)
