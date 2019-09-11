from django.db import models
from search.django.adapters import SearchQueryAdapter


class NotExcludedFromBestPracticeManager(models.Manager):
    def get_queryset(self):
        return super(NotExcludedFromBestPracticeManager, self).get_queryset().filter(excluded_from_best_practice=False)


class AccountQuerySet(models.QuerySet):

    # def for_user(self, user_email):
    #     return self.filter(models.Q(is_private=False) |
    #                        models.Q(emails_shared_with__contains=user_email))

    def search(self, term):
        # The default implementation of the `search` queryset method from the
        # search library doesn't use the `corpus` field to search against, but
        # that's what we want to do
        qset = SearchQueryAdapter.from_queryset(self)
        qset = qset.filter(corpus=term)
        # `as_django_queryset` returns the queryset and the IDs of the documents
        # in their original order, but we have no need for those in this case
        queryset, doc_pks = qset.as_django_queryset()
        return queryset


class AccountManager(models.Manager):

    def get_queryset(self):
        return AccountQuerySet(self.model, using=self._db)

    # def for_user(self, user_email):
    #     return self.get_queryset().for_user(user_email=user_email)

    def search(self, term):
        return self.get_queryset().search(term)
