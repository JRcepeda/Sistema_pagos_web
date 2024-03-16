from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.db import IntegrityError #errores propios de la base de datos
from django.contrib.auth.decorators import login_required# decorador para proteger la funcion /ruta
# Create your views here.
#def hello(request):
#    #return HttpResponse('Hello!!')
#    return render(request,'signup.html',{'form':UserCreationForm})
#se define lo que se mostrara en la pagína
def signup(request):
    print("paila prin")
    if request.method=='GET':#cuando recarga la pagina
        print('paila')
        return render(request,'signup.html',{'form':UserCreationForm})
        #print('Enviando Formulario')
    else:
        print(request.POST)
        if request.POST['password1']==request.POST['password2']:
            print("paila 2")
            #si la contraseñas coinciden se crea un usuario y una contraseña
            #luego se guarda en la base de datos    
            try:
                user=User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                #una sesion en django es una cookie que almacena datos de usuario
                #login crea ua cookie con datos de usuario
                #con la cookie se peude saber que tareas fueronc readas por el usuario
                # tambien ver a que páginas tiene acceso
                login(request,user)
                return redirect('/tasks') 
            except IntegrityError:
                #('El usuario ya existe')
                return render(request,'signup.html',
                              {'form':UserCreationForm,
                               'error':'el usuario ya existe'})
        
        else:
            
            return render(request,'signup.html',
                              {'form':UserCreationForm,
                               'error':'La contraseñas no coinciden'})
#        print('Obteniendo datos')


def signout(request):#salir de la aplicacion
    logout(request)
    return redirect('logi')

def logi(request):# entrar a la aplicacion
    #al igual que signup se comprueba si se envia datos o se esta cargando la página
    if request.method=='GET':
        return render(request,'logi.html',{'form':AuthenticationForm})
    else:
        #se comprueba el usuario si es valido authenticate devuelve el usuario si no es vacio
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'logi.html',{'form':AuthenticationForm,'error':'Usuario o Contraseña incorrecta'})
        else:
            #guarda sesion del usuario con login
            login(request,user)
            return redirect('/tasks')
        #print(request.POST)
   