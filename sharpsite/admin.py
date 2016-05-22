from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserAlert)
admin.site.register(UserProfile)
admin.site.register(UserMessage)
admin.site.register(UserComment)
admin.site.register(Project)
admin.site.register(ProjectComment)
admin.site.register(Team)
admin.site.register(TeamRank)
admin.site.register(TeamMembers)
admin.site.register(TeamRankPermission)
admin.site.register(TeamComment)
admin.site.register(Report)
