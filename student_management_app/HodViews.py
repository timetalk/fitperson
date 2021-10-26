from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Courses, Deo, FitPersonName, HouseHoldDetail, SchoolName, SessionYearModel, Staffs, StudentStreem, Students, Subjects, CustomUser
from django.contrib import admin, messages
from . form import AddStudentForm, EditStudentForm
from django.urls import reverse

def admin_home(request):
    return render(request, "hod_template/home_content.html") 


def add_staff(request):
    Schools = SchoolName.objects.all()
    context = {
        'schools': Schools
    }
    return render(request, "hod_template/add_staff_template.html", context) 

def add_school_name(request):
    return render(request, "hod_template/add_school_template.html") 

def add_school_name_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        school_name = request.POST.get("school_name")
        try:
            check_exist = SchoolName.objects.filter(school_name=school_name).exists()
            if check_exist:
                messages.error(request, "School exists")
                return HttpResponseRedirect(reverse("add_school_name"))
            else:
                school = SchoolName(school_name=school_name)
                school.save()
                messages.success(request, "Successfull ")
                return HttpResponseRedirect(reverse("add_school_name"))
        except:
            messages.error(request, "Error")
            return HttpResponseRedirect(reverse("add_school_name"))



def add_staff_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        school_id = request.POST.get("school_name")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
      

        school_obj = SchoolName.objects.get(id=school_id)
        print(school_obj)
    

    try:
      
        user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,user_type=2)
        user.staffs.address = address
        user.staffs.school_id = school_obj
        user.save()

   

        

        messages.success(request, "Successfull Added Staff")
        return HttpResponseRedirect(reverse("add_staff"))
    except:
        messages.error(request, "Error occur please try again")
        return HttpResponseRedirect(reverse("add_staff"))


def add_student(request):
    # courses = Courses.objects.all()
    form=AddStudentForm()
    context = {
        # "courses": courses
        "form":form

    }
    return render(request, "hod_template/add_student_template.html", context) 

def add_student_save(request):
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
                return HttpResponseRedirect(reverse("add_student"))
            except:
                messages.error(request, "Error occur please try again")
                return HttpResponseRedirect(reverse("add_student"))
        else:
            form = AddStudentForm()
            context = {
                "form":form
            }
            return render(request, "hod_template/add_student_template.html", context) 

def add_course(request):
    return render(request, "hod_template/add_course_template.html") 

def add_course_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        course_name = request.POST.get("course")

        try:
            course = Courses(course_name=course_name)
            course.save()
            messages.success(request, "Successfull Added course")
            return HttpResponseRedirect(reverse("add_course"))
        except:
            messages.error(request, "Error occur please try again")
            return HttpResponseRedirect(reverse("add_course"))

            
def add_subject(request):
    staffs = CustomUser.objects.filter(user_type=2)
    courses = Courses.objects.all()
    context = {
        "staffs": staffs,
        "courses": courses,
    }
    return render(request, "hod_template/add_subject_template.html", context) 

def add_subject_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        subject_name = request.POST.get("subject_name")
        course_id = request.POST.get("course")
        course_obj = Courses.objects.get(id=course_id)

        staff_id = request.POST.get("staff_name")
        staff_obj =CustomUser.objects.get(id=staff_id, user_type=2)

        try:
            subject = Subjects(subject_name=subject_name, course_id=course_obj, staff_id=staff_obj)
            subject.save()
            messages.success(request, "Successfull Added course")
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request, "Error occur please try again")
            return HttpResponseRedirect(reverse("add_subject"))

def manage_course(request):
    courses = Courses.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'hod_template/manage_course_template.html', context)

def manage_subjects(request):
    subjects = Subjects.objects.all()
    context = {
        "subjects": subjects
    }
    return render(request, 'hod_template/manage_subjects_template.html', context)

def manage_staffs(request):
    school_name = SchoolName.objects.all()
    context={
        "schools": school_name
    }
    return render(request, 'hod_template/school_list_template.html', context)
    

def manage_students(request):
    school_name = SchoolName.objects.all()
    context={
        "schools": school_name
    }
    return render(request, 'hod_template/school_list_student.html', context)
        

def edit_staff(request, staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    context = {
        "staff": staff,
        "id": staff_id,
    }
    return render(request, 'hod_template/edit_staff_template.html', context)

def edit_staff_save(request):
    if request.method != "POST":
        return HttpResponse("<h2> The method is not allowed </h2>")
    else:
        staff_id = request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()
            

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()
            messages.success(request, "Successfull Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id":staff_id}))
        except:
            messages.error(request, "Error occur please try again")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id":staff_id} ))



def edit_student(request, student_id):
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
    return render(request, 'hod_template/edit_student_template.html', context)

def edit_student_save(request):
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
                return HttpResponseRedirect(reverse("edit_student", kwargs={"student_id":student_id}))
            except:
                messages.error(request, "Error occur please try again")
                return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id} ))
        else:
            form = EditStudentForm(request.POST)
            context = {
                "form":form
            }
            return render(request, "hod_template/edit_student_template.html", context) 

def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    context = {
        "course": course,
        "id": course_id,
    }
    return render(request, "hod_template/edit_course_template.html", context) 


def edit_course_save(request):
    if request.method != 'POST':
        return HttpResponse("The method is not allowed")
    else:
        course_id = request.POST.get("course_id")
        course_name = request.POST.get('course')
    try:
        course = Courses.objects.get(id=course_id)
        course.course_name = course_name
        course.save()
        messages.success(request, "Successfull Edit course")
        return HttpResponseRedirect(reverse("edit_course", kwargs={"course_id": course_id} ))
    except:
        messages.error(request, "Error occur please try again")
        return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id": course_id} ))
        

def edit_subject(request,subject_id):
    subject = Subjects.objects.get(id=subject_id)
    staffs = CustomUser.objects.filter(user_type=2)
    courses = Courses.objects.all()
    context = {
        "subject": subject,
        "staffs": staffs,
        "courses": courses,
        "id": subject_id
    }
    return render(request, 'hod_template/edit_subject_template.html', context)


def edit_subject_save(request):
    if request.method != 'POST':
        return HttpResponse("The method is no valid")
    else:
        try:
            subject_id = request.POST.get("subject_id")
            subject_name = request.POST.get("subject_name")
            course_id  = request.POST.get("course_id")
            staff_id = request.POST.get("staff_id")

            course_obj = Courses.objects.get(id=course_id)
            staff_obj = CustomUser.objects.get(id=staff_id)

            subject = Subjects.objects.get(id=subject_id)
            subject.subject_name = subject_name
            subject.course_id = course_obj
            subject.staff_id = staff_obj
            subject.save()
            messages.success(request, "Successfull Edit Subject")
            return HttpResponseRedirect(reverse("edit_subject",  kwargs={"subject_id":subject_id } ))
        except:
            messages.error(request, "Error occur please try again")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id } ))

def manage_session(request):
    return render(request, "hod_template/manage_session_template.html")

def manage_session_save(request):
    if request.method != "POST":
        return HttpResponse("The request is not valid")
    else:
        session_start_year = request.POST.get("session_started")
        session_end_year = request.POST.get("session_ended")
    try:
        sessionyear = SessionYearModel(session_start_year=session_start_year, session_end_year=session_end_year)
        sessionyear.save()
        messages.success(request, "Successfull Edit Subject")
        return HttpResponseRedirect(reverse("manage_session"))
    except:
        messages.error(request, "Error occur please try again")
        return HttpResponseRedirect(reverse("manage_session"))


def school_list(request, school_id):
    staffs = Staffs.objects.filter(school_id__school_name=school_id)
    school_name = SchoolName.objects.get(school_name=school_id)
    context = {
        "staffs": staffs,
        "schools": school_name
    }
    return render(request, 'hod_template/manage_staff_template.html', context)

def school_list_student(request, school_id):
    students = Students.objects.filter(school_id__school_name=school_id)
    print(students)
    school_name = SchoolName.objects.get(school_name=school_id)
    context = {
        "students": students,
        "schools": school_name
    }
    return render(request, 'hod_template/manage_student_template.html', context)


def fit_person(request):
    return render(request, 'hod_template/add_fit_person_template.html')


def fit_person_save(request):
    if request.method != 'POST':
        return HttpResponse("This method is not allowed")
    else:
        person_name = request.POST.get("fitperson_name")
        person_number = request.POST.get("fitperson_number")

        try:
            fit_person = FitPersonName(fit_person_name=person_name, fit_person_number=person_number)
            fit_person.save()
            messages.success(request, "Successfull LAdd fit person")
            return HttpResponseRedirect(reverse("fit_person"))
        except:
            messages.error(request, "Error occur please try again")
            return HttpResponseRedirect(reverse("fit_person"))



def class_streem(request):
    return render(request, 'hod_template/add_class_streem_template.html')

def class_streem_save(request):
    if request.method != 'POST':
        return HttpResponse("This method is not valid")
    else:
        class_streem = request.POST.get('class_streem')
    try:
        class_streem = StudentStreem(streem_name=class_streem)
        class_streem.save()
        messages.success(request, "Successfull Streem")
        return HttpResponseRedirect(reverse("class_streem"))
    except:
        messages.error(request, "Error occur please try again")
        return HttpResponseRedirect(reverse("class_streem"))




def house_hold(request):
    return render(request, 'hod_template/add_student_household_template.html')

def house_hold_save(request):
    if request.method != 'POST':
        return HttpResponse("This method is not valid")
    else:
        father_name = request.POST.get('father_name')
        father_number = request.POST.get('father_number')
        house_location = request.POST.get('house_location')
        house_number = request.POST.get('house_number')
        
        try:
            house_hold = HouseHoldDetail(father_house_name=father_name,house_number=father_number,street_village=house_location,father_houser_number=house_number)
            house_hold.save()
            messages.success(request, "Successfull LAdd fit person")
            return HttpResponseRedirect(reverse("house_hold"))
        except:
            messages.error(request, "Error occur please try again")
            return HttpResponseRedirect(reverse("fit_person"))

def add_deo(request):
    return render(request, "hod_template/add_deo_template.html") 

def add_deo_save(request):
    if request.method != "POST":
        return HttpResponse("Method is not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
    try:
        
        user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name,user_type=5)
        user.deo.address = address
        user.save()

        messages.success(request, "Successfull")
        return HttpResponseRedirect(reverse("add_deo"))
    except:
        messages.error(request, "Error occur please try again")
        return HttpResponseRedirect(reverse("add_deo"))

    
def manage_deo(request):
    deos = Deo.objects.all()
    context = {
        'deos': deos
    }
    return render(request, 'hod_template/manage_deo_template.html', context)

def add_staff_admin(request):
    return render(request, 'hod_template/add_staff_admin_template.html')      