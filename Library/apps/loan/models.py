from django.db import models
from apps.book.models import books
from apps.user.models import users

class loans (models.Model):
    loan_id = models.AutoField(primary_key=True)
    loanDate = models.DateField(auto_now_add=True)
    book = models.ForeignKey(books, null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(users, null=False, blank=False, on_delete=models.CASCADE)