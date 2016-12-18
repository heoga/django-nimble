from django.contrib.auth.models import User
from django.db import models
from polymorphic.models import PolymorphicModel


class Story(PolymorphicModel):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def name(self):
        return '{}{:0>5}'.format(self.ident, self.id)
