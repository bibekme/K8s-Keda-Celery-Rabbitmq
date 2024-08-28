from django.shortcuts import render

from .tasks import debug_task


def home(request):
    debug_task.delay()
    return render(request, "index.html")
