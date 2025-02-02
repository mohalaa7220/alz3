from django.shortcuts import render
from .models import MainTitle
from django.contrib.auth.decorators import login_required


@login_required
def quiz_view(request):
    main_titles = MainTitle.objects.prefetch_related("questions").all()
    return render(request, "mmse.html", {"main_titles": main_titles})
