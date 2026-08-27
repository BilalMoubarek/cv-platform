from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContactMessage, CVSubmission
from .forms import ContactForm, CVSubmissionForm

def contact_view(request):
    """صفحة نموذج التواصل"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إرسال رسالتك بنجاح! سنتواصل معك قريباً.")
            return redirect('core:home')
    else:
        form = ContactForm()
    return render(request, 'dashboard/contact.html', {'form': form})

@login_required
def submit_cv_view(request):
    """صفحة رفع السيرة الذاتية"""
    if request.method == 'POST':
        form = CVSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.user = request.user
            cv.email = request.user.email
            cv.full_name = f"{request.user.first_name} {request.user.last_name}"
            cv.save()
            messages.success(request, "✅ تم رفع السيرة الذاتية بنجاح! في انتظار المراجعة.")
            return redirect('dashboard:my_submissions')
    else:
        form = CVSubmissionForm()
    return render(request, 'dashboard/submit_cv.html', {'form': form})

@login_required
def my_submissions_view(request):
    """عرض جميع طلبات المستخدم"""
    submissions = CVSubmission.objects.filter(user=request.user).order_by('-submitted_at')
    return render(request, 'dashboard/my_submissions.html', {'submissions': submissions})

@login_required
def dashboard_home_view(request):
    """لوحة التحكم الرئيسية"""
    user = request.user
    submissions = CVSubmission.objects.filter(user=user)
    total_submissions = submissions.count()
    pending = submissions.filter(status='pending').count()
    approved = submissions.filter(status='approved').count()
    rejected = submissions.filter(status='rejected').count()
    
    context = {
        'total_submissions': total_submissions,
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
    }
    return render(request, 'dashboard/dashboard_home.html', context)