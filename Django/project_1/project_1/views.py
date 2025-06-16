from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from app_1.models import Date,s,Edit,Signup
from datetime import datetime
def signup(request):
    return render(request,"signup.html")

def login(request):
    return render(request,"login.html")

def user_signup(request):
    name=request.POST.get('name');
    email=request.POST.get('email');
    password=request.POST.get('password');
    confirm_password=request.POST.get('confirm-password');
    if password!=confirm_password:
        error="ERROR"
        problem="Password Mismatch."
        return render(request,"msg.html",{"error":error,"p1":problem})
      
    check=Signup.objects.all().filter(Q(name=name) | Q(email=email)).first()
    if check:
        error="ERROR"
        problem="Username or Email already exists."
        return render(request,"msg.html",{"error":error,"p2":problem})
    else:
        signup=Signup(name=name,email=email,password=password,confirm_password=confirm_password)
        signup.save()
        return redirect("login")

def user_login(request):
    username=request.POST.get('username');
    password=request.POST.get('password');
    
    signup = Signup.objects.filter(Q(name=username) | Q(email=username)).first()
    if signup==None:
        error="ERROR"
        problem="User does not exist."
        return render(request,"msg.html",{"error":error,"p3":problem})
    else:
        if password==signup.password:
            
            request.session['username']=username
            return redirect("home")
        else:
            error="ERROR"
            problem="Password Incorrect."
            return render(request,"msg.html",{"error":error,"p4":problem})
        
def home(request):
    return render(request,"home.html")

def hello(request):
    return HttpResponse("hello,enjoy.......")

def date(request):
    today = timezone.now().date()
    return render(request,"select_date.html",{'today':today})

def edit(request):
    return render(request,"edit.html")

def insert(request):
    dt=request.POST.get('date');
    format_user_date = datetime.strptime(dt, '%Y-%m-%d').date()
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    check=s.objects.all().filter(user_id=user).filter(date_field=format_user_date)
    if check:
        error="ERROR"
        problem="Date already set in timetable.."
        return render(request,"msg.html",{"error":error,"p5":problem})
    else:
        d=Date(date=format_user_date,user_id=user);
        d.save();
        return render(request,"set_timetable.html",{'a':format_user_date})
    
# def view(request):
#     display=Date.objects.all().order_by('-id').first()
#     return render(request,"set_timetable.html",{'a':display})

def save_work(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    display=Date.objects.all().filter(user_id=user).order_by('-id').first()
    date_format=display.date
    first=request.POST.get('work_9_10_30');
    second=request.POST.get('work_10_30_12');
    third=request.POST.get('work_12_1_30');
    fourth=request.POST.get('work_1_30_3');
    fifth=request.POST.get('work_3_4_30');
    sixth=request.POST.get('work_4_30_6');
    l=[first,second,third,fourth,fifth,sixth]
    l1=[]
    for i in l:
        if i!="":
            l1.append(i)
    if l1==[]:
        error="ERROR"
        problem="Empty works will not be saved."
        return render(request,"msg.html",{"error":error,"p6":problem})
    else:
        total_works=len(l1)
        login_user=  request.session['username']
        user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
        w=s(date_field=date_format,one=first,two=second,three=third,four=fourth,five=fifth,six=sixth,total=total_works,user_id=user);
        w.save();
        return render(request,"msg.html")

def sample(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    now = timezone.now()
    display = s.objects.filter(user_id=user, date_field__gte=now).order_by('date_field')
    delays = [(i, i * 0.3) for i in range(len(display))]
    return render(request,"home.html",{'a':display, 'delays': delays})


def edit(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    now = timezone.now()
    display = s.objects.filter(user_id=user, date_field__gte=now).order_by('date_field')
    return render(request,"edit.html",{'a':display})
def check(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    now = timezone.now()
    display = s.objects.filter(user_id=user, date_field__gte=now).order_by('date_field')
    l=[]
    for i in display:
        date=i.date_field
        l.append(date)
    user_date=request.POST.get('work_date');
    format_user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
    
    if format_user_date in l:
        e=Edit(date_field=user_date,user_id=user)
        e.save()
        work=s.objects.all().filter(user_id=user).get(date_field=format_user_date)
        return render(request,"set_timetable.html",{"a":format_user_date,"b":work})
    else:
        error="ERROR"
        problem = "No works set for this day."
        return render(request,"msg.html",{"error":error,"p7":problem})

def edit_work(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    display=Edit.objects.all().filter(user_id=user).order_by('-id').first()
    date_format=display.date_field
    first=request.POST.get('work_9_10_30');
    second=request.POST.get('work_10_30_12');
    third=request.POST.get('work_12_1_30');
    fourth=request.POST.get('work_1_30_3');
    fifth=request.POST.get('work_3_4_30');
    sixth=request.POST.get('work_4_30_6');
    
    
    l=[first,second,third,fourth,fifth,sixth]
    l1=[]
    for i in l:
        if i!="":
            l1.append(i)
    if l1==[]:
        error="ERROR"
        problem="Empty works will not be saved."
        return render(request,"msg.html",{"error":error,"p6":problem})
    else:
        total_works=len(l1)
        login_user=  request.session['username']
        user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
        w=s.objects.all().filter(user_id=user).get(date_field=date_format)
        w.one=first
        w.two=second
        w.three=third
        w.four=fourth
        w.five=fifth
        w.six=sixth
        w.total=total_works
        w.save();
        return render(request,"msg.html")

def delete(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    now = timezone.now()
    display=s.objects.all().filter(user_id=user, date_field__gte=now).order_by('date_field')
    b="enjoy"
    return render(request,"edit.html",{'a':display,"b":b})
def del_date(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    now = timezone.now()
    display=s.objects.all().filter(user_id=user, date_field__gte=now).order_by('date_field')
    l=[]
    for i in display:
        date=i.date_field
        l.append(date)
    user_date=request.POST.get('work_date');
    format_user_date = datetime.strptime(user_date, '%Y-%m-%d').date()
    
    if format_user_date in l:
        d=s.objects.all().filter(user_id=user).get(date_field=format_user_date).delete()
        b="enjoy"
        return render(request,"msg.html",{"b":b})

    else:
        error="ERROR"
        problem = "No works set for this day."
        return render(request,"msg.html",{"error":error,"p7":problem})


def view(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    now = timezone.now()
    display = s.objects.filter(user_id=user, date_field__gte=now).order_by('date_field')
    c="enjoy"
    return render(request,"edit.html",{'a':display,"c":c})

def time_table(request):
    login_user=  request.session['username']
    user =Signup.objects.filter(Q(name=login_user) | Q(email=login_user)).first()
    work_date=request.POST.get('work_date')
    w = s.objects.filter(user_id=user, date_field=work_date).first()

    if not w:
        error="ERROR"
        problem = "No works set for this day."
        return render(request,"msg.html",{"error":error,"p7":problem})

    # Define the fixed time slots
    time_slots = [
        "9:00 AM - 10:30 AM",
        "10:30 AM - 12:00 PM",
        "1:30 PM - 3:00 PM",
        "3:00 PM - 4:30 PM",
        "4:30 PM - 6:00 PM",
        "6:30 PM - 8:00 PM"
    ]

    # Extract work messages from the model fields
    work_messages = [
        w.one,
        w.two,
        w.three,
        w.four,
        w.five,
        w.six,
    ]

    # Combine time + work into one list
    slots = []
    for i in range(6):
        slots.append({
            "time": time_slots[i],
            "message": work_messages[i]
        })

    return render(request, 'view.html', {'slots': slots})

def password_reset(request):
    return render(request,"pswdreset.html")

def forgot_password(request):
    email=request.POST.get('email')
    new_password=request.POST.get('new_password')
    confirm_password=request.POST.get('confirm_password');
    if new_password!=confirm_password:
        error="ERROR"
        problem="Password Mismatch."
        return render(request,"msg.html",{"error":error,"p1":problem})
    check = Signup.objects.filter(Q(email=email)).first()
    if check==None:
        error="ERROR"
        problem="User does not exist."
        return render(request,"msg.html",{"error":error,"p3":problem})
    else:
        check.password=new_password
        check.confirm_password=confirm_password
        check.save()
    
        return render(request,"login.html")