from distutils.command.upload import upload
from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):

    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(BaseModel):

    image = models.ImageField(upload_to='products')
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class ProductSale(BaseModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_of_sale = models.DateField()
