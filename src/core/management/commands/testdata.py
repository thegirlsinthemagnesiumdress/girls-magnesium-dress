import os

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from djangae.test import process_task_queues


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('flush')

        search_index_file = os.path.join(settings.BASE_DIR, ".storage/search_indexes")
        if os.path.exists(search_index_file):
            print("Removing search indexes")
            os.remove(search_index_file)

        # Generate test data here

        print("Processing tasks")
        process_task_queues()

        print("Done")
