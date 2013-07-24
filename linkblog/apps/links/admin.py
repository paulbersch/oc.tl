from django.contrib.admin import ModelAdmin, site, TabularInline
from models import Tag, Project, Link, Idea, Tweet, Page, Note, Book, BookAuthor, ReadingLog, Image, File

class RichTextAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/site_media/js/tinymce_setup.js',
        ]

class TagAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class ProjectAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ['tags','files','images']

class PageAdmin(RichTextAdmin):
    filter_horizontal = ['tags','files','images']

class NoteAdmin(RichTextAdmin):
    filter_horizontal = ['tags','projects','files','images']

class LinkAdmin(RichTextAdmin):
    filter_horizontal = ['tags','projects','files','images']

class IdeaAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ['tags','files','images']

class TweetAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ['tags','files','images']
    list_display = ['tweet_id','text','created','updated']

class BookAuthorAdmin(ModelAdmin):
    pass

class BookAdmin(ModelAdmin):
    pass

class ReadingLogAdmin(ModelAdmin):
    pass

class ImageAdmin(ModelAdmin):
    pass

class FileAdmin(ModelAdmin):
    pass

site.register(Tag, TagAdmin)
site.register(Project, ProjectAdmin)
site.register(Link, LinkAdmin)
site.register(Tweet, TweetAdmin)
site.register(Idea, IdeaAdmin)
site.register(Note, NoteAdmin)
site.register(Page, PageAdmin)

site.register(File, FileAdmin)
site.register(Image, ImageAdmin)

site.register(BookAuthor, BookAuthorAdmin)
site.register(Book, BookAdmin)
site.register(ReadingLog, ReadingLogAdmin)

# vim: tabstop=4:shiftwidth=4:set expandtab:retab
