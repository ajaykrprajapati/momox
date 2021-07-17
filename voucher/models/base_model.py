from django.db import models


class BaseModel(models):
    class Meta:
        abstract = True
