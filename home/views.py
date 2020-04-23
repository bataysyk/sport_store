from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, logout
from .models import  Product, Basket
from .form import ProductForm, ProductFormEdit
from django.contrib import messages
# Create your views here.

def home(request):
    data = dict()
    products = Product.objects.all()
    data["products"] = products
    return render(request, "home.html", context=data)

def user_login(request):
    if request.method == "GET":
        return render(request, "log_in.html")
    elif request.method == "POST":
        username = request.POST.get('account-name')
        password = request.POST.get('account-password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    data = dict()
                    data["username"] = user.username
                    data["email"] = user.email
                    data["password"] = user.password
                    return home(request)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        return render(request, 'home.html')

def sign_up(request):
    if request.method == "GET":
        return render(request, "sign_up.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        global user
        user = User(
            username=name,
            email=email,
            password=password
        )
        user.save()
        return render(request, "home_2.html")

def account(request):
    return render(request, "account.html")

def user_exit(request):
    logout(request)
    return render(request, "home.html")

def ajax_login_check(request):
    information = dict()
    loginiserted = request.GET.get('login')
    if User.objects.filter(username=loginiserted).exists():
        information['test'] = 'Exists'
    else:
        information['test'] = 'Free'

    return JsonResponse(data=information)

def ajax_email_check(request):
    information = dict()
    loginiserted = request.GET.get('login')
    if User.objects.filter(email=loginiserted).exists():
        information['test'] = 'Exists'
    else:
        information['test'] = 'Free'

    return JsonResponse(data=information)

def ajax_password_1_check(request):
    information = dict()
    password_1 = request.GET.get('password_1')
    password_2 = request.GET.get('password_2')
    if password_1 == password_2:
        information['test'] = 'Exists'
    else:
        information['test'] = 'Free'

    return JsonResponse(data=information)

def ajax_registration_login_check(request):
    information = dict()
    login_to_test = request.GET.get("login")
    if login == User.objects.filter(username=login_to_test).exists():
        information["test"] = "Exists"
    else:
        information['test'] = "Free"

    return JsonResponse(data=information)

def ajax_registration_password_check(request):
    information = dict()
    password = request.GET.get("password")
    if len(password) < 5:
        information["test"] = "Exists"
    else:
        information["test"] = "Free"
    return JsonResponse(data=information)


def add_in_basket(request, product_id: int):
    if not request.user.is_authenticated:
        raise Http404
    product = Product.objects.get(id=product_id)
    number = 1
    user = request.user

    basket = Basket(
        product=product,
        status=False,
        number=number,
        user=user
    )
    basket.save()
    return redirect('/home/')

def basket(request):
    data = dict()
    basket = Basket.objects.filter(user=request.user.id)
    basket_sum = sum([i.product.price for i in basket])
    data["basket"] = enumerate(basket, start=1)
    data["basket_sum"] = basket_sum
    return render(request, "basket.html", context=data)

def basket_delete_product(request, product_id: int):
    product = Basket.objects.get(id=product_id)
    product.delete()
    return redirect("/home/basket/")

def admin_add_product(request):
    data =dict()
    form = ProductForm(request.POST or None, request.FILES or None)
    data["form"] = form
    if request.method == "POST":
        if form.is_valid:
            print("correct")
            form.save()
            return redirect("/home/")
    return render(request, "admin_add_product.html", context=data)

def admin_edit_product(request, product_id: int):
    data = dict()
    product = Product.objects.get(id=product_id)

    if request.method == "GET":
        form = ProductFormEdit(instance=product)
        data["product"] = product
        data["form"] = form
        return render(request, "admin_edit_product.html", context=data)
    elif request.method == "POST":
        product_form = ProductFormEdit(request.POST)
        if product_form.is_valid():
            product.price = product_form.cleaned_data['price']
            product.name = product_form.cleaned_data['name']
            product.date_added = product_form.cleaned_data['date_added']
            product.weight = product_form.cleaned_data["weight"]
            product.producer = product_form.cleaned_data["producer"]
            product.note = product_form.cleaned_data["note"]
            product.save()
            messages.success(request, "Dish modified successfully")
        else:
            messages.error(request, "Dish form was NOT correct")
        return redirect('/home/')



def admin_delete_product(request, product_id: int):
    delete_product = Product.objects.get(id=product_id)
    delete_product.delete()
    return redirect("/home/")

def ajax_delete_product(request, product_id: int):
    print(request)
    product = Basket.objects.get(id=product_id)
    print(product)
    product.delete()
    return JsonResponse({'result': "OK"})

def information_about_product(request, product_id: int):
    data =dict()
    product_information = Product.objects.get(id=product_id)
    print(product_information.picture)
    data["product_information"] = product_information
    return render(request, "information_about_product.html", context=data)

def ajax_decrease_product_count(request, product_id:int):
    product = Basket.objects.get(id=product_id)
    if product.number == 1 :
        return JsonResponse({"result": "NOT OK"})
    if product.number > 1:
        product.number -= 1
        product.save()


    return JsonResponse({'result': "OK"})

