from django.shortcuts import render, HttpResponse
from Portal_App.forms import Signup
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
import random
otp_storage = 0
def CREATE (request):
    if request.method=='POST':
        signupform=Signup(request.POST) 
        if signupform.is_valid() and signupform.cleaned_data['password']==signupform.cleaned_data['confirm_password']:
            password=signupform.cleaned_data['password']
            fname=signupform.cleaned_data['first_name']
            lname=signupform.cleaned_data['last_name']
            email=signupform.cleaned_data['email']
            username=signupform.cleaned_data['username']

            new_user = User.objects.create_user(username, email, password)
            new_user.first_name=fname
            new_user.last_name=lname
            new_user.save()
        else:
            print('password is match')
    signupform = Signup()
    context={
        'signupform':signupform
    }
    return render(request,'test.html', context)   

def INDEX(request):
   
        username = request.GET.get('username')  
        email = request.GET.get('email')        
        password = request.GET.get('password') 

        return render(request, 'index.html', {
            'username': username,
            'email': email,
            'password': password
        })



from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html')  # Redirect to the index page after login
        else:
            return render(request, 'index.html')
import random
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
 

def Forgot(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            otp = random.randint(1000, 9999)
            
            # Store OTP and Email in session
            request.session['validate_otp'] = otp
            request.session['email_session'] = email
            request.session.modified = True  # Ensure session updates

            print(f"Stored OTP: {otp}")  # Debugging

            send_mail(
                "Password Reset OTP",
                f"Your OTP is: {otp}",
                "arvindsonkar685@gmail.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "OTP sent to your email!")
            return redirect('validate_otp')

    return render(request, 'forgot.html')


def OtpVerify(request):
    if request.method == "POST":
        otp = request.POST.get('otp')
        stored_otp = request.session.get('validate_otp')
        
        if stored_otp is None:
            messages.error(request, "OTP session expired. Please request a new OTP.")
            return redirect('forgot_password')
        
        if otp and otp.isdigit() and int(otp) == stored_otp:
            return redirect('changepassword')
        else:
            messages.error(request, "Invalid OTP. Try again.")
            return redirect('validate_otp')

    return render(request, 'forgot.html')


class ChangePassword(View):
    def get(self, request):
        return render(request, 'changepassword.html')

    def post(self, request):
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if not new_password or not confirm_password:
            messages.error(request, "Both password fields are required.")
            return redirect('changepassword')

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('changepassword')

        email = request.session.get('email_session')
        if not email:
            messages.error(request, "Session expired or invalid email.")
            return redirect('forgot_password')

        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)

            # Clear session after password change
            request.session.flush()

            # messages.success(request, "Password changed successfully.")
            return redirect('login')
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
            return redirect('changepassword')