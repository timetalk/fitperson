from django.shortcuts import render

def school_admin_views(request):
    return render(request, 'school_admin_template/home_content.html')