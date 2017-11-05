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
    Renders the template for a particular stage given a stage_id
    """
    stage = Stage.objects.get(pk=request.POST['pk'])
    template = stage.get_stage_url()
    context = {'pkid':request.POST['pk']}
    return render_to_response(template, context=context)


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
    """
    Renders the list of challenges to the user.
    """
    user = request.user
    # give user access to level 1 if they cannot
    if len(user.level_set.all()) == 0:
        UserLevel.objects.create(user=user, level=Level.objects.get(pk=1))

    # hardcoding unlocking new levels

    # level 2 completed -> unlock level 3
    if _completed_stages(user, 2) >= 2:
        _grant_level(user, 3)
    # level 1 completed -> unlock level 2
    elif _completed_stages(user, 1) >= 3:
        _grant_level(user, 2)


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
    context_instance = RequestContext(request)
    pkid = request.POST['pkid']
    user = request.user
    stage = Stage.objects.get(pk=pkid)
    try:
        UserStage.objects.all.get(user=user, stage=stage)
    except:
        UserStage.objects.create(user=user, stage=stage)

    return view_list(request)


def _completed_stages(user, level_id):
    """
    Returns number of completed stages in a level given a level id and a
    user
    """
    levels_of_completed_stage = [x.level_id for x in user.stage_set.all()]

    return levels_of_completed_stage.count(level_id)


def _has_level(user, level_id):
    for level in user.level_set.all():
        if level.id == level_id:
            return True
    return False


def _grant_level(user, level_id):
    if not _has_level(user, level_id):
        UserLevel.objects.create(user=user,
                                 level=Level.objects.get(pk=level_id))
