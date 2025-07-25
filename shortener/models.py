from django.db import models
from django.contrib.auth.models import User
import string
import random

def generate_short_code():
    """Create a random 10-character code"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

class URL(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short_code
