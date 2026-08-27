from django.contrib import admin
from .models import ContactMessage, CVSubmission

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"✅ {queryset.count()} رسالة تم تحديثها كـ مقروءة")
    mark_as_read.short_description = "📖 تحديد كمقروءة"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
        self.message_user(request, f"🔄 {queryset.count()} رسالة تم تحديثها كـ غير مقروءة")
    mark_as_unread.short_description = "📩 تحديد كغير مقروءة"
    
    fieldsets = (
        ('📩 معلومات الرسالة', {
            'fields': ('name', 'email', 'subject', 'message', 'created_at')
        }),
        ('📊 الحالة', {
            'fields': ('is_read',)
        }),
    )

@admin.register(CVSubmission)
class CVSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'status', 'submitted_at']
    list_filter = ['status', 'submitted_at']
    search_fields = ['full_name', 'email', 'phone']
    readonly_fields = ['full_name', 'email', 'phone', 'cv_file', 'message', 'submitted_at']
    actions = ['approve_submissions', 'reject_submissions']
    
    def approve_submissions(self, request, queryset):
        for submission in queryset:
            submission.approve()
        self.message_user(request, f"✅ {queryset.count()} طلب تمت الموافقة عليه")
    approve_submissions.short_description = "✅ الموافقة على الطلبات المحددة"
    
    def reject_submissions(self, request, queryset):
        for submission in queryset:
            submission.reject()
        self.message_user(request, f"❌ {queryset.count()} طلب تم رفضه")
    reject_submissions.short_description = "❌ رفض الطلبات المحددة"
    
    fieldsets = (
        ('👤 معلومات مقدم الطلب', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('📄 السيرة الذاتية', {
            'fields': ('cv_file', 'message', 'submitted_at')
        }),
        ('📊 الحالة', {
            'fields': ('status', 'admin_notes')
        }),
    )