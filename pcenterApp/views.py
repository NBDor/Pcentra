from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Url
from .forms import UrlForm

def create(request):
    
    template = 'urlshortcut/create.html'
    context = {}

    context['form'] = UrlForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        used_form = UrlForm(request.POST)

        if used_form.is_valid():
            url_object = used_form.save()
            new_url = request.build_absolute_uri('/s/') + url_object.shortcut
            full_link = url_object.full_link 
             
            context['new_url']  = new_url
            context['full_link'] = full_link
             
            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, query):

    try:
        url_object = Url.objects.get(shortcut=query)
        url_object.times_followed += 1        
        url_object.save()
        
        return HttpResponseRedirect(url_object.full_link)
        
    except:
        raise Http404('Error: url link is broken.')