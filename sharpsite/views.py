from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import Http404
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.core.paginator import Paginator, InvalidPage
from django.utils import timezone
from .models import *
import json

IS_STAGING = False # On sandbox server
IS_DEV = True # On dev server
EXTRA = {"dev":IS_DEV,
         "staging":IS_STAGING,
         "url":"http://localhost:8000/"}
# Create your views here.
def testpage(request):
    template = loader.get_template("sharp/base.html")
    context = RequestContext(request, {
        "data": EXTRA,
        "auth": False,
        "user": request.user
    })
    return HttpResponse(template.render(context))

# Projects
def projects_view(request, project_id):
    try:
        template = loader.get_template("sharp/project_view.html")
        context = RequestContext(request, {
            "data": EXTRA,
            "auth": request.user.is_authenticated(),
            "user": request.user,
            "project": Project.objects.get(pk=project_id)
        })
        return HttpResponse(template.render(context))
    except Project.DoesNotExist:
        raise Http404

def projects_lang(request, project_id):
    return HttpResponse("te,Test lang")

def projects_admin_censor_toggle(request, project_id):
    try:
        if not request.user.is_staff or not request.user.is_superuser:
            raise PermissionDenied
        p = Project.objects.get(pk=project_id)
        if p.state == "u" or p.state == "s":
            p.state = "c"
        elif p.state == "c":
            p.state = "u"
        p.save()
        return redirect("/projects/" + project_id + "/")
    except Project.DoesNotExist:
        raise Http404

def projects_delete(request, project_id):
    try:
        p = Project.objects.get(pk=project_id)
        if not request.user.is_staff or not request.user.is_superuser or not p.owner == request.user:
            raise PermissionDenied
        p.name = ""
        p.notes = ""
        p.proj_credits = ""
        p.state = "d"
        p.admin_notes = "Deleted by " + request.user.username
        p.sharp_file.delete()
        p.save()
        return redirect("/projects/" + project_id + "/")
    except Project.DoesNotExist:
        raise Http404

def projects_create(request):
    template = loader.get_template("sharp/project_create.html")
    context = RequestContext(request, {
        "data": EXTRA,
        "auth": request.user.is_authenticated(),
        "user": request.user
    })
    return HttpResponse(template.render(context))

def projects_create_do(request):
    p = Project(
        owner=request.user,
        name="Untitled",
        notes="This is your awesome new project",
        proj_credits="The Sharp Scratch Mod Team",
        state="u",
        admin_notes="",
        sharp_file="test"
    )
    p.save()
    return HttpResponse("ok|"+str(p.id))

# Teams
def team_create(request):
    if request.method == "POST":
        if not Team.objects.filter(tid=request.POST['id']).count() == 0:
            return HttpResponse("fail")
        t = Team(tid=request.POST['id'],
                 name=request.POST['name'],
                 notes=request.POST['desc'],
                 admin_notes=""
                 )
        t.save()
        tr_o = TeamRank(team=t,
                      name="Owner",
                        invited=False,
                        guest=False,
                        blocked=False)
        tr_o.save()
        tr_a = TeamRank(team=t,
                        name="Admin",
                        invited=False,
                        guest=False,
                        blocked=False)
        tr_a.save()
        tr_m = TeamRank(team=t,
                        name="Member",
                        invited=False,
                        guest=False,
                        blocked=False)
        tr_m.save()
        tr_i = TeamRank(team=t,
                        name="Invited",
                        invited=True,
                        guest=False,
                        blocked=False)
        tr_i.save()
        tr_g = TeamRank(team=t,
                        name="Guest",
                        invited=False,
                        guest=True,
                        blocked=False)
        tr_g.save()
        tr_b = TeamRank(team=t,
                        name="Blocked",
                        invited=False,
                        guest=False,
                        blocked=True)
        tr_b.save()
        trp_o = TeamRankPermission(
            delete_comments=True,
            add_comments=True,
            rm_member=True,
            demote_lower_member=True,
            demote_equal_member=True,
            demote_higher_member=True,
            promote_to_equal=True,
            promote_to_higher=True,
            invite_member=True,
            block_member=True,
            edit_ranks=True,
            delete_team=True,
            edit_notes=True,
            rank=tr_o)
        trp_o.save()
        trp_a = TeamRankPermission(
            delete_comments=True,
            add_comments=True,
            rm_member=True,
            demote_lower_member=True,
            demote_equal_member=False,
            demote_higher_member=False,
            promote_to_equal=False,
            promote_to_higher=False,
            invite_member=True,
            block_member=True,
            edit_ranks=True,
            delete_team=False,
            edit_notes=True,
            rank=tr_a)
        trp_a.save()
        trp_m = TeamRankPermission(
            delete_comments=False,
            add_comments=True,
            rm_member=False,
            demote_lower_member=False,
            demote_equal_member=False,
            demote_higher_member=False,
            promote_to_equal=False,
            promote_to_higher=False,
            invite_member=False,
            block_member=False,
            edit_ranks=False,
            delete_team=False,
            edit_notes=False,
            rank=tr_m)
        trp_m.save()
        trp_g = TeamRankPermission(
            delete_comments=False,
            add_comments=True,
            rm_member=False,
            demote_lower_member=False,
            demote_equal_member=False,
            demote_higher_member=False,
            promote_to_equal=False,
            promote_to_higher=False,
            invite_member=False,
            block_member=False,
            edit_ranks=False,
            delete_team=False,
            edit_notes=False,
            rank=tr_g)
        trp_g.save()
        trp_i = TeamRankPermission(
            delete_comments=False,
            add_comments=True,
            rm_member=False,
            demote_lower_member=False,
            demote_equal_member=False,
            demote_higher_member=False,
            promote_to_equal=False,
            promote_to_higher=False,
            invite_member=False,
            block_member=False,
            edit_ranks=False,
            delete_team=False,
            edit_notes=False,
            rank=tr_i)
        trp_i.save()
        trp_b = TeamRankPermission(
            delete_comments=False,
            add_comments=False,
            rm_member=False,
            demote_lower_member=False,
            demote_equal_member=False,
            demote_higher_member=False,
            promote_to_equal=False,
            promote_to_higher=False,
            invite_member=False,
            block_member=False,
            edit_ranks=False,
            delete_team=False,
            edit_notes=False,
            rank=tr_b)
        trp_b.save()
        tm = TeamMembers(member=request.user,
                         team=t,
                         rank=tr_o)
        tm.save()
        return HttpResponse("ok")
    template = loader.get_template("sharp/team_create.html")
    context = RequestContext(request, {
        "data": EXTRA,
        "auth": request.user.is_authenticated(),
        "user": request.user
    })
    return HttpResponse(template.render(context))

def team_view(request, team_id):
    if Team.objects.filter(tid=team_id).count == 0:
        raise Http404
    if TeamMembers.objects.filter(member=request.user, team=Team.objects.get(tid=team_id)).count() == 0:
        mp = TeamRankPermission.objects.get(rank=Rank.objects.filter(guest=True)[0])
        r = Rank.objects.filter(guest=True)[0]
    else:
        mp = TeamRankPermission.objects.get(rank=TeamMembers.objects.get(member=request.user, team=Team.objects.get(tid=team_id)).rank)
        r = TeamMembers.objects.get(member=request.user, team=Team.objects.get(tid=team_id)).rank
    template = loader.get_template("sharp/team_view.html")
    context = RequestContext(request, {
        "data": EXTRA,
        "auth": request.user.is_authenticated(),
        "user": request.user,
        "team": Team.objects.get(tid=team_id),
        "member_perm": mp,
        "rank": r,
    })
    return HttpResponse(template.render(context))

def team_manage(request, team_id):
    if Team.objects.filter(tid=team_id).count == 0:
        raise Http404
    if TeamMembers.objects.filter(member=request.user, team=Team.objects.get(tid=team_id)).count() == 0:
        mp = TeamRankPermission.objects.get(rank=Rank.objects.filter(guest=True)[0])
        r = Rank.objects.filter(guest=True)[0]
    else:
        mp = TeamRankPermission.objects.get(rank=TeamMembers.objects.get(member=request.user, team=Team.objects.get(tid=team_id)).rank)
        r = TeamMembers.objects.get(member=request.user, team=Team.objects.get(tid=team_id)).rank
    template = loader.get_template("sharp/team_manage.html")
    context = RequestContext(request, {
        "data": EXTRA,
        "auth": request.user.is_authenticated(),
        "user": request.user,
        "team": Team.objects.get(tid=team_id),
        "member_perm": mp,
        "rank": r,
        "members": TeamMembers.objects.filter(team=Team.objects.get(tid=team_id)),
        "ranks": TeamRank.objects.filter(team=Team.objects.get(tid=team_id))
    })
    return HttpResponse(template.render(context))
