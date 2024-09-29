from django.views.generic import DetailView, ListView, CreateView, UpdateView
from .models import MarkdownExample
from .forms import MarkDownExampleForm
from django.urls import reverse_lazy


# Detail view for displaying a single MarkdownExample instance
class MarkdownDetailView(DetailView):
    model = MarkdownExample
    template_name = 'app1/markdown_detail.html'


# List view for displaying all MarkdownExample instances
class MarkdownListView(ListView):
    model = MarkdownExample
    template_name = 'app1/markdown_list.html'
    context_object_name = 'markdown_example'


# Create view for adding a new MarkdownExample instance
class MarkdownCreateView(CreateView):
    model = MarkdownExample
    form_class = MarkDownExampleForm
    template_name = 'app1/markdown_form.html'  # Template for the form
    success_url = reverse_lazy('markdown-list')  # Redirect after successful creation


# Update view for editing an existing MarkdownExample instance
class MarkdownUpdateView(UpdateView):
    model = MarkdownExample
    form_class = MarkDownExampleForm
    template_name = 'app1/markdown_form.html'  # Reusing the form template
    success_url = reverse_lazy('markdown-list')  # Redirect after successful update
