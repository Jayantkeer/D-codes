from multiprocessing.util import is_abstract_socket_namespace
from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostMOdelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']