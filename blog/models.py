from django.db import models

class bugatti(models.Model):
    name = models.TextField(max_length=100,null=True)
    price = models.TextField(max_length=100, null=True)
    desc = models.TextField(null=True)
    img = models.TextField(null=True)
    img1 = models.TextField(null=True)
    img2 = models.TextField(null=True)
    img3 = models.TextField(null=True)
    img4 = models.TextField(null=True)

class koenigsegg(models.Model):
    name = models.TextField(max_length=100, null=True)
    price = models.TextField(max_length=100, null=True)
    desc = models.TextField(null=True)
    img = models.TextField(null=True)
    img1 = models.TextField(null=True)
    img2 = models.TextField(null=True)
    img3 = models.TextField(null=True)
    img4 = models.TextField(null=True)



