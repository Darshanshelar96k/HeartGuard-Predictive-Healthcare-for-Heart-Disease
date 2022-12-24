from django.http import HttpResponse
from django.shortcuts import render



# loading the saved model
 
#.......................................................
import numpy as np
import pickle     
      
def load_model():
    with open('heart_.pkl', 'rb') as file:
     data2 = pickle.load(file)
     return data2
data2 = load_model()
model2 = data2["model"]
le_sex = data2["le_sex"]
le_chest = data2["le_chest"]
le_ecg  = data2["le_ecg"]
le_ex  = data2["le_ex"]
le_slop  = data2["le_slop"]    


# Create your views here.
def index(request):
    return render(request,'index.html')


def predict(request):
    if request.method == "POST":
         print(request.method)
         age =int(request.POST.get('Age', False))
         sex =request.POST.get('gender', False)
         chest =request.POST.get('chestpaintype', False)
         rbp =int(request.POST.get('RestingBP', False))
         col =int(request.POST.get('Cholesterol', False))
         fast =int(request.POST.get('FastingBS', False))
         recg =request.POST.get('RestingECG', False)
         maxhr =int(request.POST.get('mhr',False))
         excer =request.POST.get('excer', False)
         old =float(request.POST.get('Oldpeak', False))
         slop =request.POST.get('ST_Slope', False)
         input_data= np.array([[age,sex,chest,rbp,col,fast,recg,maxhr,excer,old,slop]])
         input_ =input_data
         input_[:,1] = le_sex.fit_transform(input_data[:,1])
         input_[:,2] = le_chest.fit_transform(input_data[:,2])
         input_[:,6] = le_ecg.fit_transform(input_data[:,6])
         input_[:,8] = le_ex.fit_transform(input_data[:,8])
         input_[:,10] = le_slop.fit_transform(input_data[:,10])
         HeartDisease=model2.predict(input_)
         context = {"hd": HeartDisease}
         print(HeartDisease)
         return render(request,"predicted.html",context)
    return render(request,'predict.html')


def about(request):
    return render(request,"about.html")







# def heartpredict(request):
#   print (request.POST.dict())
#   age =int(request.POST.get('Age', False))
#   sex =request.POST.get('gender', False)
#   chest =request.POST.get('chestpaintype', False)
#   rbp =int(request.POST.get('RestingBP', False))
#   col =int(request.POST.get('Cholesterol', False))
#   fast =int(request.POST.get('FastingBS', False))
#   recg =request.POST.get('RestingECG', False)
#   maxhr =int(request.POST.get('mhr',False))
#   excer =request.POST.get('excer', False)
#   old =float(request.POST.get('Oldpeak', False))
#   slop =request.POST.get('ST_Slope', False)
#   input_data= np.array([[age,sex,chest,rbp,col,fast,recg,maxhr,excer,old,slop]])
#   input_ =input_data
#   input_[:,1] = le_sex.fit_transform(input_data[:,1])
#   input_[:,2] = le_chest.fit_transform(input_data[:,2])
#   input_[:,6] = le_ecg.fit_transform(input_data[:,6])
#   input_[:,8] = le_ex.fit_transform(input_data[:,8])
#   input_[:,10] = le_slop.fit_transform(input_data[:,10])
#   HeartDisease=model2.predict(input_)
#   return HttpResponse(HeartDisease)
  

