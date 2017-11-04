from django.template import loader
from django.http import HttpResponse

from puzzle.models import Stage


def view_stage(request, pk):
    """
    Renders the template for a particular stage given a stage_id,
    if the user has the required permissions for it
    """

    template = loader.get_template(Stage.objects.get(pk=pk).get_stage_url())
    context = {}
    return HttpResponse(template.render(context, request))


def view_home(request, user_id):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))