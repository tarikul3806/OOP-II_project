from django.shortcuts import render,HttpResponse
from .models import contact
# Create your views here.
def index(request):

        if request.method == 'POST':
            index = contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            index.name=name
            index.email=email
            index.phone=phone
            index.message=message
            index.save()

        return render(request, 'index.html')