from __future__ import unicode_literals

import uuid


from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
from django.db import models

import uuid

from django.db import models


class CreateUpdateModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(verbose_name='criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='atualizado em', auto_now=True)

    class Meta:
        abstract = True


#usuarios
class UUIDUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    groups = models.ManyToManyField(Group, blank=True, related_name="uuiduser_set", related_query_name="user")
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name="uuiduser_set", related_query_name="user")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

# Create your models here.
class Forum(CreateUpdateModel):
    assunto = models.CharField(max_length=200, null=True)
    descricao = models.TextField(verbose_name='descricao')

class Respostas(CreateUpdateModel):
    user = models.ForeignKey(UUIDUser, related_query_name="user", on_delete=models.CASCADE )
    mensagens = models.TextField(verbose_name='mensagens')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name='forum')


class Arts(CreateUpdateModel):
    descricao = models.TextField(null=True, blank=True, default=None)
    titulo = models.CharField(max_length=200)
    anime = models.CharField(max_length=400)
    foto = models.ImageField(verbose_name='foto', upload_to='midia/%Y/%m/%d')
    





class Anime(CreateUpdateModel):
    nome = models.CharField(max_length=300)
    ep = models.IntegerField(verbose_name='episodio')
    descricao = models.TextField(verbose_name='sinopse')