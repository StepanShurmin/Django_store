from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home_page, contacts, category, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/product/', product, name='product'),

]