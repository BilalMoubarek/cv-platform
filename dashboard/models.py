from django.db import models
from django.conf import settings

class ContactMessage(models.Model):
    """نموذج الرسائل من الزوار"""
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="الإيميل")
    subject = models.CharField(max_length=200, verbose_name="الموضوع")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")
    is_read = models.BooleanField(default=False, verbose_name="مقروءة")
    
    class Meta:
        verbose_name = "رسالة"
        verbose_name_plural = "الرسائل"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class CVSubmission(models.Model):
    """نموذج رفع السيرة الذاتية"""
    STATUS_CHOICES = [
        ('pending', 'في انتظار المراجعة'),
        ('approved', 'تم الموافقة'),
        ('rejected', 'مرفوض'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cv_submissions')
    full_name = models.CharField(max_length=200, verbose_name="الاسم الكامل")
    email = models.EmailField(verbose_name="الإيميل")
    phone = models.CharField(max_length=20, verbose_name="رقم الهاتف")
    cv_file = models.FileField(upload_to='cvs/', verbose_name="السيرة الذاتية (PDF)")
    message = models.TextField(blank=True, null=True, verbose_name="رسالة إضافية")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="الحالة")
    submitted_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")
    reviewed_at = models.DateTimeField(blank=True, null=True, verbose_name="تاريخ المراجعة")
    admin_notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات المشرف")
    
    class Meta:
        verbose_name = "سيرة ذاتية"
        verbose_name_plural = "السير الذاتية"
        ordering = ['-submitted_at']
    
    def __str__(self):
        return f"{self.full_name} - {self.status}"
    
    def approve(self):
        self.status = 'approved'
        self.reviewed_at = models.DateTimeField(auto_now=True)
        self.save()
    
    def reject(self):
        self.status = 'rejected'
        self.reviewed_at = models.DateTimeField(auto_now=True)
        self.save()