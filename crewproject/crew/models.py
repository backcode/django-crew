from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import ObjectDoesNotExist
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class Team(TimeStampedModel):
	name = models.CharField(_("Team Name"), max_length="30", null=True, blank=True)
	owner = models.OneToOneField(User)
    members = models.ManyToManyField(User, through='Membership')


class Role(TimeStampedModel):
	name = models.CharField(_("Role"), max_length="30", null=True, blank=True)


class Membership(models.Model):
	user = models.ForeignKey(User)
    team = models.ForeignKey(Team)
    
	role = models.ForeignKey(Role)
