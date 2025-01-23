from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Userprofile,cardetails,bikedetails,rentedcars,rentedbikes,Payments
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from uuid import uuid4
import uuid

# Create your views here.
def index(request):
    return render(request,"index.html")
def registerpage(request):
    return render(request,"registerpage.html")
def dealer(request):
    return render(request,"dealerhome.html")
def user(request):
    return render(request,"custhome.html")
def payment(request):
    return render(request,"payment.html")
def loginpage(request):
    return render(request,"loginpage.html")
def updatepasswordpage(request):
    return render(request,"updatepassword.html")


def logout_view(request):
    """Logs out the user and redirects to the home page."""
    logout(request)  
    return redirect('index') 

def dealervehiclelist(request):
     cars = cardetails.objects.filter(dealer=request.user)
     bikes = bikedetails.objects.filter(dealer=request.user)
    
     return render(request, 'dealervehiclelist.html', {
          'cardetails': cars,
          'bikedetails': bikes
    })
def customervehiclelist(request):
    rented_cars = rentedcars.objects.filter(user=request.user)
    rented_bikes = rentedbikes.objects.filter(user=request.user)

    return render(request, 'customervehiclelist.html', {
        'rented_cars': rented_cars,
        'rented_bikes': rented_bikes,
    })

def carlist(request):
    car = cardetails.objects.filter(rental_status="Not Rented")  # Assuming 'Not Rented' is correct status
    return render(request, 'carlist.html', {'cardetails': car})
def bikelist(request):
    bike = bikedetails.objects.filter(rental_status="Not Rented")  # Assuming 'Not Rented' is correct status
    return render(request, 'bikelist.html', {'bikedetails': bike})

def aboutus(request):
    return render(request,"aboutus.html")

def dealercarlist(request):
    return render(request,"dealercarlist.html")
def dealerbikelist(request):
    return render(request,"dealerbikelist.html")
def carrent(request, id):
    car = get_object_or_404(cardetails, rent_id=id)
    user = request.user
    if request.method == 'POST':
        hours = request.POST['rent_hours']
        image = request.FILES.get('id_proof')
        rentedcars.objects.create(
            user=user,
            rent_id=car,
            rent_hours=hours,
            id_proof=image,
        )

        car.rental_status = "Rented"
        car.save()

        
        return redirect('payment')

    else:
        context = {
            'car': car,
        }
        return render(request, "carrent.html", context)



def bikerent(request, id):
    bike = get_object_or_404(bikedetails, rent_id=id)
    user = request.user
    if request.method == 'POST':
        hours = request.POST['rent_hours']
        image = request.FILES.get('id_proof')
        rentedbikes.objects.create(
            user=user,
            rent_id=bike,
            rent_hours=hours,
            id_proof=image,
        )

        bike.rental_status = "Rented"
        bike.save()

        
        return redirect('payment')

    else:
        context = {
            'bike': bike,
        }
        return render(request, "bikerent.html", context)





def register (request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        pincode=request.POST['pincode']
        address=request.POST['address']
        role=request.POST['role']
        email=request.POST['email']
        password=request.POST['password']
        user=User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.save()
        userProfile = Userprofile.objects.create(user=user,address=address,role=role,pincode=pincode)
        userProfile.save()
        return redirect('loginpage')
    else:
        return render (request,'user/register.html')

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user=authenticate(username=username,password=password)

        if authenticated_user is not None:
            login(request,authenticated_user)
            print(authenticated_user.userprofile.role)
            if authenticated_user.userprofile.role == 'Dealer':
                return redirect('dealer')
            elif authenticated_user.userprofile.role == 'Regular User':
                return redirect('user')
            
        else:
            return redirect('loginpage') 
    return render (request,'user/login.html')

#
def add_car(request):
    
    if request.method == 'POST':
        
        rent_id = request.POST.get('rent_id', str(uuid4()))
        carname = request.POST.get('carname')
        brand = request.POST.get('brand')
        year = request.POST.get('year')
        price = request.POST.get('price')
        fueltype = request.POST.get('fueltype')
        transmissiontype = request.POST.get('transmissiontype')
        image = request.FILES.get('image')
        
        
        car=cardetails(
            rent_id=rent_id,
            carname=carname,
            brand=brand,
            year=year,
            price=price,
            fueltype=fueltype,
            transmissiontype=transmissiontype,
            image=image,
            dealer=request.user 
        )
        car.save()
        return redirect('dealer') 

    return render(request, 'dealercarlist.html')

def add_bike(request):
    
    if request.method == 'POST':
        
        rent_id = request.POST.get('rent_id', str(uuid4()))
        bikename = request.POST.get('bikename')
        brand = request.POST.get('brand')
        year = request.POST.get('year')
        price = request.POST.get('price')
        fueltype = request.POST.get('fueltype')
        image = request.FILES.get('image')
        
        
        bike=bikedetails(
            rent_id=rent_id,
            bikename=bikename,
            brand=brand,
            year=year,
            price=price,
            fueltype=fueltype,
            image=image,
            dealer=request.user 
        )
        bike.save()
        return redirect('dealer') 

    return render(request, 'dealerbikelist.html')



def remove_car(request, rent_id):
    vehicle1 = get_object_or_404(cardetails, rent_id=rent_id, dealer=request.user)
    vehicle1.delete()
    return redirect('dealer')
def remove_bike(request, rent_id):
    vehicle2= get_object_or_404(bikedetails, rent_id=rent_id, dealer=request.user)
    vehicle2.delete()
    return redirect('dealer')

def update_login(request): 
    if request.method == 'POST':
        user = request.user
        new_username = request.POST.get('username')
        new_password = request.POST.get('password')

        if new_username:
            user.username = new_username
        if new_password:
            user.set_password(new_password)  

        user.save()
        return redirect('loginpage')

    else:
       
        user = request.user
        context = {
            'authenticated_user': user,
        }

    return render(request, 'updatepassword.html', context)