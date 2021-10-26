from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from student_management_app.views import (
    showDemo,
    ShowLogin,
    doLogin,
    getuserDetails,
    logout_user
)
from student_management_app.HodViews import (
    admin_home,
    add_staff,
    add_staff_save,
    add_course,
    add_course_save,
    add_student,
    add_student_save,
    add_subject_save,
    add_subject,
    manage_course,
    manage_staffs,
    manage_students,
    manage_subjects,
    edit_staff,
    edit_student,
    edit_course,
    edit_subject,
    edit_staff_save,
    edit_student_save,
    edit_course_save,
    edit_subject_save,
    manage_session,
    manage_session_save,
    add_school_name,
    add_school_name_save,
    school_list,
    fit_person,
    fit_person_save,
    class_streem,
    house_hold,
    house_hold_save,
    class_streem_save,
    school_list_student,
    add_deo,
    add_deo_save,
    manage_deo,

)

from student_management_app.StaffViews import (
    staff_home, 
    staff_take_attendance,
    get_student,
    save_attendance_data,
    staff_update_attendance,
    get_attendance_dates,
    get_attendance_student,
    save_updateattendance_data,
    staff_add_result,
    save_student_result,
    staff_views_result,
    staff_views_streem,
    staff_add_student,
    staff_add_student_save,
    staff_edit_student_save,
    staff_edit_student,
    staff_manage_students,
    staff_school_list_student,
)

from student_management_app.StudentViews import(
    student_home,
    student_view_attendance,
    student_view_attendance_save,  
    
)

from student_management_app.DeoViews import (
    deo_home,
    deo_school_detail,
    show_staffs,
    show_students,
    classes_streem,
    manage_all_staff,
    manage_all_student,
  
    
)


from student_management_app.SchoolAdminViews import (
    school_admin_views,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', showDemo),                               
    path('', ShowLogin, name="show_login"),
    path('doLogin', doLogin, name='do_login'),
    path('get_user_details', getuserDetails),
    path('logout', logout_user, name='logout'),
    path('home_admin', admin_home, name="home_admin"),
    path('add_staff', add_staff, name='add_staff'),
    path('add_staff_save', add_staff_save, name='add_staff_save'),
    path('add_course', add_course, name='add_course'),
    path('add_course_save', add_course_save, name='add_course_save'),
    path('add_student', add_student, name='add_student'),
    path('add_student_save', add_student_save, name='add_student_save'),
    path('add_subject', add_subject, name='add_subject'),
    path('add_subject_save', add_subject_save, name='add_subject_save'),
    path('manage_courses', manage_course, name='manage_course'),
    path('manage_subjects', manage_subjects, name='manage_subjects'),
    path('manage_students', manage_students, name='manage_students'),
    path('manage_staffs', manage_staffs, name='manage_staffs'),
    path('edit_staff/<int:staff_id>', edit_staff, name='edit_staff'),
    path('edit_course/<str:course_id>', edit_course, name='edit_course'),
    path('edit_course_save', edit_course_save, name='edit_course_save'),
    path('edit_student/<str:student_id>', edit_student, name='edit_student'),
    path('edit_subject/<str:subject_id>', edit_subject, name='edit_subject'),
    path('edit_subject_save', edit_subject_save, name='edit_subject_save'),
    path('edit_staff_save/', edit_staff_save, name='edit_staff_save'),
    path('edit_student/<int:student_id>', edit_student, name='edit_student'),
    path('edit_student_save', edit_student_save, name='edit_student_save'),
    path('manage_session', manage_session, name='manage_session'),
    path('manage_session_save', manage_session_save, name='manage_session_save'),
    path('add_school_name', add_school_name, name='add_school_name'),    
    path('add_school_name_save', add_school_name_save, name='add_school_name_save'),
    path('school_list/<str:school_id>', school_list, name='school_list'),
    path('fit_person', fit_person, name='fit_person'),
    path('fit_person_save', fit_person_save, name='fit_person_save'),
    path('class_streem', class_streem, name='class_streem'),
    path('house_hold', house_hold, name='house_hold'),
    path('house_hold_save', house_hold_save, name='house_hold_save'),
    path('class_streem_save', class_streem_save, name='class_streem_save'),
    path('school_list_student/<str:school_id>', school_list_student, name='school_list_student'),
    path('add_deo', add_deo, name='add_deo'),    
    path('add_deo_save', add_deo_save, name='add_deo_save'),
    path('manage_deo', manage_deo, name='manage_deo'),

    #staff issues
    path('staff_home', staff_home, name="staff_home"),
    path('staff_take_attendance', staff_take_attendance, name="staff_take_attendance"),
    path('get_student', get_student, name='get_student'),
    path('save_attendance_data', save_attendance_data, name='save_attendance_data'),
    path('staff_update_attendance', staff_update_attendance, name='staff_update_attendance'),
    path('get_attendance_dates', get_attendance_dates, name='get_attendance_dates'),
    path('get_attendance_student', get_attendance_student, name='get_attendance_student'),
    path('save_updateattendance_data', save_updateattendance_data, name='save_updateattendance_data'),
    path('staff_add_result', staff_add_result, name='staff_add_result'),
    path('save_student_result', save_student_result, name='save_student_result'),
    path('staff_views_result/<str:streem_id>', staff_views_result, name='staff_views_result'),
    path('staff_views_streem', staff_views_streem, name='staff_views_streem'),
    path('staff_add_staff', staff_add_student, name='staff_add_student'),
    path('staff_add_student_save', staff_add_student_save, name='staff_add_student_save'),
    path('staff_edit_staff', staff_edit_student, name='staff_edit_staff'),
    path('staff_edit_staff_save', staff_edit_student_save, name='staff_edit_staff_save'),
    path('staff_manage_students', staff_manage_students, name='staff_manage_students'),
    path('staff_school_list_student/<str:school_id>', staff_school_list_student, name='staff_school_list_student'),
    


    # Student issue
    path('student_home', student_home, name='student_home'),
    path('student_view_attendance', student_view_attendance, name='student_view_attendance'),
    path('student_view_attendance_save', student_view_attendance_save, name='student_view_attendance_save'),

    # Deo admin
    path('deo_home', deo_home, name='deo_home'),
    path('deo_school_detail/<str:school_id>', deo_school_detail, name='deo_school_detail'),
    path('show_staffs/<str:school_id>', show_staffs, name='show_staffs'),
    path('show_students/<str:school_id>/<str:streem_id>', show_students, name='show_students'),
    path('class_streem/<str:school_id>', classes_streem, name='class_streem'),
    path('manage_all_staff', manage_all_staff, name='manage_all_staff'),
    path('manage_all_student', manage_all_student, name='manage_all_student'),

    # School Admin
    path('school_admin_views', school_admin_views, name='school_admin_views'),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
