from django.contrib import admin
from .models import MarkdownExample
from markdownx.admin import MarkdownxModelAdmin


# Register the MarkdownExample model with MarkdownxModelAdmin
@admin.register(MarkdownExample)
class MarkdownExampleAdmin(MarkdownxModelAdmin):
    list_display = ('title',)  # Displays the title in the list view
    search_fields = ('title',)  # Allows searching by title
