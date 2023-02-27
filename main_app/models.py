from django.db import models


class BASIC_STRUCTURE(models.Model):

	name=models.CharField('Name',max_length=500)
	component_list = []
	install = models.TextField('Instalation')
	usage = models.TextField('Usage')
	review = models.TextField('Review')

	model_state = models.BooleanField(default=True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{}'.format(self.name)

class FULL_CODE(models.Model):

	zip_file = models.FileField('full_code_zip', upload_to='zips')

	model_state = models.BooleanField(default=True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{}'.format(self.zip_file)

# Create your models here.
class RB_CATEGO(models.Model):
	catego_name=models.CharField('Category Name', max_length=500)
	catego_resume=models.TextField('Resume')

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}'.format(self.catego_name,self.catego_resume)

class RB_SUBC(models.Model):
	subcatego_name=models.CharField('Subcategory Name', max_length=500)
	subcatego_resume=models.TextField('Resume')

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)
	def __str__(self):
		return '{} - {}'.format(self.subcatego_name,self.subcatego_resume)
class RB_TYPE(models.Model):
	generic_typo=models.CharField('Genéric Name', max_length=500)
	category=models.ForeignKey(RB_CATEGO,on_delete=models.DO_NOTHING)
	subcategory=models.ForeignKey(RB_SUBC,on_delete=models.DO_NOTHING)

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}/{}'.format(self.generic_typo,self.category,self.subcategory)

class C_CATEGO(models.Model):
	catego_name=models.CharField('Category Name', max_length=500)
	catego_resume=models.TextField('Resume')

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}'.format(self.catego_name,self.catego_resume)

class C_SUBC(models.Model):
	subcatego_name=models.CharField('Subcategory Name',max_length=200)
	subcatego_resume=models.TextField('Resume')

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)
	def __str__(self):
		return '{} - {}'.format(self.subcatego_name,self.subcatego_resume)
class C_TYPE(models.Model):
	generic_typo=models.CharField('Genéric Name', max_length=500)
	category=models.ForeignKey(C_CATEGO,on_delete=models.DO_NOTHING)
	subcategory=models.ForeignKey(C_SUBC,on_delete=models.DO_NOTHING)

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}/{}'.format(self.generic_typo,self.category,self.subcategory)

class COMPONENT(models.Model):
	name=models.CharField('Name', max_length=500)
	c_type=models.ForeignKey(C_TYPE, on_delete=models.DO_NOTHING)


	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}'.format(self.name,self.c_type)

class ROBOT(models.Model):
	name=models.CharField('Robot Name',max_length=500)
	slug=models.SlugField('Slug')
	resume=models.TextField('Resume')
	bot_type=models.ForeignKey(RB_TYPE,on_delete=models.DO_NOTHING)
	bot_code=models.ForeignKey(FULL_CODE,on_delete=models.DO_NOTHING)
	bot_comp=models.ForeignKey(COMPONENT,on_delete=models.DO_NOTHING)
	bot_struct=models.ForeignKey(BASIC_STRUCTURE, on_delete=models.DO_NOTHING)

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}'.format(self.name,self.bot_type)

class CODE(models.Model):

	robot=models.ForeignKey(ROBOT, on_delete=models.DO_NOTHING)
	code=models.CharField('Code',max_length=44)

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

class BASIC_LIBRARY(models.Model):

	name=models.CharField('Library Name',max_length=500)
	resume=models.TextField('Resume')
	code=models.FileField('Zip File')
	repository=models.URLField('Repository URL')

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{}'.format(self.name)

class BASIC_COMP(models.Model):

	comp=models.ForeignKey(COMPONENT, on_delete=models.DO_NOTHING)
	used_for=models.TextField()

	model_state = models.BooleanField(default = True)
	date_created = models.DateTimeField('Fecha de Creación', auto_now=False, auto_now_add=True)
	date_modified = models.DateTimeField('Fecha de Modificación', auto_now=True, auto_now_add=False)

	def __str__(self):
		return '{} - {}'.format(self.comp,self.used_for)