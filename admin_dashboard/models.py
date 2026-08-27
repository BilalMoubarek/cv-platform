from django.db import models
from django.conf import settings

class AdminNotification(models.Model):
    NOTIFICATION_TYPES = [
        ('new_user', 'مستخدم جديد'),
        ('new_cv', 'سيرة ذاتية جديدة'),
        ('new_message', 'رسالة جديدة'),
        ('system', 'نظام'),
    ]
    
    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.get_type_display()}: {self.message[:50]}"