from django.http import HttpResponse
from django.template import loader
from .models import BirdSighting, SightingForm

def bird_sightings(request):
    if request.method == 'GET':
        my_bird_sightings = BirdSighting.objects.all().values()
        template = loader.get_template('sightings.html')
        page_data = {
            'sightings': my_bird_sightings,
            'form': SightingForm
        }
        return HttpResponse(template.render(page_data, request))
    
    if request.method=='POST':
        
        form=SightingForm(request.POST)
        if form.is_valid():
            sighting=form.save()

        my_bird_sightings = BirdSighting.objects.all().values()
        template = loader.get_template('sightings.html')
        page_data = {
            'sightings': my_bird_sightings,
            'form': SightingForm
        }
        return HttpResponse(template.render(page_data, request))