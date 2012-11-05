from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
from django.db import models
#from django.db.models import ObjectDoesNotExist
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


ROLE_CHOICES = (
    (0, 'Read'),
    (1, 'Write'),
    (2, 'Admin'),
)


class Crew(TimeStampedModel):
    """Defining a team of people (group) to be used to organize users."""
    name = models.CharField(_("Crew Name"), max_length="30", null=True, blank=True)
    owner = models.OneToOneField(User)
    members = models.ManyToManyField(User, through='Membership', related_name='+')
    slug = models.SlugField(_("Slug"), blank=True, null=True, max_length=255)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Crew, self).save(*args, **kwargs)
        if not self.slug:
            # TODO - make unique
            slug = slugify(self.name)
            #try:
            #    Step.objects.get(slug=slug, protocol=self.protocol)
            #    count = self.protocol.step_set.filter(slug=slug).count()
            #    self.slug = "{0}-{1}".format(slug, count)
            #except ObjectDoesNotExist:
            self.slug = slug
            self.save()



class Membership(models.Model):
    """This is the linking table for definig who is on a team and what their role on the team is.  A use may only have one Role per team."""
    user = models.ForeignKey(User)
    team = models.ForeignKey('crew.Crew')
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    class Meta:
        ordering = ['team__name', 'user__username']

    def __unicode__(self):
        return "%s is a %s on %s" % (self.user, self.role, self.team)
