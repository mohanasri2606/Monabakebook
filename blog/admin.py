from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','display_image')
    search_fields = ('title', 'category__name')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',) 
    class Meta:
        ordering = ['-created_at'] 

    def display_image(self, obj):
        if obj.img:  # Check if image exists
            return format_html('<img src="{}" width="100" />', obj.img.url)
        return "No Image"

    display_image.allow_tags = True
    display_image.short_description = "Image"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',) 

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
