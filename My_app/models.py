from django.db import models

# Create your models here.


class Author(models.Model):
   name=models.CharField(max_length=200,null=True)

   def __str__(self):
       return '{}'.format(self.name)

class Book(models.Model):
    title = models.CharField(max_length=200,null=True)

    price = models.IntegerField(null=True)
    image = models.ImageField(upload_to='book_media')


    author =models.ForeignKey(Author,on_delete=models.CASCADE,default=1)



    def __str__(self):
        return '{}'.format(self.title)
class UserProfile(models.Model):
    username= models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)
class loginTable(models.Model):
    objects = None
    username= models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    def __str__(self):
        return '{}'.format(self.username)

