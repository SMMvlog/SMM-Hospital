from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def log(request):
    error=""
    if not request.user.is_staff:
        if request.method=="POST":
            u = request.POST['name']
            p = request.POST['pass']
            user = authenticate(username=u,password=p)
            try:
                if user.is_staff:
                    login(request,user)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        d = {'error':error}
        return render(request,'login.html',d)
    else:
        return redirect('home')

def logOut(request):
    logout(request)
    return redirect('log')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def home(request):
    if not request.user.is_staff:
       return redirect('log')
    doctor = Docter.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appointment:
        a+=1
    d1 = {"d":d,"p":p,"a":a}
    return render(request,'home.html',d1)

def add_doc(request):
    error=""
    if not request.user.is_staff:
        return redirect('log')
    if request.method=="POST":
        u = request.POST['name']
        contact = request.POST['contact']
        special = request.POST['special']
        # nw = Docter(name=u,mobile=contact,special=special)
        try:
            Docter.objects.create(name=u,mobile=contact,special=special)
            # nw.save()
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'add_doc.html',d)

def viewdoc(request):
    if not request.user.is_staff:
        return redirect('log')
    else:
        doc = Docter.objects.all()
        return render(request,'viewdoc.html',{'doc':doc})


def docdel(request,pid):
    if not request.user.is_staff:
        return redirect('log')
    doc = Docter.objects.get(id=pid)
    doc.delete()
    return redirect('viewdoc')


def viewp(request):
    if request.user.is_staff:
        pnt = Patient.objects.all()
        return render(request,'viewp.html',{'pnt':pnt})
    else:
        return redirect('log')

def addpnt(request):
    error = ""
    if not request.user.is_staff:
        return redirect('log')
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        gender= request.POST['gender']
        address= request.POST['address']
        # nw = Docter(name=u,mobile=contact,special=special)
        try:
            Patient.objects.create(name=name, mobile=contact, gender=gender,address=address)
            # nw.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'addpatient.html', d)

def delp(request,id):
    if not request.user.is_staff:
        return redirect('log')
    p = Docter.objects.get(id=id)
    p.delete()
    return redirect('viewp')
def uptp(request,id):
    error = ""
    if not request.user.is_staff:
        return redirect('log')
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        gender = request.POST['gender']
        address = request.POST['address']
        try:
            nw = Patient(id=id, name=name, mobile=contact, gender=gender,address=address)
            nw.save()
            error = "no"
        except:
            error = "yes"
    p = Patient.objects.get(id=id)
    return render(request, "uptp.html", {"error": error, "p": p})

def addappoint(request):
    error =""
    if not request.user.is_staff:
        return redirect('log')
    doc = Docter.objects.all()
    pnt = Patient.objects.all()
    if request.method=="POST":
        d = request.POST['doctor']
        p = request.POST['patient']
        dt = request.POST['date']
        tm = request.POST['time']
        doctor = Docter.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()
        try:
           Appointment.objects.create(doctor=doctor,patient=patient,date1=dt,time1=tm)
           error = "no"
        except:
            error = "yes"
    d = {'error': error,'doc':doc,'pnt':pnt}
    return render(request,'addappoint.html',d)

def viewappoint(request):
    if not request.user.is_staff:
        return redirect('log')
    fm = Appointment.objects.all()
    return render(request,"viewappoint.html",{'fm':fm})

def delapp(request,id):
    if not request.user.is_staff:
        return redirect('log')
    fm = Appointment.objects.get(id=id)
    fm.delete()
    return render(request, "viewappoint.html", {'fm': fm})

def editdoc(request,id):
    error = ""
    if not request.user.is_staff:
        return redirect('log')
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        special = request.POST['special']
        try:
            nw = Docter(id=id, name=name, mobile=contact, special=special)
            nw.save()
            error = "no"
        except:
            error = "yes"
    doc = Docter.objects.get(id=id)
    return render(request,"editdoc.html",{"error":error,"doc":doc})