from .models import Product,Testimonial
from math import ceil
from django.shortcuts import render,redirect

def home(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request,'shop/about.html')

def menu(request):
    categories = Product.objects.values('category').distinct()  # Get distinct categories
    allProds = []

    for category in categories:
        products = Product.objects.filter(category=category['category'])
        allProds.append(products)

    params = {'allProds': allProds}
    return render(request, 'shop/menu.html', params)

def testimonial(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        review = request.POST.get('review', '')
        test = Testimonial(name=name, review=review)
        test.save()
        return redirect('testimonial')  # Redirect to the same page after successful form submission

    testimonials = Testimonial.objects.all()
    testimonials = list(testimonials)
    testimonials.reverse()
    return render(request, 'shop/testimonial.html', {'testimonials': testimonials})

