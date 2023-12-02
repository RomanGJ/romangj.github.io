from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='carusel_img')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.name


