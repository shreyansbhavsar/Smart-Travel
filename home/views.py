from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import logout
# Create your views here.
import random
from .models import CustomUser, Order_table, Image_table
from .decorators import t_only, p_only, g_only
from django.contrib.auth import authenticate, logout
# from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.conf import settings
from django.core.mail import send_mail

# json_file = open('databaseProj/config_vars.json').read()
# data = json.loads(json_file)


def index(request):
    return render(request, 'base.html')


def addphoto(request, id):
    data = CustomUser.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'addphoto.html', {'user': data})
    else:
        # uid = request.POST.get('uid', False)
        description = request.POST.get('description', False)
        img = request.FILES.get('img', False)
        # print(str(CustomUser.category))
        uid = request.user.id
        print(uid)

        obj = Image_table()
        obj.uid = uid
        obj.description = description
        obj.img = img

        obj.save()
        if request.user.category == 'Photographer':
            return redirect('pdashboard')
        else:
            return redirect('g_dashboard')


def myorders(request):
    lemail = request.user.email
    order = Order_table.objects.filter(email=lemail)
    return render(request, 'myorders.html', {'order': order})


def sendmail(email, subject, message):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


def page404(request):
    return render(request, 'page404.html')


@login_required
@t_only
def viewprofile(request, id):

    data = CustomUser.objects.get(id=id)
    u = Image_table.objects.filter(uid=id)
    return render(request, 'viewprofile.html', {'user': data, 'u': u})


def forgotpassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        pswd = CustomUser.objects.filter(email=email).all()
        print(pswd.values('password'))
        # subject = ""
        # message = ""
    return render(request, 'forgotpass.html')


@login_required
@t_only
def order(request, id):
    n = random.randint(1204784, 1218000)
    if request.method == 'GET':
        data = CustomUser.objects.get(id=id)
        return render(request, 'order.html', {'data': data, 'n': n})
    else:
        data = CustomUser.objects.get(id=id)
        m = request.POST['orderid']

        orderid = request.POST['orderid']
        email = request.POST['email']
        phnum = request.POST['phnum']
        fullname = request.POST['fullname']
        location = request.POST['location']
        category = request.POST.get('category', False)

        obj = Order_table()
        obj.orderid = orderid
        obj.email = email
        obj.location = location
        obj.fullname = fullname
        obj.phnum = phnum
        obj.category = category

        obj.save()
        semail = data.email
        subject = "Order recieved"
        message = "You have received an order form" + request.user.username + " for the location" + location + \
            " . Kindly note it and Contact the user. The Contact details are :" + \
            request.user.phnum + "."
        sendmail(semail, subject, message)

        subject = "Order recieved"
        message = "Your order has been placed having Order id " + orderid + \
            " .The Contact details of "+data.category+" are : "+data.phnum+"."
        sendmail(email, subject, message)
        return render(request, 'orderdone.html', {'n': m})


def profile(request):
    data = CustomUser.objects.get(id=request.user.id)
    # print(data)
    if request.method == "POST":
        # print(data)
        fn = request.POST.get('first_name', False)
        ln = request.POST.get('last_name', False)
        un = request.POST.get('username', False)
        em = request.POST.get('email', False)
        pn = request.POST.get('phnum', False)
        lt = request.POST.get('location', False)
        zc = request.POST.get('zipcode', False)
        ch = request.POST.get('charges', False)
        bio = request.POST.get('bio', False)
        # print(un)
    #     myuser = CustomUser()

        data.first_name = fn

        data.last_name = ln
        data.username = un
        data.email = em
        data.location = lt
        data.zipcode = zc
        data.phnum = pn
        data.charges = ch
        data.bio = bio
        print(data.bio)
        data.save()
        return render(request, 'base.html')
    else:
        return render(request, 'profile.html')


@ csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(str(user))
        if user is not None:
            if user.category == 'Traveller':
                auth_login(request, user)
                return redirect('dashboard')
            elif user.category == 'Photographer':
                auth_login(request, user)
                return redirect('pdashboard')
            else:
                auth_login(request, user)
                return redirect('g_dashboard')
        else:
            return render(request, 'login.html', {'msg': 'Failed. Please try again'})
    else:
        return render(request, 'login.html')
    if request.method == 'GET':
        return render(request, 'login.html')


@ csrf_exempt
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phnum = request.POST['phnum']
        location = request.POST['location']
        zipcode = request.POST['zipcode']
        category = request.POST['category']
        # img = request.FILES
        image = request.FILES.get('img', False)

        # phnum = request.POST['phnum']
        # print(request.POST)
        existing_email = CustomUser.objects.filter(email=email)
        is_new_user = (len(list(existing_email)) == 0)
        print(is_new_user)
        if (is_new_user):
            new_user = CustomUser.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                      email=email, password=password, phnum=phnum, location=location, zipcode=zipcode, category=category, image=image)
            new_user.save()
            subject = "Welcome"
            message = "Hello User, Welcome to Smart Travel your account has been created plz login "
            sendmail(email, subject, message)

            return render(request, 'base.html')
        else:
            return render(request, 'signup.html', {'msg': 'Error. Email already exists'})
    else:
        return render(request, 'signup.html')


@ login_required
def log_out(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'base.html')

    # clear session
    # del request.session['current_user']
    # del request.session['user_name']
    # return render(request, 'base.html')
    logout(request)
    return render(request, 'base.html')

# @login_required
# @check_group


@ login_required
@ t_only
def dashboard(request):
    return render(request, 'dashboard.html')


@ login_required
@ g_only
def g_dashboard(request):
    u = Image_table.objects.filter(uid=request.user.id)
    return render(request, 'g_dashboard.html', {'u': u})


@ login_required
@ p_only
def pdashboard(request):
    u = Image_table.objects.filter(uid=request.user.id)

    return render(request, 'pdashboard.html', {'u': u})


@ login_required
@ t_only
def photographer(request):
    # pcount = CustomUser.objects.filter(category='Photographer').count()
    x = CustomUser.objects.filter(category='Photographer').all()
    print(str(x))
    # pgrapher = CustomUser.objects.filter(category='Photographer').all()
    return render(request, 'photographer.html', {'x': x})


@ login_required
@ t_only
def guide(request):
    g = CustomUser.objects.filter(category='Guide').all()
    print(str(g))
    return render(request, 'guide.html', {'g': g})
