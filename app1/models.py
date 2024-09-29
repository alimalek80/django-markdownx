from django.db import models
from django.urls import reverse
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField


class MarkdownExample(models.Model):
    title = models.CharField(max_length=200)
    markdown_description = MarkdownxField()

    # Create a property that returns the markdown
    @property
    def formatted_markdown(self):
        return markdownify(self.markdown_description)

    def get_absolute_url(self):
        return reverse('markdown-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
