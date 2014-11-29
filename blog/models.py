from django.db import models
from django.utils.translation import ugettext_lazy as _
from markdown import markdown as md

class Category(models.Model):
	name = models.CharField(max_length=35)
	slug = models.SlugField(max_length=35)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Posts\' category')
		verbose_name_plural = _('Posts\' categories')

class Label(models.Model):
	name = models.CharField(max_length=35)
	slug = models.SlugField(max_length=35)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Label')
		verbose_name_plural = _('Labels')

class Post(models.Model):
	title = models.CharField(_('Title'), max_length=200)
	slug = models.SlugField()
	lead = models.CharField(_('Lead'), max_length=500)
	content = models.TextField(_('Content'))
	category = models.ForeignKey(Category, verbose_name = _('Category'))
	labels = models.ManyToManyField(Label, verbose_name = _('Labels'))
	pub_date = models.DateTimeField(_('Publication date'))
	published = models.BooleanField(_('Is published?'), default=False)

	def __str__(self):
		return self.title
	
	def parsed_lead(self):
		return md(self.lead)
	parsed_lead.allow_tags = True
	parsed_lead.is_safe = True
	
	def parsed(self):
		return md(self.content)
	parsed.allow_tags = True
	parsed.is_safe = True

	class Meta:
		verbose_name = _('Post')
		verbose_name_plural = _('Posts')
		ordering = ['-pub_date']

