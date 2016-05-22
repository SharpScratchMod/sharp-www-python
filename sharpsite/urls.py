from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

urlpatterns = [
    #---Static Pages---#
    # /
    ##url(r'^$', views.page_home),'

    #---Projects---#
    # /projects/#/
    url(r'^projects/(?P<project_id>[0-9]+)/$', views.projects_view),
    # /projects/#/locale/lang_list.txt
    url(r'^projects/(?P<project_id>[0-9]+)/locale/lang_list\.txt$', views.projects_lang),
    # /projects/#/admin_censor_uncensor/
    url(r'^projects/(?P<project_id>[0-9]+)/admin_censor_uncensor/$', views.projects_admin_censor_toggle),
    # /projects/#/delete/
    url(r'^projects/(?P<project_id>[0-9]+)/delete/$', views.projects_delete),
    # /create/
    url(r'^create/$', views.projects_create),
    # /create/do/
    url(r'^create/do/$', views.projects_create_do),

    #---Users---#
    # /users/*/
    ##url(r'^users/(?P<username>\w+)/$', views.users_view),

    #---Teams---#
    # /new_team/
    url(r'^new_team/$', views.team_create),
    # /teams/*/
    url(r'^teams/(?P<team_id>[a-zA-Z0-9\-_]+)/$', views.team_view),
    # /teams/*/manage/
    url(r'^teams/(?P<team_id>[a-zA-Z0-9\-_]+)/manage/$', views.team_manage),

    #---Admin---#

    #---Tests---#
    url(r'^tests/testpage$', views.testpage),
]
