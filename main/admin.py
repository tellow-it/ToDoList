from django.contrib import admin
from main.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    model = ToDo
    list_display = ['important', 'title', 'slug', 'category', 'description', 'deadline', 'date_creation']
    list_filter = ['category', 'important']
    list_display_links = ['title']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ToDo, ToDoAdmin)
