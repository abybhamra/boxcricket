from django.db import models


class Game(models.Model):
    date = models.DateField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.date

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('game_details', args=[str(self.id)])


class Team(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    captain = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.game, self.name, self.captain


class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    over_number = models.IntegerField()
    bowl_number = models.IntegerField()
    bowler = models.CharField(max_length=50, unique=True, null=False, blank=False)
    bastman = models.CharField(max_length=50, unique=True, null=False, blank=False)
    runs = models.IntegerField()
    wicket = models.IntegerField()

    def __str__(self):
        return self.game, self.over_number, self.bowl_number, self.bowler, self.bastman, self.runs, self.wicket


class MatchScore(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.CharField(max_length=50, unique=True, null=False, blank=False)
    runs_scored = models.IntegerField()
    runs_conceded = models.IntegerField()
    wicket = models.IntegerField()

    def __str__(self):
        return self.game, self.player, self.runs_conceded, self.runs_scored, self.wicket
