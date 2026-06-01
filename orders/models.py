from django.db import models

class OrderStatus(models.TextChoices):
    PENDING = ("pending", "در انتظار")
    COOKING = ("cooking", "در حال آماده‌سازی")
    DELIVERING = ("delivering", "در راه تحویل")
    DELIVERED = ("delivered", "تحویل داده شده")
    
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ سفارش")
    order_status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING,verbose_name="وضعیت سفارش")
    customer = models.ForeignKey("accounts.CustomUser", verbose_name="مشتری", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "سفارش"    
        verbose_name_plural = "سفارش"

    def __str__(self):
        return f"{self.customer} - {self.order_status}"
    
class OrderItem(models.Model):
    food = models.ForeignKey("menu.Food", verbose_name="غذا", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey("Order", verbose_name="سفارش", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "آیتم سفارش"
        verbose_name_plural = "آیتم سفارش"

    def __str__(self):
        return f"{self.food} - {self.quantity}"