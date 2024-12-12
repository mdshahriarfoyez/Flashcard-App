from django.db import models
from django.contrib.auth.models import User

class FlashcardSet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Flashcard(models.Model):
    set = models.ForeignKey(FlashcardSet, related_name="cards", on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField()
    is_hidden = models.BooleanField(default=False)

class Rating(models.Model):
    set = models.ForeignKey(FlashcardSet, related_name="ratings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)

    class Meta:
        unique_together = ('set', 'user')
