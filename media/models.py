from django.db import models
import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(uuid.uuid4()), ext)
    return os.path.join('static/upload/', filename)


class Video(models.Model):
    nome = models.CharField(max_length=100, verbose_name=u'Nome', default='', blank=True)
    arquivo = models.FileField(verbose_name=u"Arquivo", upload_to=get_file_path)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome
