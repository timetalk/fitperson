import json
from student_management_app.form import AddStudentForm, EditStudentForm
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls.base import reverse
from student_management_app.models import Attendance, AttendanceReport, SchoolName, SessionYearModel, StudentResults, StudentStreem, Students, Subjects
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .models import Courses,FitPersonName, HouseHoldDetail, SchoolName, SessionYearModel, Staffs,  StudentStreem, Students, Subjects, CustomUser
from django.contrib import  messages
from django.urls import reverse


def staff_home(request):
    return render(request, "staff_template/home_content.html")

def staff_take_attendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYearModel.objects.all()

    context = {
        'subjects': subjects,
        'session_years': session_years,
    }

    return render(request, "staff_template/staff_take_attendance.html", context)

@csrf_exempt
def get_student(request):
    subject_id = request.POST.get("subject")
    session_year = request.POST.get("session_year")

    subject = Subjects.objects.get(id=subject_id)
    session_mode = SessionYearModel.objects.get(id=session_year)
    students = Students.objects.filter(course_id=subject.course_id, session_year_id=session_mode)

    list_data = []

    for student in students:
        data_small = {"id":student.admin.id, "name": student.admin.first_name+ " "+student.admin.last_name}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

@csrf_exempt
def save_attendance_data(request):
    student_ids = request.POST.get("student_ids")
    subject_id=request.POST.get("subject_id")
    attendance_date = request.POST.get("attendace_date")
    session_year_id = request.POST.get("session_year_id")

    subject_model = Subjects.objects.get(id=subject_id)
    session_model = SessionYearModel.objects.get(id=session_year_id)
    # print(student_ids)
    json_student = json.loads(student_ids)
    # print(data[0]["id"])

    try:
        attendance=Attendance(subject_id=subject_model, attendance_date=attendance_date,session_year_id=session_model)
        attendance.save()

        for stud in json_student:
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=stud['status'])
            attendance_report.save()
        print(student_ids)
        return HttpResponse("OK")
    except:
        return HttpResponse("ERROR")

@csrf_exempt
def staff_update_attendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYearModel.objects.all()

    context = {
        'subjects': subjects,
        'session_years': session_years,
    }

    return render(request, "staff_template/staff_update_attendance.html", context)

@csrf_exempt
def get_attendance_dates(request):
    subject = request.POST.get("subject")
    session_year_id = request.POST.get("session_year_id")

    subject_obj = Subjects.objects.get(id=subject)
    session_year_obj = SessionYearModel.objects.get(id=session_year_id)
    attendance = Attendance.objects.filter(subject_id=subject_obj, session_year_id=session_year_obj)

    attendance_obj=[]
    for attendace_single in attendance:
        data={"id": attendace_single.id, "attendace_date": str(attendace_single.attendance_date), "session_year_id":session_year_obj.id}
        attendance_obj.append(data)
    return JsonResponse(json.dumps(attendance_obj), safe=False)

@csrf_exempt
def get_attendance_student(request):
    attendance_date = request.POST.get("attendance_date")
  
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance)
    print(attendance_data)


    list_data = []
    for student in attendance_data:
        data_small = {"id": student.student_id.admin.id, "name":student.student_id.admin.first_name+ " " +student.student_id.admin.last_name, "status":student.status}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def save_updateattendance_data(request):
    student_ids = request.POST.get("student_ids")
    attendance_date = request.POST.get("attendance_date")
    print(attendance_date)
    attendance = Attendance.objects.get(id=attendance_date)


    json_student = json.loads(student_ids)


    try:
        for stud in json_student:
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport.objects.get(student_id=student, attendance_id=attendance.id)
            attendance_report.status=stud['status']
            attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("ERROR") 

def staff_add_result(request):
    subjects=Subjects.objects.filter(staff_id=request.user.id)
    session_years=SessionYearModel.objects.all()
    context={
        "subjects":subjects,
        "session_years":session_years,
    }
    return render(request, "staff_template/staff_add_result.html", context)


def save_student_result(request):
    if request.method != 'POST':
        return HttpResponseRedirect('staff_add_result')
    student_admin_id = request.POST.get('student_list')
    assignment_marks = request.POST.get('assignment_marks')
    examination_marks = request.POST.get('examination_marks')
    subject_id = request.POST.get('subject')
    student_obj = Students.objects.get(admin=student_admin_id)
    subject_obj = Subjects.objects.get(id=subject_id)
    try:
        check_exist = StudentResults.objects.filter(subject_id=subject_obj, student_id=student_obj).exists()
        print(check_exist)
        if  check_exist:
            result = StudentResults.objects.get(subject_id=subject_obj, student_id=student_obj)
            result.subject_assignment_marks=assignment_marks
            result.subject_exam_marks=examination_marks
            result.save()
            messages.success(request, f"Successfully Updated {student_obj.admin.first_name}  {student_obj.admin.last_name }'s Results")
            return HttpResponseRedirect(reverse('staff_add_result'))
        else:
            result = StudentResults(student_id=student_obj, subject_id=subject_obj,subject_assignment_marks=assignment_marks, subject_exam_marks=examination_marks)
            result.save()
            messages.success(request, f"Successfully added {student_obj.admin.first_name}  {student_obj.admin.last_name }'s Results")
            return HttpResponseRedirect(reverse('staff_add_result'))

    except:
        messages.error(request, "Error in Added Results")
        return HttpResponseRedirect(reverse('staff_add_result'))


def staff_views_result(request,  streem_id):
    student_names = Students.objects.filter(school_id__school_name__iexact="mwanakianga", streem_id=streem_id)
    context = {
        "student_names": student_names
    }
    return render(request, "staff_template/staff_views_result.html", context)

def staff_views_streem(request):
    streem_names = StudentStreem.objects.all()
    context = {
        "streem_names": streem_names
    }
    return render(request, "staff_template/staff_streem_template.html", context)\

def add_student(request):
    # courses = Courses.objects.all()
    form=AddStudentForm()
    context = {
        # "courses": courses
        "form":form

    }
    return render(request, "staff_template/add_student_template.html", context) 


def staff_add_student(request):
    # courses = Courses.objects.all()
    form=AddStudentForm()
    context = {
        # "courses": courses
        "form":form

    }
    return render(request, "staff_template/add_student_template.html", context) 

def staff_add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]

            school_name = form.cleaned_data["school_name"]
            class_name= form.cleaned_data["class_name"]
            fit_person_name = form.cleaned_data["fit_person_name"]
            father_house_name = form.cleaned_data["father_house_name"]

            gender = form.cleaned_data["sex"]
            course_id = form.cleaned_data["course"]
        

            session_year_id = form.cleaned_data["session_year_id"]

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            course_obj = Courses.objects.get(id=course_id)
                
            try:
                user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, user_type=3)
                user.students.course_id = course_obj
                user.students.address = address
                user.students.gender = gender
                session_year = SessionYearModel.objects.get(id=session_year_id)
                user.students.session_year_id = session_year
                user.students.profile_pic = profile_pic_url

                school_obj = SchoolName.objects.get(id=school_name)
                user.students.school_id = school_obj

                class_obj = StudentStreem.objects.get(id=class_name)
                user.students.class_form_id = class_obj

                fit_person_obj = FitPersonName.objects.get(id=fit_person_name)
                user.students.fit_person_id = fit_person_obj

                household_obj = HouseHoldDetail.objects.get(id=father_house_name)
                user.students.household_id = household_obj


                user.save()
                messages.success(request, "Successfull Added Student")
                return HttpResponseRedirect(reverse("staff_add_student"))
            except:
                messages.error(request, "Error occur please try again")
                return HttpResponseRedirect(reverse("staff_add_student"))
        else:
            form = AddStudentForm()
            context = {
                "form":form
            }
            return render(request, "staff_template/add_student_template.html", context) 



def staff_edit_student(request, student_id):
    request.session['student_id']=student_id
    student = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()
    form = EditStudentForm()
    form.fields['email'].initial = student.admin.email
    form.fields['username'].initial = student.admin.username
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['address'].initial = student.address
    form.fields['sex'].initial = student.gender
    form.fields['course'].initial = student.course_id.id
    form.fields['session_year_id'].initial = student.session_year_id
    form.fields["school_name"].initial = student.school_id
    form.fields["fit_person_name"].initial = student.fit_person_id
    form.fields["class_name"].initial = student.streem_id
    form.fields["father_house_name"].initial = student.household_id

    context = {
        "student": student,
        "courses": courses,
        "id": student_id,
        "form":form

    }
    return render(request, 'staff_template/edit_student_template.html', context)

def staff_edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse("<h1>Invalid method</h1>")
    else:
        student_id = request.session.get("student_id")
        print(student_id)
        if student_id == None:
            return HttpResponseRedirect(reverse("manage_student"))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]

            gender = form.cleaned_data["sex"]
            course_id = form.cleaned_data["course"]

            school_name = form.cleaned_data["school_name"]
            class_name= form.cleaned_data["class_name"]
            fit_person_name = form.cleaned_data["fit_person_name"]
            father_house_name = form.cleaned_data["father_house_name"]
        

            session_year_id = form.cleaned_data["session_year_id"]
          

            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            course_obj = Courses.objects.get(id=course_id)
            

            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            try:
                students = Students.objects.get(admin=student_id)
                students.course_id = course_obj
                students.address = address
                students.gender = gender

                session_year = SessionYearModel.objects.get(id=session_year_id)
                students.session_year_id = session_year

                school_obj = SchoolName.objects.get(id=school_name)
                students.school_id = school_obj

                class_obj = StudentStreem.objects.get(id=class_name)
                students.streem_id = class_obj

                fit_person_obj = FitPersonName.objects.get(id=fit_person_name)
                students.fit_person_id = fit_person_obj

                household_obj = HouseHoldDetail.objects.get(id=father_house_name)
                students.household_id = household_obj

                if profile_pic_url != None:
                    students.profile_pic = profile_pic_url
                students.save()

                del request.session["student_id"]
                messages.success(request, "Successfull Edit Student")
                return HttpResponseRedirect(reverse("staff_edit_student", kwargs={"student_id":student_id}))
            except:
                messages.error(request, "Error occur please try again")
                return HttpResponseRedirect(reverse("staff_edit_student",kwargs={"student_id":student_id} ))
        else:
            form = EditStudentForm(request.POST)
            context = {
                "form":form
            }
            return render(request, "staff_template/edit_student_template.html", context)

def staff_manage_students(request):
    school_name = SchoolName.objects.all()
    context={
        "schools": school_name
    }
    return render(request, 'staff_template/school_list_student.html', context) 



def staff_school_list_student(request, school_id):
    students = Students.objects.filter(school_id__school_name=school_id)
    print(students)
    school_name = SchoolName.objects.get(school_name=school_id)
    context = {
        "students": students,
        "schools": school_name
    }
    return render(request, 'staff_template/manage_student_template.html', context)