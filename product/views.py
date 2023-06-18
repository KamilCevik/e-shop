from audioop import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Comment, CommentForm
from django.contrib import messages


def index(request):
    return HttpResponse("Product Page")


@login_required(login_url='/login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user

            data = Comment()
            data.user_id = current_user.id
            data.product_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(
                request, 'Your Comment Has Been Submitted Successfully.')

            return HttpResponseRedirect(url)
    messages.error(request, 'Your comment could not be saved. Please check.')
    return HttpResponseRedirect(url)
