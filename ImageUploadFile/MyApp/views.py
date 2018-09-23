from django.shortcuts import render
from MyApp.forms import ProfileForm
from MyApp.models import Profile

# Create your views here.
def loginn(request):
    return render(request,"profile.html",{})

def SaveProfile(request):
    
    name1=request.POST.get("name")
    picture1=request.FILES['picture']
    print("asfddsafsafsafdsdsafsf" , name1)
    print("fj;lsakfjsakjfaslj" , picture1)
    obj=Profile(name=name1,picture=picture1)
    obj.save()
    pic=Profile.objects.all()
    formpic={"pickey":pic}
    return render(request,"saved.html",formpic) 
   
    
    