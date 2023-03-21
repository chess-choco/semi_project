from django.db import models

class ChessOpening(models.Model):
    name = models.CharField(max_length=200)
    moves = models.TextField(null=True)
    description = models.TextField()

    def num_variations(self):
        return self.variations.count()

    def __str__(self):
        return self.name

class ChessVariation(models.Model):
    opening = models.ForeignKey(ChessOpening, on_delete=models.CASCADE, related_name='variations')
    name = models.CharField(max_length=200, null=True, blank=True)
    moves = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name # or f"Variation {self.pk}"
