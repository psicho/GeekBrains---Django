from django.shortcuts import render, render_to_response
from mainapp.models import Teach, Work

def main(request):
    return render_to_response("index.html")

def work(request):
    place_of_work = Work.objects.all()
    return render_to_response("work.html", {'place_of_work': place_of_work})

def teach(request):
    place_of_teach = Teach.objects.all()
    return render_to_response("teach.html", {'place_of_teach': place_of_teach})
