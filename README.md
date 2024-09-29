

# Markdownx

This guide explains how to install and configure `django-markdownx` in your Django project for managing markdown content. Also including how to use Pygments for code highliting. 

### Installation

First, install the `django-markdownx` package:

```bash
pip install django-markdownx
```

### Configuration

After installation, add `markdownx` to the `INSTALLED_APPS` in your `settings.py` file:

```python
INSTALLED_APPS = [
    # other apps...
    'markdownx',
]
```

### URL Configuration

Next, add the MarkdownX URL patterns to your `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('markdownx/', include('markdownx.urls')),
    path('', include('app1.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Models

In your `models.py` file, create a model with a `MarkdownxField()` to store markdown content:

```python
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.urls import reverse

class MarkdownExample(models.Model):
    title = models.CharField(max_length=200)
    markdown_description = MarkdownxField()

    @property
    def formatted_markdown(self):
        return markdownify(self.markdown_description)

    def get_absolute_url(self):
        return reverse('markdown-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
```

### Forms

In `forms.py`, create a form for your `MarkdownExample` model:

```python
from django import forms
from .models import MarkdownExample

class MarkDownExampleForm(forms.ModelForm):
    class Meta:
        model = MarkdownExample
        fields = '__all__'
```

### Views

Add the following views to your `views.py` file:

```python
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import MarkdownExample
from .forms import MarkDownExampleForm
from django.urls import reverse_lazy

class MarkdownDetailView(DetailView):
    model = MarkdownExample
    template_name = 'app1/markdown_detail.html'

class MarkdownListView(ListView):
    model = MarkdownExample
    template_name = 'app1/markdown_list.html'
    context_object_name = 'markdown_example'

class MarkdownCreateView(CreateView):
    model = MarkdownExample
    form_class = MarkDownExampleForm
    template_name = 'app1/markdown_form.html'
    success_url = reverse_lazy('markdown-list')

class MarkdownUpdateView(UpdateView):
    model = MarkdownExample
    form_class = MarkDownExampleForm
    template_name = 'app1/markdown_form.html'
    success_url = reverse_lazy('markdown-list')
```

### Admin

In `admin.py`, register your model with the `MarkdownxModelAdmin`:

```python
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MarkdownExample

@admin.register(MarkdownExample)
class MarkdownExampleAdmin(MarkdownxModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
```

### Templates

- **markdown_list.html**

```html
<div class="container">
    <h1>Markdown Examples List</h1>
    <ul>
        {% for example in markdown_example %}
            <li>
                <a href="{{ example.get_absolute_url }}">{{ example.title }}</a>
            </li>
        {% empty %}
            <li>No markdown examples available.</li>
        {% endfor %}
    </ul>
    <a href="{% url 'markdown-create' %}" class="btn btn-primary">Create New Markdown Example</a>
</div>
```

- **markdown_form.html**

```html
<div class="container">
    <h1>{{ view.object.pk|yesno:"Update Markdown Example,Create Markdown Example" }}</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-success">Save</button>
    </form>
    <a href="{% url 'markdown-list' %}" class="btn btn-secondary">Back to List</a>
</div>
```

- **markdown_detail.html**

```html
<div class="container">
    <h1>{{ object.title }}</h1>
    <p>{{ object.formatted_markdown|safe }}</p>
    <a href="{% url 'markdown-update' object.pk %}" class="btn btn-primary">Edit</a>
    <a href="{% url 'markdown-list' %}" class="btn btn-secondary">Back to List</a>
</div>
```

### Code Highlighting

To add code highlighting, install **Pygments**:

```bash
pip install Pygments
```

Generate the CSS file for code highlighting:

```bash
pygmentize -S monokai -f html -a .codehilite > styles.css
```

Place the `styles.css` in the `static/app1/` directory and update your template to include the stylesheet:

```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'app1/styles.css' %}">
```

Finally, add the following to your `settings.py` to enable code highlighting:

```python
MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.codehilite',
]
```

### Finished!

Your MarkdownX setup with code highlighting is complete.
