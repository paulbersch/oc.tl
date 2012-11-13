from django.db import models
from django.template.defaultfilters import slugify

from django.db.models.query import QuerySet
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

class SubclassingQuerySet(QuerySet):
    def __getitem__(self, k):
        result = super(SubclassingQuerySet, self).__getitem__(k)
        if isinstance(result, models.Model) :
            return result.as_leaf_class()
        else :
            return result
    def __iter__(self):
        for item in super(SubclassingQuerySet, self).__iter__():
            yield item.as_leaf_class()

class ContentManager(models.Manager):
    def get_query_set(self):
        return SubclassingQuerySet(self.model)

class Content(models.Model):
    objects = ContentManager()

    name = models.CharField(max_length=500, unique=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('Tag', blank=True)

    content_type = models.ForeignKey(ContentType,editable=False,null=True)

    def __unicode__(self):
        return self.name

    def synopsis(self):
        return self.name

    def save(self, *args, **kwargs):
        if(not self.content_type):
            self.content_type = ContentType.objects.get_for_model(self.__class__)

        if self.name is None or self.name == '':
            self.name = " - ".join([unicode(self.content_type), unicode(self.created)])

        if self.id is None and not self.created:
            self.created = datetime.now()
        # auto-generate a slug
        if len(self.slug) == 0:
            if len(self.name) > 50:
                self.slug = slugify(self.name)[:50].lower()
            else:
               self.slug = slugify(self.name).lower()

        super(Content, self).save(*args, **kwargs)

    def as_leaf_class(self):
        content_type = self.content_type
        model = content_type.model_class()
        if (model == Content):
            return self
        try:
            return model.objects.get(id=self.id)
        except:
            return self

class Tag(models.Model):
    name = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    template = 'links/tag.html' 
    def get_absolute_url(self):
        return "/%s/" % "/".join(['t', self.slug])

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # auto-generate a slug
        if len(self.slug) == 0:
            if len(self.name) > 50:
                self.slug = slugify(self.name)[:50].lower()
            else:
                self.slug = slugify(self.name).lower()
        super(Tag, self).save(*args, **kwargs)

class Project(Content):
    code_url = models.CharField(max_length=500)
    example_url = models.CharField(max_length=500)

    template = 'links/detail/project.html'

    def get_absolute_url(self):
        return "/%s/" % "/".join([str(x) for x in ['p', self.created.year, self.created.month, self.created.day, self.slug]])

class Link(Content):
    url = models.CharField(max_length=500)
    excerpt = models.CharField(max_length=1000,blank=True)
    discussion = models.TextField()
    projects = models.ManyToManyField('Project', blank=True)

    template = 'links/detail/link.html'

    def sysnopsis(self):
        return self.discussion[:100] if len(self.discussion) > 100 else self.discussion

    def get_absolute_url(self):
        return "/%s/" % "/".join([str(x) for x in ['l', self.created.year, self.created.month, self.created.day, self.slug]])

class Idea(Content):
    description = models.TextField()

    template = 'links/detail/idea.html'

    def sysnopsis(self):
        return self.description[:100] if len(self.description) > 100 else self.description

    def get_absolute_url(self):
        return "/%s/" % "/".join([str(x) for x in ['i', self.created.year, self.created.month, self.created.day, self.slug]])

class Note(Content):
    text = models.TextField()
    projects = models.ManyToManyField('Project', blank=True)

    template = 'links/detail/note.html'

    def sysnopsis(self):
        return self.text[:100] if len(self.text) > 100 else self.text

    def get_absolute_url(self):
        return "/%s/" % "/".join([str(x) for x in ['n', self.created.year, self.created.month, self.created.day, self.slug]])

class Tweet(Content):
    tweet_id = models.CharField(max_length=100, unique=True)
    text = models.CharField(max_length=500)

    raw_tweet_json = models.TextField()

    template = 'links/detail/tweet.html'

    def sysnopsis(self):
        return ""

    def get_absolute_url(self):
        return "/%s/" % "/".join([str(x) for x in ['s', self.created.year, self.created.month, self.created.day, self.slug]])

class BookAuthor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # auto-generate a slug
        if len(self.slug) == 0:
            if len(self.name) > 50:
                self.slug = slugify(self.name)[:50].lower()
            else:
               self.slug = slugify(self.name).lower()

        super(BookAuthor, self).save(*args, **kwargs)

class Book(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=50, blank=True, unique=True)

    author = models.ForeignKey(BookAuthor)
    description = models.TextField()
    purchase_link = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # auto-generate a slug
        if len(self.slug) == 0:
            if len(self.title) > 50:
                self.slug = slugify(self.title)[:50].lower()
            else:
               self.slug = slugify(self.title).lower()

        super(Book, self).save(*args, **kwargs)

class ReadingLog(Content):
    book = models.ForeignKey(Book)
    page = models.IntegerField(blank=True)
    chapter = models.IntegerField(blank=True)
    placename = models.CharField(max_length=100, blank=True)

    text = models.TextField()

    template = 'links/detail/readinglog.html'

    def sysnopsis(self):
        return self.text[:100] if len(self.text) > 100 else self.text

    def get_absolute_url(self):
        return "/%s/" % "/".join([str(x) for x in ['r', self.book.slug, self.created.year, self.created.month, self.created.day, self.slug]])

