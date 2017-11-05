from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from .models import Level

from puzzle.models import Stage, UserStage, UserLevel


@csrf_exempt
def view_stage(request):
    """
    Renders the template for a particular stage given a stage_id,
    if the user has the required permissions for it
    """

    template = Stage.objects.get(pk=request.POST['pk']).get_stage_url()
    context = {'pkid':request.POST['pk']}
    # render the stage if user has permission
    if request.POST['pk'] in request.user.user_level_set:
        return render_to_response(template, context=context)
    else:
        raise Http403("You cannot access this stage yet")


def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def view_home(request):
    template = 'home.html'
    context = {}

    return render_to_response(template, context=context)

@csrf_exempt
def view_list(request):
    # give user access to level 1 if they cannot
    if len(request.user.level_set.all()) == 0:
        UserLevel.objects.create(user=request.user, level=Level.objects.get(pk=1))

    template = 'list.html'
    user = request.user
    unlocked_levels = [x.id for x in user.level_set.all()]
    completed_stages = [x.id for x in user.stage_set.all()]
    context = {'level1': get_object_or_404(Level, pk=1),
               'level2': get_object_or_404(Level, pk=2),
               'level3': get_object_or_404(Level, pk=3),
               'unlocked_levels': unlocked_levels,
               'completed_stages': completed_stages
               }

    return render_to_response(template, context=context)

@csrf_exempt
def setStageStatus(request):
    context_instance=RequestContext(request)
    pkid = request.POST['pkid']
    user = request.user
    stage = Stage.objects.get(pk=pkid)
    UserStage.objects.create(user=user, stage=stage)

    return view_list(request)
