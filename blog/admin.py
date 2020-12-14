from django.contrib import admin
from blog import models



@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)} #타이틀과 똑같이 입력되게 하는 기능
    raw_id_fields = ('author',) # 검색 용이하게 하는 기능
    date_hierarchy = 'publish'
    ordering = ('status','publish')
    

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','post','created','active')
    list_filter = ('active','created','updated')
    search_fields = ('name','email','body')