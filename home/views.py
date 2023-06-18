import json
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from home.forms import SearchForm

from home.models import ContactForm, ContactFormMessage, Setting
from order.models import ShopCart
from product.models import Category, Product, Images, Comment


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category = Category.objects.all()
    dayproducts = Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]
    request.session['cart_items'] = ShopCart.objects.filter(
        user_id=request.user.id).count()
    context = {
        'setting': setting,
        'category': category,
        'page': 'home',
        'sliderdata': sliderdata,
        'dayproducts': dayproducts,
        'lastproducts': lastproducts,
        'randomproducts': randomproducts,
    }
    return render(request, 'index.html', context)


def aboutus(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               }
    return render(request, 'aboutus.html', context)


def references(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               }
    return render(request, 'references.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Your Message Has Been Successfully')
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form = ContactForm()
    context = {'setting': setting,
               'form': form,
               'category': category,
               }
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    products = Product.objects.filter(category_id=id)
    context = {
        'products': products,
        'category': category,
        'categorydata': categorydata,
    }
    return render(request, 'products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id)
    context = {
        'category': category,
        'product': product,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)


def product_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {
                'category': category,
                'products': products,
            }
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/')


def get_products(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        product = Product.objects.filter(title__icontains=query)
        results = []
        for rs in product:
            product_json = {}
            product_json = rs.title
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
