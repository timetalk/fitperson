from django import forms
from . models import Courses, FitPersonName, HouseHoldDetail, SchoolName, SessionYearModel, StudentStreem

class DateInput(forms.DateInput):
    input_type="year"

class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    school_list=[]
    try:
        schools=SchoolName.objects.all()
        for school in schools:
            small_school=(school.id, school.school_name)
            school_list.append(small_school)
    except:
        school_list=[]
    
    course_list=[]
    try:
        courses=Courses.objects.all()
        for course in courses:
            small_course=(course.id, course.course_name)
            course_list.append(small_course)
    except:
        course_list=[]
    
    fit_person_list=[]
    try:
        fit_persons=FitPersonName.objects.all()
        for fit_person in fit_persons:
            small_fit_person=(fit_person.id, fit_person.fit_person_name)
            fit_person_list.append(small_fit_person)
    except:
        fit_person_list=[]
    

    household_list=[]
    try:
        households=HouseHoldDetail.objects.all()
        for household in households:
            small_household=(household.id, household.father_house_name)
            household_list.append(small_household)
    except:
        household_list=[]
    
    class_list=[]
    try:
        classs=StudentStreem.objects.all()
        for class_id in classs:
            small_class=(class_id.id, class_id.streem_name)
            class_list.append(small_class)
    except:
        class_list=[]
    
    
    session_list=[]
    try:
        sessions=SessionYearModel.objects.all()
        for session in sessions:
            small_session=(session.id, str(session.session_start_year)+" - "+str(session.session_end_year))
            session_list.append(small_session)
    except:
        session_list=[]
    

    gender_choice=(
        ("Male", "Male"),
        ("Female", "Female")
    )
 
    school_name = forms.ChoiceField(label="School Name", choices=school_list, widget=forms.Select(attrs={'class': 'form-control'}))
    class_name = forms.ChoiceField(label="Form And Streem", choices=class_list, widget=forms.Select(attrs={'class': 'form-control'}))
    fit_person_name = forms.ChoiceField(label="Fit Person", choices=fit_person_list, widget=forms.Select(attrs={'class': 'form-control'}))
    father_house_name = forms.ChoiceField(label="Father House Name", choices=household_list, widget=forms.Select(attrs={'class': 'form-control'}))
    course=forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={'class': 'form-control'}))
    sex=forms.ChoiceField(label="Sex", choices=gender_choice,  widget=forms.Select(attrs={'class': 'form-control'}))
    session_year_id=forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile image", widget=forms.FileInput(attrs={"class": "form-control"}))


class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    
    course_list=[]
    try:
        courses=Courses.objects.all()
        for course in courses:
            small_course=(course.id, course.course_name)
            course_list.append(small_course)
    except:
         course_list=[]

    session_list=[]
    try:
        sessions=SessionYearModel.objects.all()
        for session in sessions:
            small_session=(session.id, str(session.session_start_year)+" - "+str(session.session_end_year))
            session_list.append(small_session)
    except:
        course_list=[]

    gender_choice=(
        ("Male", "Male"),
        ("Female", "Female")
    )

    
    fit_person_list=[]
    try:
        fit_persons=FitPersonName.objects.all()
        for fit_person in fit_persons:
            small_fit_person=(fit_person.id, fit_person.fit_person_name)
            fit_person_list.append(small_fit_person)
    except:
        fit_person_list=[]
    

    household_list=[]
    try:
        households=HouseHoldDetail.objects.all()
        for household in households:
            small_household=(household.id, household.father_house_name)
            household_list.append(small_household)
    except:
        household_list=[]
    
    class_list=[]
    try:
        classs=StudentStreem.objects.all()
        for class_id in classs:
            small_class=(class_id.id, class_id.streem_name)
            class_list.append(small_class)
    except:
        class_list=[]
    
    school_list=[]
    try:
        schools=SchoolName.objects.all()
        for school in schools:
            small_school=(school.id, school.school_name)
            school_list.append(small_school)
    except:
        school_list=[]

    course=forms.ChoiceField(label="Course", choices=course_list, widget=forms.Select(attrs={'class': 'form-control'}))
    school_name = forms.ChoiceField(label="School Name", choices=school_list, widget=forms.Select(attrs={'class': 'form-control'}))
    class_name = forms.ChoiceField(label="Form And Streem", choices=class_list, widget=forms.Select(attrs={'class': 'form-control'}))
    fit_person_name = forms.ChoiceField(label="Fit Person", choices=fit_person_list, widget=forms.Select(attrs={'class': 'form-control'}))
    father_house_name = forms.ChoiceField(label="Father House Name", choices=household_list, widget=forms.Select(attrs={'class': 'form-control'}))
    sex=forms.ChoiceField(label="Sex", choices=gender_choice,  widget=forms.Select(attrs={'class': 'form-control'}))
    session_year_id=forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={"class": "form-control"}))
    profile_pic = forms.FileField(label="Profile image", widget=forms.FileInput(attrs={"class": "form-control"}))