from django.shortcuts import render,redirect
from .forms import User_create_form,login_form,Add_item_form,Display_formset
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import AddItem


def user_creation_view(request):
    if request.method == 'POST':
        form = User_create_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = User_create_form()
    return render(request,'mainapp/user_creation.html',{'form':form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('display')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return redirect('display')
    form = login_form()
    return render(request,'mainapp/login.html',{'form':form,'redirect_field_name':'login'})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_item_view(request):
    if request.method == 'POST':
        Title = request.POST['Title']
        password = request.POST['password']
        AddItem.objects.create(user=request.user, Title=Title, password=password)
    form = Add_item_form()
    return render(request,'mainapp/add.html',{'form':form})

@login_required(login_url='login')
def display_item_view(request):
    data_set = AddItem.objects.filter(user = request.user)
    data_list = []
    for data in data_set:
        data_list.append({'Title':data.Title, 'password':data.password})

    formset = Display_formset(initial=data_list)
    if formset.is_valid():
        formset.save()
    return render(request,'mainapp/display.html',{'formset':formset})

