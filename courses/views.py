from django.shortcuts import render


def courses_view(request):
    return render(request, "courses/courses_page.html")
