from django.shortcuts import render, redirect

def home_view(request):
    # Show admin button only if user is admin (is_staff=True)
    show_admin = False
    if request.user.is_authenticated and request.user.is_staff:
        show_admin = True
    
    return render(request, 'core/home.html', {'show_admin': show_admin})

def hide_admin_view(request):
    return redirect('core:home')