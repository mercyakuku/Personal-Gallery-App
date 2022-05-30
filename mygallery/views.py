from django.shortcuts import render

# Create your views here.
def index(request):
    images = Image.get_all_images()
    locations = Location.objects.all()
    title = 'Kush Gallery App'

    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})