from django.db import models
import random
import os

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/pictures/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

class ProductManager(models.Manager):
    def get_by_id(self,id):
        qs=self.get_qureyset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None

class Product(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    image           = models.ImageField(upload_to='products/pictures/',null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

