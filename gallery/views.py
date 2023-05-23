from django.shortcuts import render, get_object_or_404
from gallery.models import Image, Category
from datetime import date


def gallery_view(request):
    context = {
        "images": Image.objects.filter(created_date__gte=f"{date.today().year}-{date.today().month}-01")
    }
    return render(request, 'gallery.html', context)


def image_detail(request, pk):
    context = {
        "image": Image.objects.get(pk=pk)
    }
    return render(request, 'image_detail.html', context)
