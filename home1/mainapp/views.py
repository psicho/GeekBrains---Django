from django.shortcuts import render, render_to_response

def main(request):
    return render_to_response("index.html")

def work(request):
    return render_to_response("work.html")

def teach(request):
    return render_to_response("teach.html")

def style(request):
    return render_to_response("style.css")