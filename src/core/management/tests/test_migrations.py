# coding=utf-8

from core.management.migrations import import_dmb_lite, INDUSTRY_MAP
from djangae.test import TestCase
from django.conf import settings
from os.path import join
from core.tests.mommy_recepies import make_user


from core.models import User, Survey


class TestDMBLiteImport(TestCase):

    def setUp(self):
        make_user(email='bbelcastro@google.com')
        self.filename = join(settings.BASE_DIR, "core/management/tests/csv_mock_dmblite.csv")
        import_dmb_lite(self.filename)

    def test_it_creates_users(self):
        users = set([
            u'thorntonm@google.com',
            u'pchillari@google.com',
            u'pchillari@google.com',
            u'agatap@google.com',
            u'bbelcastro@google.com',
        ])

        self.assertEqual(User.objects.all().count(), 4)
        saved_users = set([u.email for u in User.objects.all()])
        self.assertEqual(saved_users, users)

    def test_it_creates_accounts(self):

        accounts = set([
            u'Bell',
            u'Bell',
            u'šai',
            u'IPF Provident',

        ])
        self.assertEqual(Survey.objects.all().count(), 4)

        saved_accounts = set([a.company_name for a in Survey.objects.all()])
        self.assertEqual(saved_accounts, accounts)

    def test_it_adds_survey_to_user(self):
        user = User.objects.filter(email="pchillari@google.com")[0]
        self.assertEqual(user.accounts.count(), 2)

    def test_it_sets_creator_and_date_if_older(self):
        user = User.objects.filter(email="pchillari@google.com")[0]
        surveys_queryset = Survey.objects.filter(company_name="Bell", country="IT")
        self.assertEqual(surveys_queryset.count(), 1)

        self.assertEqual(surveys_queryset[0].creator, user)

    def test_it_sets_is_an_imported_account(self):
        for s in Survey.objects.all():
            self.assertTrue(s.imported_from_dmb_lite)

    def test_it_creates_users_not_again(self):
        users = set([
            u'thorntonm@google.com',
            u'pchillari@google.com',
            u'pchillari@google.com',
            u'agatap@google.com',
            u'bbelcastro@google.com',
        ])
        import_dmb_lite(self.filename)
        self.assertEqual(User.objects.all().count(), 4)
        saved_users = set([u.email for u in User.objects.all()])
        self.assertEqual(saved_users, users)

    def test_it_creates_accounts_not_again(self):
        import_dmb_lite(self.filename)
        accounts = set([
            u'Bell',
            u'Bell',
            u'šai',
            u'IPF Provident',

        ])
        self.assertEqual(Survey.objects.all().count(), 4)

        saved_accounts = set([a.company_name for a in Survey.objects.all()])
        self.assertEqual(saved_accounts, accounts)

    def test_it_adds_survey_to_user_not_again(self):
        import_dmb_lite(self.filename)
        user = User.objects.filter(email="pchillari@google.com")[0]
        self.assertEqual(user.accounts.count(), 2)

    def test_industry_in_mapping_exist(self):
        INDUSTRIES = settings.TENANTS['ads']['INDUSTRIES']

        for i in INDUSTRY_MAP.values():
            self.assertIsNotNone(INDUSTRIES.get(i, None))

    def test_industry_is_mapped(self):
        INDUSTRIES = settings.TENANTS['ads']['INDUSTRIES']

        for i in INDUSTRY_MAP.values():
            self.assertIsNotNone(INDUSTRIES.get(i, None))
