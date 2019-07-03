from django.db import models

class Articles(models.Model):
	# """docstring for Articles"""
	# def __init__(self, arg):
	# 	super(Articles, self).__init__()
	# 	self.arg = arg
		
	title = models.CharField(max_length=120)
	post = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.title