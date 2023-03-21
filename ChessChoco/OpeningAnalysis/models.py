from django.db import models

class ChessOpening(models.Model):
    name = models.CharField(max_length=200)
    moves = models.TextField(null=True)
    description = models.TextField()
    variation = models.TextField(default='없음')
