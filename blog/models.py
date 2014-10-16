from django.db import models



class Category(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name



class Tag(models.Model):
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name



class Thread(models.Model):
	title = models.CharField(max_length=140)
	description = models.CharField(max_length=140, null=True)
	author = models.CharField(max_length=30, null=True)
	author_email = models.EmailField(null=True)
	date_creation = models.DateTimeField()
	status = (
		('P', 'posted'),
		('C', 'closed'),
	)
	priority = (
		('L', 'low'),
		('M', 'medium'),
		('H', 'high'),
	)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.title




class Record(models.Model):
	title = models.CharField(max_length=140)
	content = models.TextField()
	author = models.CharField(max_length=30)
	author_email = models.EmailField(null=True)
	date_creation = models.DateTimeField(null=True)
	status = (
		('P', 'posted'),
		('C', 'closed'),
	)
	thread = models.ForeignKey(Thread)
	priority = (
		('L', 'low'),
		('M', 'medium'),
		('H', 'high'),
	)
	tags = models.ManyToManyField(Tag)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)

	def __str__(self):
		return self.title



