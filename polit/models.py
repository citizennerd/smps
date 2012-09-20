from django.db import models

class AdministrativeRegion(models.Model):
	name = models.CharField(max_length=255)
	within = models.ForeignKey('AdministrativeRegion', null=True, blank=True)

class Role(models.Model):
	name = models.CharField(max_length=255)	

class Politician(models.Model):
	name = models.CharField(max_length=250)
	family_name = models.CharField(max_length=250)

class PoliticalEventType(models.Model):
	name = models.CharField(max_length=250)

class PoliticalEvent(models.Model):
	type = models.ForeignKey(PoliticalEventType)
	date = models.DateField()
	area = models.ForeignKey(AdministrativeRegion)
	role = models.ForeignKey(Role)

class Candidate(models.Model):
	politician = models.ForeignKey(Politician)
	political_event = models.ForeignKey(PoliticalEvent)
	elected = models.BooleanField(default=False)

