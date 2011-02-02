import datetime
from django.db import models
from django.contrib.auth.models import User
from markdown import markdown


class Addon(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    pub_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(editable=False)
    
    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        self.updated_date = date.datetime.now()
        self.description_html = markdown(self.description)
        super(Addon, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('addons_addon_detail', (), { 'object_id': self.id })
        
        
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    description_html = models.TextField(editable=False)
    
    addons = models.ManyToManyField(Addon, through='AddonCategory')
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'
        
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        self.description_html = markdown(self.description)
        super(Category, self).save(*args, **kwargs)

        
class AddonCategory(models.Model):
    addon = models.ForeignKey(Addon)
    category = models.ForeignKey(Category)
    
    class Meta:
        unique_together = ('addon', 'category')
        
        
class Version(models.Model):
    addon = models.ForeignKey(Addon)
    string = models.CharField(max_length=200)
    pub_date = models.DateTimeField(editable=False)
    releasenotes = models.TextField()
    releasenotes_html = models.TextField(editable=False)

    class Meta:
        ordering = ['-pub_date']
        
    def __unicode__(self):
        return "%s - %s" % (unicode(self.addon), self.string)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.pub_date = datetime.datetime.now()
        super(Version, self).save(*args, **kwargs)
        