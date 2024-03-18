from django.shortcuts import render,redirect
from .models import consult_sql,consult_sql2,consult_sql3,consult_sql4

# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required#para que no cualquiera la pueda acceder a menos de que sea un usuario 
def fuente(request):
    #request es la peticion
    return render(request,'consultas.html')

#peticion de pago
def datos_sql(request):
    if request.method=='POST':

        try:
            notice,saldo=consult_sql(request.POST['documento'])
            saldo=[f"${saldo[0][0]:,.0f}"]
            return render(request,'consultas.html',{'notice':notice,'saldo':[f"El saldo es: {saldo[0]}"]})
        except:
            return render(request,'consultas.html',{'notice':['Digite un numero de documento'],'saldo':[0]})
     
    else:     
        return render(request,'consultas.html')


#peticion de saldo

def datos_sql2(request):
    if request.method=='POST':

        try:
            resultado=[f"${consult_sql2(request.POST['documento'])[0][0]:,.0f}"]
            return render(request,'consultas.html',{'estado':[f"El saldo es: {resultado[0]}"]})
        except:
            return render(request,'consultas.html',{'estado':['Digite un número de documento']})
    else:
        return render(request,'consultas.html')

def datos_trans(request):
    if request.method=='GET':
        return render(request,'transacciones.html')
    else:

        try:
            resultado=f"${consult_sql3(request.POST['fecha1'],request.POST['fecha2'])[0][0]:,.0f}"           
            return render(request,'transacciones.html',{'resultado':resultado})        
        except:
            return render(request,'transacciones.html',{'resultado':'Sin fondos'})
def datos_trans2(request):
    if request.method=='GET':
        return render(request,'transacciones.html')
    else:
        if request.POST['documento']!=None or request.POST['fecha']!=None:
            
            try:
            # locale.setlocale(locale.LC_ALL,'es_CO.UTF-8')           
                resultado=consult_sql4(request.POST['documento'],request.POST['fecha'])[0]
                print(resultado)
                resultado=f"El documento {request.POST['documento']} tiene una transacción rechazada con la referencia {resultado[1]} con el valor de {resultado[0]:,.0f} debido a que, presenta la inconsistencia: {resultado[2]}"

                return render(request,'transacciones.html',{'Res':resultado})
            except:
                #return render(request,'transacciones.html',{'Res':resultado})
                return render(request,'transacciones.html')
        
        else:
            return render(request,'transacciones.html')
        

  
'''  if request.POST['fecha1']==None:
        print(request.POST['fecha1'])
        #return render(request,'fuente')

    else:
        resultado=consult_sql2(request.POST['fecha'])
        print('aqui')
        print(resultado)
        #return redirect('/tasks/')
        return render(request,'consultas.html',{'estado':resultado})
'''
