from django.shortcuts import render, redirect

import uuid #random unique number generator
from .models import Url #databse

from django.http import HttpResponse #ajax response
# Create your views here.

# homepage
def index(request):

    return render(request,'index.html')

# ajax form sumbmission logic, and saving full url and unique uuid number
def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5] #generate a unique uuid number with limit 5

        # saving into 'Url' database
        Url_db = Url(link=url,uuid=uid) # model object creating and assinging values
        Url_db.save()

        return HttpResponse(uid)

def linkloader(request,pk):

    try:

        try:
            Url_db = Url.objects.get(uuid=pk)
            counter=Url_db.count

            if (counter >= 10):
                Url_db.delete()
                print('Main url deleted')
            else:
                Url_db.count=counter+1 # increamenting 'count' value in db
                print(Url_db.count)
                print(type(Url_db.count))
                Url_db.save()
                print('url count increamented')
        
        except:
            return HttpResponse('<div style="text-align: center;margin-top: 50px;"><h1>Url Expired</h1><a href="/">Back</a></div>')
    
        return redirect(Url_db.link) # load main url

    except:
        return HttpResponse('<div style="text-align: center;margin-top: 50px;"><h1>Not Secure Url</h1><a href="/">Back</a></div>')