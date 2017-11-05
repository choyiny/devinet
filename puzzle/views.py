from django.shortcuts import render_to_response
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


from .models import Level

from puzzle.models import Stage


@csrf_exempt
def view_stage(request):
    """
    Renders the template for a particular stage given a stage_id,
    if the user has the required permissions for it
    """

    template = Stage.objects.get(pk=request.POST['pk']).get_stage_url()
    context = {}
    return render_to_response(template, context=context)


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def view_home(request):
    template = 'home.html'
    context = {}

    return render_to_response(template, context=context)

def view_list(request):
    template = 'list.html'
    context = {'level1': get_object_or_404(Level, pk=1),
               'level2': get_object_or_404(Level, pk=2),
               'level3': get_object_or_404(Level, pk=3)}

    return render_to_response(template, context=context)
