from django.db import models
from django.contrib.auth.models import User

from polit.models import *

class PolitComment(models.Model):
	politician = models.ForeignKey(Politician)
	comment = models.TextField()

	def __str__(self):
		

class Evaluation(models.Model):
	name = models.CharField(max_lenght=100)

	def __str__(self):
		return self.name

class UserEvaluation(models.Model):
	user = models.ForeignKey(User)
	comment = models.ForeignKey(PolitComment, related_name="evaluation")
	source = models.TextField()
	evaluation = models.ForeignKey(Evaluation)

def merge_comments(id, ids):
	fpc = PolitComment.objects.get(id=id)
	for mid in ids:
		mpc = PolitComment.objects.get(id=mid)
		for eval in mpc.evaluation.all():
			eval.comment = fpc
			eval.save()
		mpc.delete()
