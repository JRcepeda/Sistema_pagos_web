from django.shortcuts import render,redirect
from .models import consult_sql,consult_sql2,consult_sql3,consult_sql4
import locale
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required#para que no cualquiera la pueda acceder a menos de que sea un usuario 
def fuente(request):
    #request es la peticion
    return render(request,'consultas.html')

#peticion de pago
def datos_sql(request):
    if request.method=='GET':
        return render(request,'consultas.html')
    else:
        try:
            notice,saldo=consult_sql(request.POST['documento'])
            locale.setlocale(locale.LC_ALL,'es_CO.UTF-8')
            saldo=[locale.currency(saldo[0][0],grouping=True)]
            return render(request,'consultas.html',{'notice':notice,'saldo':saldo})
        except:
            return render(request,'consultas.html',{'notice':['Digite un numero de documento'],'saldo':[0]})
      #      return render(request,'consultas.html',{'notice':notice,'saldo':saldo})

#peticion de saldo

def datos_sql2(request):
    if request.method=='GET':
        return render(request,'consultas.html')
    else:
        try:
         #   print(request.POST)#request.POST['documento']
            locale.setlocale(locale.LC_ALL,'es_CO.UTF-8')
            resultado=[locale.currency(consult_sql2(request.POST['documento'])[0][0],grouping=True)]
            #return redirect('/tasks/')
            return render(request,'consultas.html',{'estado':resultado})
        except:
            return render(request,'consultas.html',{'estado':['Digite un número de documento']})
def datos_trans(request):
    if request.method=='GET':
        return render(request,'transacciones.html')
    else:
        locale.setlocale(locale.LC_ALL,'es_CO.UTF-8')
        resultado=consult_sql3(request.POST['fecha1'],request.POST['fecha2'])[0][0]
        try:
            resultado=locale.currency(resultado,grouping=True)
            return render(request,'transacciones.html',{'resultado':resultado})        
        except:
            return render(request,'transacciones.html',{'resultado':'Sin fondos'})
def datos_trans2(request):
    if request.method=='GET':
        return render(request,'transacciones.html')
    else:
        try:
            locale.setlocale(locale.LC_ALL,'es_CO.UTF-8')

            
            resultado=consult_sql4(request.POST['documento'],request.POST['fecha'])[0]

            resultado=f"El documento {request.POST['documento']} tiene una transacción rechazada con la referencia {resultado[1]} con el valor de {locale.currency(resultado[0],grouping=True)} debido a que, presenta la inconsistencia: {resultado[2]}"
            return render(request,'transacciones.html',{'Res':resultado})
        except:
            return render(request,'transacciones.html')
      #  try:
      #      resultado=locale.currency(resultado,grouping=True)
       #     return render(request,'transacciones.html',{'resultado':resultado})        
       # except:
    #    return render(request,'transacciones.html',{'resultado':'Sin fondos'})

    #else:
#    print(request.POST['fecha1'])
# print(request.POST['fecha2'])
#        return render(request,'logi')
  

  
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
