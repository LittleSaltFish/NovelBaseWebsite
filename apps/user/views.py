from django.shortcuts import render

# Create your views here.
def SignInResult(request):
    return render(request, 'SignIn.html')


def SignUpResult(request):
    return render(request, 'SignUp.html')
