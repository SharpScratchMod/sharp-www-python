from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Users
class UserAlert(models.Model):
    msg = models.TextField()
    to = models.ForeignKey(User)
    from_user = models.ForeignKey(User, related_name="from+")
    dismissed = models.BooleanField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ban_alert = models.ForeignKey(UserAlert, null=True, blank=True)
    location = models.CharField(max_length=100)
    about_me = models.TextField()

class UserMessage(models.Model):
    msg = models.TextField()
    to = models.ForeignKey(User)

class UserComment(models.Model):
    owner = models.ForeignKey(User)
    message = models.TextField()
    user = models.ForeignKey(User, related_name="commented_on")

# Projects
class Project(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=500)
    notes = models.TextField()
    proj_credits = models.TextField()
    state = models.CharField(max_length=1) #u Unshared, s Shared, c Censored, d Deleted
    admin_notes = models.TextField()
    sharp_file = models.FileField(upload_to="projects")

class ProjectComment(models.Model):
    owner = models.ForeignKey(User)
    message = models.TextField()
    project = models.ForeignKey(Project)

# Teams
class Team(models.Model):
    tid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=500)
    notes = models.TextField()
    admin_notes = models.TextField()

class TeamRank(models.Model):
    team = models.ForeignKey(Team)
    name = models.TextField()
    invited = models.BooleanField()
    guest = models.BooleanField()
    blocked = models.BooleanField()

class TeamMembers(models.Model):
    member = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    rank = models.ForeignKey(TeamRank)

class TeamRankPermission(models.Model):
    delete_comments = models.BooleanField()
    add_comments = models.BooleanField()
    rm_member = models.BooleanField()
    demote_lower_member = models.BooleanField()
    demote_equal_member = models.BooleanField()
    demote_higher_member = models.BooleanField()
    promote_to_equal = models.BooleanField()
    promote_to_higher = models.BooleanField()
    invite_member = models.BooleanField()
    block_member = models.BooleanField()
    edit_ranks = models.BooleanField()
    delete_team = models.BooleanField()
    edit_notes = models.BooleanField()

    rank = models.OneToOneField(TeamRank)

class TeamComment(models.Model):
    owner = models.ForeignKey(User)
    message = models.TextField()
    team = models.ForeignKey(Team)

# Admin Stuff
class Report(models.Model):
    reporter = models.ForeignKey(User, related_name="reporter")
    reported = models.ForeignKey(User, related_name="reported")
    rtype = models.CharField(max_length=2)
    # p Project, t Team, u User, pc Project Comment, tc Team comment, uc User comment
    project = models.ForeignKey(Project, null=True, blank=True)
    team = models.ForeignKey(Team, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    project_comment = models.ForeignKey(ProjectComment, null=True, blank=True)
    team_comment = models.ForeignKey(TeamComment, null=True, blank=True)
    user_comment = models.ForeignKey(UserComment, null=True, blank=True)

#Materializecss
