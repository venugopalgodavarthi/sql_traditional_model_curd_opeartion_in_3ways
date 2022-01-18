from django.http import HttpResponse
from django.shortcuts import render
import pymysql

dbconn = pymysql.connect(user='root',password='root',host='localhost',port=3306,db='cbpro7')
cus=dbconn.cursor()

def sample(request):
    print(dbconn)
    cus.execute('create table student(id int primary key, name varchar(20), email varchar(30))')
    return HttpResponse('tables is created')

def insert(request):
    cus.execute('insert into student (id, name, email) values (1,"sai","sai@gmail.com")')
    res=cus.rowcount
    dbconn.commit()
    return HttpResponse('{} row is insert '.format(res))

def dyinsert(request,id,name,email):
    val=[id,name,email]
    cus.execute('insert into student(id,name,email) values (%s,%s,%s)',val)
    res=cus.rowcount
    dbconn.commit()
    return HttpResponse('{} row is insert '.format(res))


def finsert(request):
    if request.method=='GET':
        if len(request.GET) != 0:
            val=[request.GET.get('id'),request.GET.get('name'),request.GET.get('email')]
            cus.execute('insert into student(id,name,email) values (%s,%s,%s)',val)
            dbconn.commit()
            return HttpResponse('{} row is insert '.format(cus.rowcount)) 
    return render(request,'insert.html')


def select(request):
    cus.execute('select * from student')
    res=cus.fetchall()
    return render(request,'select.html',{'res':res})
    

def update(request):
    cus.execute('update student set email="saikumar@gmail.com" where id=1 ')
    res=cus.rowcount
    dbconn.commit()
    return HttpResponse('{} row is update '.format(res))

def dyupdate(request,id,name,email):
    val=[name,email,id]
    cus.execute('update student set name=%s, email=%s where id=%s',val)
    res=cus.rowcount
    dbconn.commit()
    return HttpResponse('{} row is update '.format(res))


def fupdate(request,data):
    if request.method=='GET':
        if len(request.GET) != 0:
            val=[request.GET.get('name'),request.GET.get('email'),request.GET.get('id')]
            cus.execute('update student set name=%s, email=%s where id=%s',val)
            dbconn.commit()
            return HttpResponse('{} row is update'.format(cus.rowcount)) 
    
    val=[data]
    cus.execute('select * from student where id=%s',val)
    res=cus.fetchone()
    return render(request,'update.html',{'i':res})

def delete(request):
    cus.execute('delete from student where id=1')
    res=cus.rowcount
    dbconn.commit()
    return HttpResponse('{} row is deleted '.format(res))

def dydelete(request,id):
    val=[id]
    cus.execute('delete from student where id=%s',val)
    res=cus.rowcount
    dbconn.commit()
    return HttpResponse('{} row is deleted '.format(res))

def fdelete(request):
    if request.method=='GET':
        if len(request.GET) != 0:
            val=[request.GET.get('id')]
            cus.execute('delete from student where id=%s',val)
            dbconn.commit()
            return HttpResponse('{} row is delete'.format(cus.rowcount)) 
    return render(request,'delete.html')
    
    