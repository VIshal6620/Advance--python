from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .service.UserService import UserService


def ors_home(request):
    return HttpResponse("<h1>ORS App</h1>")


def welcome(request):
    return render(request, "Welcome.html")


def test_user_signup(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    login_id = request.POST.get('login_id')
    password = request.POST.get('password')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')
    print(first_name)
    print(last_name)
    print(login_id)
    print(password)
    print(dob)
    print(address)
    print(csrfmiddlewaretoken)
    return render(request, 'UserRegistration.html')


def user_signup(request):
    message = ''
    if request.method == "POST":
        params = {}
        params['first_name'] = request.POST.get('first_name')
        params['last_name'] = request.POST.get('last_name')
        params['login_id'] = request.POST.get('login_id')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        service.add(params)
        message = 'User Registered Successfully'
    return render(request, 'UserRegistration.html', {'message': message})


def user_signin(request):
    message = ''
    if request.method == "POST":
        login_id = request.POST.get('login_id')
        password = request.POST.get('password')
        service = UserService()
        user_data = service.auth(login_id, password)
        if len(user_data) != 0:
            request.session['first_name'] = user_data[0].get('first_name')
            return redirect('/ORS/welcome')
        # return render(request, 'Welcome.html', {'FirstName': user_data[0].get('FirstName')})
        else:
            message = 'Login_id & Password is Invalid'
    return render(request, 'Login.html', {'message': message})


def user_save(request):
    message = ''
    if request.method == "POST":
        params = {}
        params['first_name'] = request.POST.get('first_name')
        params['last_name'] = request.POST.get('last_name')
        params['login_id'] = request.POST.get('login_id')
        params['password'] = request.POST.get('password')
        params['dob'] = request.POST.get('dob')
        params['address'] = request.POST.get('address')
        service = UserService()
        if request.POST['operation'] == "save":
            service.add(params)
            message = 'User Added Successfully'
        if request.POST['operation'] == "update":
            params['id'] = request.POST.get('id')
            service.update(params)
            message = 'User Updated Successfully'
    return render(request, 'User.html', {'message': message})


def test_list(request):
    list = [
        {"id": 1, "first_name": "vishal", "last_name": "vishwakarma", "Email": "vishal@gmail.com", "password": "1234"},
        {"id": 2, "first_name": "vishal", "last_name": "vishwakarma", "Email": "vishal@gmail.com", "password": "1234"},
        {"id": 3, "first_name": "vishal", "last_name": "vishwakarma", "Email": "vishal@gmail.com", "password": "1234"},
        {"id": 4, "first_name": "kamal", "last_name": "vishwakarma", "Email": "vishal@gmail.com", "password": "1234"},
        {"id": 5, "first_name": "jatin", "last_name": "patel", "Email": "jatin@123", "password": "12345"},
    ]
    return render(request, 'TestList.html', {"list": list})


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    if request.method == "POST":
        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1
        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1
        if request.POST['operation'] == "search":
            params['first_name'] = request.POST['first_name']

    service = UserService()
    list = service.search(params)
    index = (params['pageNo'] - 1) * 5
    return render(request, "UserList.html", {"list": list, 'pageNo': params['pageNo'], 'index': index})


def delete_user(request, id=0):
    service = UserService()
    service.delete(id)
    return redirect("/ORS/list/")


def edit_user(request, id=0):
    service = UserService()
    user_data = service.get(id)
    user_data[0]['dob'] = user_data[0]['dob'].strftime('%Y-%m-%d')
    return render(request, 'User.html', {'form': user_data[0]})


def logout(request):
    request.session['first_name'] = None
    return redirect('/ORS/login')


def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)


def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)


def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")


def setCookies(request):
    key = "name"
    value = "abc"
    res = HttpResponse("<h1>cookie created..!!</h1>")
    res.set_cookie(key, value, max_age=20)
    return res


def getCookies(request):
    value = request.COOKIES.get('name')
    html = "<h3><center> value = {} </center></h3>".format(value)
    return HttpResponse(html)
