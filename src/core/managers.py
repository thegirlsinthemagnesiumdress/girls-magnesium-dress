from django.db import models


class NotExcludedFromBestPracticeManager(models.Manager):
    def get_queryset(self):
        return super(NotExcludedFromBestPracticeManager, self).get_queryset().filter(excluded_from_best_practice=False)
