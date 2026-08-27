from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.db.models import Count, Q
from datetime import datetime, timedelta
from accounts.models import CustomUser
from dashboard.models import ContactMessage, CVSubmission
from .models import AdminNotification

@staff_member_required
def admin_dashboard_view(request):
    """لوحة تحكم المشرف الرئيسية"""
    
    # إحصائيات المستخدمين
    total_users = CustomUser.objects.count()
    new_users_today = CustomUser.objects.filter(
        date_joined__date=datetime.now().date()
    ).count()
    
    # إحصائيات الرسائل
    total_messages = ContactMessage.objects.count()
    unread_messages = ContactMessage.objects.filter(is_read=False).count()
    
    # إحصائيات السير الذاتية
    total_cvs = CVSubmission.objects.count()
    pending_cvs = CVSubmission.objects.filter(status='pending').count()
    approved_cvs = CVSubmission.objects.filter(status='approved').count()
    rejected_cvs = CVSubmission.objects.filter(status='rejected').count()
    
    # آخر 5 رسائل
    recent_messages = ContactMessage.objects.all().order_by('-created_at')[:5]
    
    # آخر 5 طلبات CV
    recent_cvs = CVSubmission.objects.all().order_by('-submitted_at')[:5]
    
    # آخر 5 مستخدمين جدد
    recent_users = CustomUser.objects.all().order_by('-date_joined')[:5]
    
    # إشعارات غير مقروءة
    notifications = AdminNotification.objects.filter(is_read=False)[:10]
    
    context = {
        'total_users': total_users,
        'new_users_today': new_users_today,
        'total_messages': total_messages,
        'unread_messages': unread_messages,
        'total_cvs': total_cvs,
        'pending_cvs': pending_cvs,
        'approved_cvs': approved_cvs,
        'rejected_cvs': rejected_cvs,
        'recent_messages': recent_messages,
        'recent_cvs': recent_cvs,
        'recent_users': recent_users,
        'notifications': notifications,
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)

@staff_member_required
def admin_users_view(request):
    """عرض جميع المستخدمين"""
    users = CustomUser.objects.all().order_by('-date_joined')
    return render(request, 'admin_dashboard/users.html', {'users': users})

@staff_member_required
def admin_messages_view(request):
    """عرض جميع الرسائل"""
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'admin_dashboard/messages.html', {'messages': messages_list})

@staff_member_required
def admin_cvs_view(request):
    """عرض جميع السير الذاتية"""
    cvs = CVSubmission.objects.all().order_by('-submitted_at')
    return render(request, 'admin_dashboard/cvs.html', {'cvs': cvs})

@staff_member_required
def mark_notification_read(request, notification_id):
    """تحديد إشعار كمقروء"""
    try:
        notification = AdminNotification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
    except:
        pass
    return redirect('admin_dashboard:dashboard')