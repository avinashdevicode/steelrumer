from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
# Create your models here.
class LinkCountManager(models.Manager):
	def get_query_set(self):
		return super(LinkCountManager, self).get_query_set().annotate(
			votes = Count('vote')).order_by('-votes')


class Link(models.Model):
	title = models.CharField("Head Line", max_length=250)
	submitter = models.ForeignKey(User)
	sumnitted_on = models.DateTimeField(auto_now_add = True)
	rank_score = models.FloatField(default=0.0)
	url = models.URLField("URL", max_length=250, blank=True)
	description = models.TextField(blank=True)
	with_votes = LinkCountManager()
	objects = models.Manager()

	def __unicode__(self):
		return self.title

class Vote(models.Model):
	voter = models.ForeignKey(User)
	link = models.ForeignKey(Link)

	def __unicode__(self):
		return "%s voted on %s" %(self.voter.username, self.link.title)

