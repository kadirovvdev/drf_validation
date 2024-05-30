from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)


    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username

