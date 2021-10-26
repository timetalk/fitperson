from django.http.response import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self, request, view_func, view_args, veiw_kwargs):
        modulename = view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews" or modulename == "django.views.static":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("home_admin"))
         
            elif user.user_type == "2":
                if modulename == "student_management_app.StaffViews":
                    pass
                elif modulename == "student_management_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            
            elif user.user_type == "3":
                if modulename == "student_management_app.StudentViews" or modulename == "django.views.static":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            
            elif user.user_type == "5":
                if modulename == "student_management_app.DeoViews" or modulename == "django.views.static":
                    pass
                elif modulename == "student_management_app.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("deo_home"))
                    
            else:
                return HttpResponseRedirect(reverse("show_login"))

                
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login"):
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))
