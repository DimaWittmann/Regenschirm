from django.shortcuts import render
from blog.models import *
from django.views.generic import View, DetailView
from django.http import HttpResponseRedirect, HttpResponse, Http404


# Create your views here.


class IndexView(View):
	template_name = 'blog/index.html'

	def get(self, request, *args, **kwargs):
		
		if kwargs.get("tag"):
			latest_records = Tag.objects.get(name=kwargs["tag"]).record_set.order_by('-date_creation')
		else:
			latest_records = Record.objects.order_by('-date_creation')
		categories = Category.objects.all()
		context = {'latest_records': latest_records, 'categories': categories}
		return render(request, self.template_name, context)


class RecordView(DetailView):
	model = Record
	template_name = 'blog/record.html'


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

