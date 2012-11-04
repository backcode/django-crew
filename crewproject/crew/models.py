from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import ObjectDoesNotExist
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class Team(TimeStampedModel):
	"""We are defining a team of people (group) which we will use to organize users."""
	name = models.CharField(_("Team Name"), max_length="30", null=True, blank=True)
	owner = models.OneToOneField(User)
    members = models.ManyToManyField(User, through='Membership')


class Role(TimeStampedModel):
	"""A Role is user defineable to give flexibility in how you structure your project."""
	name = models.CharField(_("Role"), max_length="30", null=True, blank=True)
	read = models.BooleanField(_("Read"))
	write = models.BooleanField(_("Write"))
	admin = models.BooleanField(_("Admin"))


class Membership(models.Model):
	"""This is the linking table for definig who is on a team and what their role on the team is.  A use may only have one Role per team."""
	user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
	role = models.ForeignKey(Role)

    class Meta:
        ordering = ['team__name', 'user__username']

    def __unicode__(self):
    	return "%s is a %s on %s" % (self.user, self.role, self.team)
