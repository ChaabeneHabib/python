from django.shortcuts import render, redirect
from  .models import  *
from esprit.forms import *
# Create your views here.
from django.http import  HttpResponse
from  .models import Project
def helloDjango(request):
    return  HttpResponse("Bonjour Django")
def detail(request , id):
    return HttpResponse("Bonjour %s "%id)
def getAll(request):
    projects = Coach.objects.all()
    return  render(request ,'library.html',{'shelf':projects})
def addCoach(request):
    upload = CoachForm()
    if request.method == 'POST':
        upload = CoachForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('getAll')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'coach_form.html', {'upload_form': upload})
def update_Coach(request, coach_id):
    coach_ids = int(coach_id)
    try:
        book_sel = Coach.objects.get(id = coach_ids)
    except Coach.DoesNotExist:
        return redirect('getAll')
    book_form = CoachForm(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('getAll')
    return render(request, 'coach_form.html', {'upload_form':book_form})
def delete_book(request, coach_id):
    book_id = int(coach_id)
    try:
        book_sel = Coach.objects.get(id = book_id)
    except Coach.DoesNotExist:
        return redirect('getAll')
    book_sel.delete()
    return redirect('getAll')
def delete_Project(request, p_id):
    p_id = int( p_id)
    try:
        Project_sel = Project.objects.get(id =  p_id)
    except Project.DoesNotExist:
        return redirect('getAllProject')
    Project_sel.delete()
    return redirect('getAllProject')
def getAllProject(request):
    projects = Project.objects.all()
    return  render(request ,'getAllProject.html',{'shelf':projects})
def addProject(request):
    project = ProjectForm()
    if request.method == 'POST':
        upload = ProjectForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('getAllProject')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'Project_form.html', {'upload_form': project})
def updateProject(request, p_id):
    p_ids = int(p_id)
    try:
        p_sel = Project.objects.get(id = p_ids)
    except Project.DoesNotExist:
        return redirect('getAllProject')
    book_form = ProjectForm(request.POST or None, instance = p_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('getAllProject')
    return render(request, 'Project_form.html', {'upload_form':book_form})