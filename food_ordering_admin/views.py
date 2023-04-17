from django.shortcuts import render

# Create your views here.

# def signup_staff(request):
#   if request.method == "POST":
#     new_user = User(
#       first_name = request.POST['first_name'],
#       last_name = request.POST['last_name'],
#       username = request.POST['username'],
#       email = request.POST['email'],
#       password = make_password(request.POST['password']),
#       is_staff = request.POST.get('is_staff') == 'on'
#     )
#     new_user.save()

#     return redirect('login')
#   return render(request,'signup_staff.html')
