from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from ..forms.form_listing import ListingForm
from ..models import Listing, Image, Category

def detail(request, pk):
    listing = get_object_or_404(Listing ,pk = pk)
    images =  Image.objects.filter(listing_id=pk)
    print(images)
    categories = Category.objects.all()


    return render(request, "web/itemdescp.html", {
        'listing': listing,
        'I':images,
        'categories':categories,
    })

def delete(request, pk):
    item = get_object_or_404(Listing, pk=pk, user = request.user)
    item.delete()
    return redirect("/user")

def edit(request, pk):
    item = get_object_or_404(Listing, pk=pk, user = request.user)
    
