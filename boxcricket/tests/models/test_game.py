from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase
from datetime import datetime
from boxcricket.models import Game


class TestGame(TestCase):
    def test_game_with_valid_datetime(self):
        Game.objects.create(date=datetime.now())
        game = Game.objects.all()

        self.assertEqual(len(game), 1)

    def test_game_raises_integrity_error_when_none_type_is_provided(self):
        with self.assertRaises(IntegrityError) as error:
            Game.objects.create()

        self.assertEqual("NOT NULL constraint failed: boxcricket_game.date", str(error.exception))

    def test_game_raises_validation_error_when_string_is_provided(self):
        with self.assertRaises(ValidationError) as error:
            Game.objects.create(date="hellothere")
            Game.objects.create(date=123)

        self.assertIn("value has an invalid date format. It must be in YYYY-MM-DD format",
                      str(error.exception))
