from django.urls import path
from .views import MarkdownListView, MarkdownDetailView, MarkdownCreateView, MarkdownUpdateView


urlpatterns = [
    # List view: shows all MarkdownExample instances
    path('', MarkdownListView.as_view(), name='markdown-list'),

    # Detail view: shows a single MarkdownExample instance by its primary key (pk)
    path('<int:pk>/', MarkdownDetailView.as_view(), name='markdown-detail'),

    # Create view: allows the creation of a new MarkdownExample
    path('create/', MarkdownCreateView.as_view(), name='markdown-create'),

    # Update view: allows the updating of an existing MarkdownExample by its pk
    path('<int:pk>/update/', MarkdownUpdateView.as_view(), name='markdown-update'),
]
