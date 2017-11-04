from django.template import loader
from django.http import HttpResponse


def view_stage(request, stage_id):
    template = loader.get_template('stage_'+ stage_id +'.html')
    context = {}
    return HttpResponse(template.render(context, request))
