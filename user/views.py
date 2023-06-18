from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from order.models import Order, OrderProduct
from product.models import Category, Comment
from django.contrib import messages
from user.models import UserProfile
from user.forms import LoginForm, ProfileUpdateForm, RegisterForm, UserUpdateForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)
    category = Category.objects.all()
    context = {
        "form": form,
        "category": category,
    }
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=password)
        login(request, user)
        current_user = request.user
        data = UserProfile()
        data.user_id = current_user.id
        data.save()
        messages.info(request, "You Have Successfully Registered")
        return redirect("/")

    return render(request, "register.html", context)


def loginUser(request):
    form = LoginForm(request.POST or None)
    category = Category.objects.all()
    context = {
        "form": form,
        "category": category,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Username or password incorrect")
            return render(request, "login.html", context)

        login(request, user)
        return redirect("/")
    return render(request, "login.html", context)


@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    return redirect("/")


def user_profile(request):
    category = Category.objects.all()
    profile = UserProfile.objects.get(user_id=request.user.id)
    context = {
        'category': category,
        'profile': profile
    }
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('/user')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'category': category,
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def change_password(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password was successfully updated')
            return redirect('change_password')
        else:
            messages.error(request, 'Please corrent the error below.')
            return HttpResponseRedirect(url)

    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form, 'category': category})


@login_required(login_url='/login')
def user_orders(request):
    category = Category.objects.all()
    orders = Order.objects.filter(user_id=request.user.id)
    context = {
        'category': category,
        'orders': orders,
    }
    return render(request, 'user_orders.html', context)


@login_required(login_url='/login')
def orderdetail(request, id):
    category = Category.objects.all()
    order = Order.objects.get(user_id=request.user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)

    context = {
        'category': category,
        'order': order,
        'orderitems': orderitems,
    }
    return render(request, 'user_orderdetail.html', context)


@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    comments = Comment.objects.filter(user_id=request.user.id)
    context = {
        'category': category,
        'comments': comments,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomment(request, id):
    Comment.objects.filter(id=id, user_id=request.user.id).delete()
    messages.success(request, 'Comment Deleted..')
    return HttpResponseRedirect('/user/comments')
