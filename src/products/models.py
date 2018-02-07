import random
import os
from django.db import models

def get_filename_ext(filepath):
    print(filepath)
    base_name = os.path.basename(filepath)
    print(base_name)
    name, ext = os.path.splitext(base_name)
    print(name,ext)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class Product(models.Model):
    title     = models.CharField(max_length=120)
    price     = models.DecimalField(decimal_places=2, max_digits=120, default= 40.00)
    description = models.TextField()
    image      = models.ImageField(upload_to='products/pictures/', null=False, blank= False)

    def __str__(self):
        return self.title


