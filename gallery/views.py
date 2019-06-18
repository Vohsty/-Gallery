from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image


def home(request):
    images = Image.all_images()
    row = round(len(images)/4)
    images1 = Image.all_images()[0:row]
    images2 = Image.all_images()[row:row*2]
    images3 = Image.all_images()[row*2:row*3]
    images4 = Image.all_images()[row*3:row*4]
    return render(request, 'home.html', {"images": images, "images1": images1, "images2": images2, "images3": images3, "images4": images4})

def category(request, cat):
    category = cat
    images = Image.filter_by_category(category)
    row = round(len(images)/4)
    images1 = images[0:row]
    images2 = images[row:row*2]
    images3 = images[row*2:row*3]
    images4 = images[row*3:row*4]
    return render(request,'category.html',{"images":images, "category":category, "images1": images1, "images2": images2, "images3": images3, "images4": images4})


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        images= Image.search(search_term)
        message = f"{search_term}"
        row = round(len(images)/4)
        images1 = images[0:row]
        images2 = images[row:row*2]
        images3 = images[row*2:row*3]
        images4 = images[row*3:row*4]
        return render(request,'search.html',{"message":message,"images":images, "images1": images1, "images2": images2, "images3": images3, "images4": images4})

    else:
        message="You haven't searched for any term"
        return render(request,'search.html',{"message":message})