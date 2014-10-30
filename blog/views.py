from django.core.urlresolvers import reverse
from django.shortcuts import render
from blog.models import *
from django.views.generic import View, DetailView
from django.http import HttpResponseRedirect, HttpResponse, Http404
from blog.forms import *

# Create your views here.


class IndexView(View):
	template_name = 'blog/index.html'

	def get(self, request, *args, **kwargs):
		
		if kwargs.get("tag_pk"):
			latest_records = Tag.objects.get(pk=int(kwargs["tag_pk"])).record_set.order_by('-date_creation')
		elif kwargs.get("thread_pk"):
			latest_records = Thread.objects.get(pk=kwargs["thread_pk"]).record_set.order_by('-date_creation')
		else:
			latest_records = Record.objects.order_by('-date_creation')
		
		categories = Category.objects.all()
		context = {'latest_records': latest_records, 'categories': categories}
		return render(request, self.template_name, context)



def like(request):
	if request.is_ajax():
		try:
			record_pk = int(request.POST['record_pk'])
			is_like = request.POST['is_like'] == "true"
		except KeyError:
			return HttpResponse('Error')

		record = Record.objects.get(pk=record_pk)
		
		if is_like:
			record.likes = record.likes + 1
			Record.save(record)
			return HttpResponse(record.likes)
		else:
			record.dislikes = record.dislikes + 1
			Record.save(record)
			return HttpResponse(record.dislikes)

	else:
		raise Http404


def record(request, pk):

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			text = form.cleaned_data['text']
			author = form.cleaned_data['author']
			author_email = form.cleaned_data['author_email']
			record = Record.objects.get(pk=pk)
			c = Comment(text=text, author=author, author_email=author_email, record=record)
			c.save()

	else:
		form = CommentForm()

	context = {}
	(context['record'], ) = Record.objects.get(pk=pk),

	context['comments'] = Record.objects.get(pk=pk).comment_set.order_by('-date_creation')
	context['form'] = form
	
	return render(request, 'blog/record.html', context)