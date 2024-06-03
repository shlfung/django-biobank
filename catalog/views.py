from django.shortcuts import render

# Create your views here.

from .models import Participant, Program

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_participants = Participant.objects.all().count()
    num_programs = Program.objects.all().count()
    #num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    context = {
        'num_participants': num_participants,
        'num_programs': num_programs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
