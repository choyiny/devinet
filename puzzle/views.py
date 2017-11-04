from django.template import loader
from django.http import HttpResponse
from .models import Level

from puzzle.models import Stage


def view_stage(request, stage_id):
    """
    Renders the template for a particular stage given a stage_id,
    if the user has the required permissions for it
    """
    template = loader.get_template(Stage.objects.get(pk=stage_id).get_stage_url)
    context = {}
    return HttpResponse(template.render(context, request))

def view_home(request):
    template = loader.get_template('home.html')
    context = {'levels':Level.objects.all()}

    return HttpResponse(template.render(context, request))