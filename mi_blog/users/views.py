from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import Profile as ProfileModel

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()

        return render(request, 'users/register.html',{'form': form})
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            
        return redirect('index')
        
def Profile(request, pk):
    if request.user.is_authenticated:
        profile = ProfileModel.objects.get(user_id=pk)
        return render(request, 'perfil.html', {"profile":profile})
    else:
        messages.success(request, ("Debes ingresar a tu cuenta para ver la pagina"))
        return redirect('index')
