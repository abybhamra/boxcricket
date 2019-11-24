from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase
from boxcricket.models import Team, Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game.objects.create(date=datetime.now())

    def test_team_with_valid_values(self):
        Team.objects.create(game=self.game, name="India", captain="Virat Kohli")
        team = Team.objects.all()

        self.assertEqual(len(team), 1)

    def test_team_with_a_string_type_game_raises_value_error(self):
        with self.assertRaises(ValueError) as error:
            Team.objects.create(game="game", name="India", captain="Virat Kohli")

        self.assertIn("Cannot assign", str(error.exception))

    def test_game_raises_integrity_error_with_a_repeat_entry(self):
        with self.assertRaises(IntegrityError) as error:
            Team.objects.create(game=self.game, name="India", captain="Virat Kohli")
            Team.objects.create(game=self.game, name="India", captain="Virat Kohli")

        self.assertEqual("UNIQUE constraint failed: boxcricket_team.captain", str(error.exception))
