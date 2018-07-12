import hashlib
import re

from djangae.contrib.gauth_datastore.models import GaeAbstractDatastoreUser
from djangae.fields import JSONField
from django.conf import settings
from django.db import models
from django.utils import timezone
from qualtrics import calculate_benchmark, dimensions


SURVEY_URL = 'https://google.qualtrics.com/jfe/form/SV_beH0HTFtnk4A5rD'


class User(GaeAbstractDatastoreUser):
    pass


class Survey(models.Model):
    """
    DMB_overall_average_by_dimension:
    {
        [category]: benchmark
    }
    """

    company_name = models.CharField(max_length=50)
    uid = models.CharField(unique=True, editable=False, max_length=32)

    # DMB_overall_average = models.DecimalField()

    # DMB_overall_average_by_dimension = JSONField()

    # DMB_best_practice = models.DecimalField()

    # DMB_best_practice_by_dimension = JSONField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def link(self):
        """
        Lint to qualtrics survey. Every company will have a different URL, created
        out of the uid.
        The uid will be stored for every survey response and we will be able to use
        it to match the data against companies.
        """
        return '{}?sid={}'.format(SURVEY_URL, self.uid)

    @property
    def link_sponsor(self):
        """
        We need to differenziate between sponsor (survey creators)
        amd participants. The way that is done is by setting sp=true.
        """
        return '{}&sp=true'.format(self.link)

    def get_dmb_overall_by_dimension(self, dimension):
        self.DMB_overall_average_by_dimension.get(dimension)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
            m = hashlib.md5()
            md5 = m.update(self.company_name + self.created_at.isoformat())
            self.uid = m.hexdigest()
        super(Survey, self).save(*args, **kwargs)


def string_to_number_or_zero(number):
    try:
        return float(number)
    except ValueError:
        return 0


class SurveyResult(models.Model):
    _question_key_regex = re.compile(r'^Q\d+(_\d+)?$')

    survey = models.ForeignKey(Survey)
    sid = models.CharField(max_length=50)
    response_id = models.CharField(max_length=50)
    loaded_at = models.DateTimeField(auto_now_add=True)

    data = JSONField()

    @property
    def questions(self):
        # filter results keys that are questions. Unfortunately we have to rely on property key names.
        questions_keys = filter(self._question_key_regex.search, self.data.keys())

        # filter out questions without a response.
        questions_keys_with_value = filter(lambda key: self.data.get(key), questions_keys)

        def create_tuple(key):
            return (
                key,
                string_to_number_or_zero(self.data.get(key)),
                settings.WEIGHTS.get(key, 1),
                self.get_question_dimension(key)
            )

        questions_key_value = map(create_tuple, questions_keys_with_value)
        return questions_key_value

    def get_question_dimension(self, question_id):
        for dimension_key, dimension_value in settings.DIMENSIONS.iteritems():
            if question_id in dimension_value:
                return dimension_key
