from django.db import models
from django.utils.translation import ugettext_lazy as _

platform_arch = (
	(1, 'i386'),
	(2, 'amd64'),
)

platform_system = (
	(1, 'Linux'),
	(2, 'Windows'),
)

class Platform(models.Model):
	arch = models.IntegerField(choices=platform_arch)
	system = models.IntegerField(choices=platform_system)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	def full_name(self):
		return platform

	class Meta:
		verbose_name = _('Platform')
		verbose_name_plural = _('Platforms')

class Version(models.Model):
	major = models.IntegerField()
	minor = models.IntegerField()
	patch = models.IntegerField()
	vtype = models.CharField(max_length=10)

	def __str__(self):
		return "v%d.%d.%d-%s" % (self.major, self.minor, self.patch, self.vtype)

	class Meta:
		verbose_name = _('Version')
		verbose_name_plural = _('Versions')

class File(models.Model):
	name = models.CharField(max_length=60)
	platform = models.ForeignKey(Platform, null=True)
	version = models.ForeignKey(Version, null=True)
	filename = models.FileField()
	downloads = models.IntegerField(default=0, editable=False)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('File')
		verbose_name_plural = _('Files')
