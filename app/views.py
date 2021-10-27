from django.shortcuts import render,redirect
from numpy import integer
from pandas.core.algorithms import value_counts
from .models import *
# import pandas as pd 
# import xlrd
import openpyxl
# Create your views here.

# def reg_user(request):
#     return render(request,"app/register.html")

# def user_upd(request,pk):
#     nk = user.objects.get(id=pk)
#     return render(request,"app/update.html",{'nk':nk})
def fileindex(request):
    ni= us_file.objects.all()
    for i in ni:
        print(i.id)
    return render(request,"app/fileindex.html",{'ni':ni}) 

def filepage(request):
    return render(request,"app/fileuplod.html") 

def abc(request,pk):
    f = us_file.objects.get(id=pk)
    return render(request,"app/readfille.html",{'f':f})

# def home(request):
#     ni = user.objects.all()
#     print(f"----{ni}")
#     return render(request,"app/index.html",{'ni':ni})

# def register(request):
#     if request.method == 'POST':
#         nam = request.POST['fn']
#         ph = request.POST['phone']
#         em = request.POST['email']
#         hy = request.POST['hobby']

#         asd = user.objects.create(
#             name =nam,
#             contect =ph,
#             email =em ,
#             Hobby = hy
#         )
#         return render(request,"app/fileuplod.html")

# def upd(request,pk):
#     if  request.method == 'POST':
#         xz = user.objects.get(id=pk)

#         xz.name =request.POST['fn']if request.POST['fn'] else xz.name
#         xz.Hobby =request.POST['hobby']if request.POST['hobby'] else xz.Hobby
#         xz.save()
#         return redirect('index')

# def dels(request,pk):
#     dls = user.objects.get(id=pk)
#     dls.delete()
#     return redirect('index')

def file_upd(request):
    if request.method == 'POST':
        ti= request.POST['title']
        f= request.FILES['fil']

        up = us_file.objects.create(
            titel= ti,
            o_file= f
        )  
        return redirect('file-index')




def exce_file(request,pk):
    if request.method == "POST":
        ab = us_file.objects.get(id=pk)
        # print(f"media/file{ab.o_file}")
        

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(ab.o_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'myapp/readfile.html', {"excel_data":excel_data})
    
        
    
   