from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Waters(models.Model):
    name = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=10,decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to="waters_image/",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Waters'

    def __str__(self):
        return super().__str__()


