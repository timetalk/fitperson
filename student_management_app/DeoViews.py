from django.shortcuts import render
from student_management_app.models import FitPersonName, HouseHoldDetail, SchoolName, Staffs, StudentResults, StudentStreem, Students, Subjects


def deo_home(request):
    schools = SchoolName.objects.all()
    student_count = Students.objects.all().count()
    staff_count = Staffs.objects.all().count()
    fit_person_count = FitPersonName.objects.all().count()
    father_house_count = HouseHoldDetail.objects.all().count()
    context = {
        "schools": schools,
        "student_count": student_count,
        "staff_count": staff_count,
        "fit_person_count": fit_person_count,
        "father_house_count": father_house_count,
    }
    return render(request, "deo_template/home_content.html", context) 


def deo_school_detail(request, school_id):
    school = SchoolName.objects.get(school_name=school_id)
    print(school)
    schools = SchoolName.objects.all()
    context = {
        "school": school,
        "schools": schools,
    }
    return render(request, 'deo_template/deo_school_detail_template.html', context)

def show_students(request, school_id, streem_id):
    streem_id = StudentStreem.objects.get(id=streem_id)
    students = Students.objects.filter(school_id__school_name=school_id, streem_id__streem_name__iexact=streem_id.streem_name)
    school_name = SchoolName.objects.get(school_name=school_id)
    schools = SchoolName.objects.all()
    context = {
        "students": students,
        "schools": school_name,
        "schools": schools
    }
    return render(request, 'deo_template/manage_student_template.html', context)

def show_staffs(request, school_id):
    class_id = request.POST.get('class_id')
    print(class_id)
    staffs = Staffs.objects.filter(school_id__school_name=school_id)
    school_name = SchoolName.objects.get(school_name=school_id)
    schools = SchoolName.objects.all()
    context = {
        "staffs": staffs,
        "schools": school_name,
        "schools": schools
    }
    return render(request, 'deo_template/manage_staff_template.html', context)


def classes_streem(request, school_id):
    students = Students.objects.filter(school_id__school_name=school_id)
    school = SchoolName.objects.get(school_name=school_id)
    schools = SchoolName.objects.all()
    classes = StudentStreem.objects.all()
    context = {
        "classes": classes,
        "schools": schools,
        "students": students,
        "school": school,
    }
    return render(request, 'deo_template/show_classes_template.html', context)


def manage_all_staff(request):
    staffs = Staffs.objects.all()
    schools = SchoolName.objects.all()
    context = {
        "staffs": staffs,
        "schools": schools
    }
    return render(request, 'deo_template/manage_staff_template.html', context)



def manage_all_student(request):
    students = Students.objects.all()
    schools = SchoolName.objects.all()
    context = {
        "students": students,
        "schools": schools
    }
    return render(request, 'deo_template/manage_student_template.html', context)