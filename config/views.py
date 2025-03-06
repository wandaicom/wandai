from django.shortcuts import render


def main(request):
    return render(request, "main.html")


def bigdata(request):
    return render(request, "bigdata.html")


def ai(request):
    return render(request, "ai.html")


def solution(request):
    return render(request, "solution.html")


def question(request):
    return render(request, "question.html")
