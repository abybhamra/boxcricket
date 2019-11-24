import datetime

from django.test import TestCase

from boxcricket.forms import GameForm


class TestGameForm(TestCase):
    def test_new_form_date_field_label_is_none(self):
        form = GameForm()
        self.assertFalse(form.fields['date'].label)

    def test_new_form_date_in_past_return_a_valid_form(self):
        date = datetime.date.today() - datetime.timedelta(days=1)
        form = GameForm(data={'date': date})
        self.assertTrue(form.is_valid())

    def test_new_form_date_too_far_in_future_return_a_valid_form(self):
        date = datetime.date.today() + datetime.timedelta(weeks=4) + datetime.timedelta(days=1)
        form = GameForm(data={'date': date})
        self.assertTrue(form.is_valid())

    def test_new_form_date_today_return_a_valid_form(self):
        date = datetime.date.today()
        form = GameForm(data={'date': date})
        self.assertTrue(form.is_valid())
