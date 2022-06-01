from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import PhotoForm

# Create your views here.

def gallery(request):
    category = request.GET.get('category')
    somephotos=Photo.objects.all()
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
        
        
    categories = Category.objects.all()
    # photos = Photo.objects.all()
    
    context = {'categories': categories, 'photos':photos,'newphotos':somephotos}
    return render(request, 'photos/gallery.html', context   )

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photos/photo.html', {'photo': photo})

def addPhoto(request):  
    
    # categories = Category.objects.all()
    # context = {'categories': categories}
    form=PhotoForm()
    if request.method == 'POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(gallery)
        
    else:
        form=PhotoForm()
    return render(request, 'photos/add.html', {'form':form})
        
        
    
        # category=request.POST['category']
        # description=request.POST['description']
        # image = request.FILES.get('image')
        # new_photo=Photo(category=category,image=image,description=description)
        # new_photo.save()
        
        
        
        
        
        # if data['category'] != 'none':
        #     category = Category.objects.get(id=data['category'])    
        # elif data['category_new'] != '':
        #     category, created = Category.objects.get_or_create(name=data['category_new'])
        # else:
        #     category = None
            
        # photo = Photo.objects.create(
        #     category=category,
        #     description = data['description'],
        #     image = image,
        # )
def search_results(request):
    if 'cat' in request.GET and request.GET["cat"]:
        category = request.GET.get("cat")
        searched_images = Photo.objects.filter(category__name__icontains=category).all()
        message = f"{category}"
        
        return render(request, 'photos/search.html', {"message": message, "images": searched_images})   
            
    
    
    
