from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import DoctorForm
from .models import Doctor


@login_required(login_url="login_url")
def patient_view(request):
    template_name = "curd_app/info.html"
    form = DoctorForm()
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    context = {"form": form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_view(request):
    template_name = "curd_app/show.html"
    obj = Doctor.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Doctor.objects.get(id=pk)
    form = DoctorForm(instance=obj)
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_urls")
    template_name = "curd_app/info.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request, pk):
    obj = Doctor.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_urls")
    return render(request, 'curd_app/confirm.html')
