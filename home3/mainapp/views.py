from django.shortcuts import render, render_to_response
from mainapp.models import Teach
from mainapp.models import Work

def main(request):
    return render_to_response("index.html")

def work(request):
    place_of_work = Work.objects.all()
    return render_to_response("work.html", {'organization':[work.organization for work in place_of_work],
                                            'position': [work.position for work in place_of_work],
                                            'site': [work.site for work in place_of_work]})

def teach(request):
    place_of_teach = Teach.objects.all()
    return render_to_response("teach.html",
                              {'universitet':[teach.universitet for teach in place_of_teach],
                               'datestart':[teach.datestart for teach in place_of_teach],
                               'dateend': [teach.dateend for teach in place_of_teach],
                               'specials': [teach.specials for teach in place_of_teach],
                               'site': [teach.site for teach in place_of_teach]})
