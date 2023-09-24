from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import HomeListView, ContactsView, CategoryListView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('<int:pk>/home/', ProductListView.as_view(), name='product'),

]