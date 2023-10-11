from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Product, Category

json_file = 'catalog/fixtures/catalog.json'


def delete_objects(model):
    """Чистит БД."""
    model.objects.all().delete()


def load_fixtures():
    """Загружает данные в БД."""
    call_command('loaddata', json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        for obj in [Product, Category]:
            delete_objects(obj)

        load_fixtures()
