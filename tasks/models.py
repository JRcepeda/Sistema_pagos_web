from django.db import models,connection


# Create your models here tablas.

#ejecuta proceso de pago creado en postgresql
def consult_sql(documento):
    with connection.cursor() as cursor:
        
        sql=f"CALL PAGO('{documento}',{7600})"
        sql2=f"SELECT SALDO FROM SALDO_ESTUDIANTE WHERE CEDULA='{documento}'"
        cursor.execute(sql)
        notice=cursor.connection.notices
        cursor.execute(sql2)
        
        saldo=cursor.fetchall()
        cursor.connection.commit()
    return notice,saldo

def consult_sql2(documento):
    with connection.cursor() as cursor:
        sql=f"SELECT SALDO FROM SALDO_ESTUDIANTE WHERE CEDULA='{documento}'"
        cursor.execute(sql)
        respuesta=cursor.fetchall()
    return respuesta

def consult_sql3(d1,d2):
    with connection.cursor() as cursor:
        sql=f"SELECT TOTAL_RECIBIDO('{d1}','{d2}');"
        print(sql)
        cursor.execute(sql)
        respuesta=cursor.fetchall()
    return respuesta

def consult_sql4(documento,fecha):
    with connection.cursor() as cursor:
        sql=f"SELECT MONTO,REFERENCIA,ERROR_PRINC FROM TRANSACCIONES_RECHAZADAS WHERE TO_CHAR(FECHA_CONSIGNACION,'YYYY-MM-DD') IN ('{fecha}') AND CEDULA='{documento}';"
        print(sql)
        cursor.execute(sql)
        respuesta=cursor.fetchall()
    return respuesta

