from django.contrib.admin import ModelAdmin, site
from models import Tag, Project, Link, Idea, Tweet, Note, Book, BookAuthor, ReadingLog

class TagAdmin(ModelAdmin):
    pass

class ProjectAdmin(ModelAdmin):
    filter_horizontal = ['tags',]

class NoteAdmin(ModelAdmin):
    filter_horizontal = ['tags','projects']

class LinkAdmin(ModelAdmin):
    filter_horizontal = ['tags','projects']

class IdeaAdmin(ModelAdmin):
    filter_horizontal = ['tags',]

class TweetAdmin(ModelAdmin):
    filter_horizontal = ['tags',]
    list_display = ['tweet_id','text','created','updated']

class BookAuthorAdmin(ModelAdmin):
    pass

class BookAdmin(ModelAdmin):
    pass

class ReadingLogAdmin(ModelAdmin):
    pass

site.register(Tag, TagAdmin)
site.register(Project, ProjectAdmin)
site.register(Link, LinkAdmin)
site.register(Tweet, TweetAdmin)
site.register(Idea, IdeaAdmin)
site.register(Note, NoteAdmin)

site.register(BookAuthor, BookAuthorAdmin)
site.register(Book, BookAdmin)
site.register(ReadingLog, ReadingLogAdmin)

