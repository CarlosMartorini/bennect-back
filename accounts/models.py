from django.db import models
from uuid import uuid4


def upload_perfil_image(instance, filename):
    return f'{instance.username}_{filename}'


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True, null=False)
    cpf = models.CharField(max_length=11, unique=True, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    cep = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    number = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    state = models.CharField(max_length=255, null=False)
    perfil_image = models.ImageField(upload_to=upload_perfil_image, blank=True, null=True)
