from django.contrib.admin import ModelAdmin, site
from models import Tag, Project, Link, Idea, Tweet

class TagAdmin(ModelAdmin):
    pass

class ProjectAdmin(ModelAdmin):
    filter_horizontal = ['tags',]

class LinkAdmin(ModelAdmin):
    filter_horizontal = ['tags','projects']

class IdeaAdmin(ModelAdmin):
    filter_horizontal = ['tags',]

class TweetAdmin(ModelAdmin):
    filter_horizontal = ['tags',]
    list_display = ['tweet_id','text','created','updated']

site.register(Tag, TagAdmin)
site.register(Project, ProjectAdmin)
site.register(Link, LinkAdmin)
site.register(Tweet, TweetAdmin)
site.register(Idea, IdeaAdmin)
