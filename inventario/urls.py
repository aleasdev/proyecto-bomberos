from django.urls import path
from .views import BlogDetailView, BlogCreateView, BlogEditView, BlogDeleteView, ListInv

urlpatterns = [
    path("", ListInv.as_view(), name="informacion"),
    path("<int:pk>/", BlogDetailView.as_view(), name="bombero_detail"),
    path("new/", BlogCreateView.as_view(), name="bombero_new"),
    path("<int:pk>/edit/", BlogEditView.as_view(), name="bombero_edit"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="bombero_delete"),
]   