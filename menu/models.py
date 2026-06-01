from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='اسم')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی"

class Food(models.Model):
    name = models.CharField(max_length=100,verbose_name='اسم')
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(default=0, verbose_name="قیمت")
    image = models.ImageField(upload_to="images", blank=True)
    category = models.ForeignKey("Category", verbose_name="دسته بندی", on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True, verbose_name="موجود بودن")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذا"