from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from . import models
from django.http import HttpResponseRedirect

# Create your views here.


# Index- Telas iniciais
class Home(TemplateView):
    template_name='iniciais/inicial.html'

class Forum(ListView):
	model = models.Forum
	template_name = 'mensagens/forum.html'

	def get_context_data(self, **kwargs):
		kwargs['respostas'] = models.Respostas.objects.all()
		return super(Forum, self).get_context_data(**kwargs)


class AdicionarRespotas(DetailView):
	models = models.Forum
	template_name = 'mensagens/resposta.html'


	def get_context_data(self, **kwargs):
		if 'enviar' in self.request.GET:
			models.Respostas.objects.create(user=self.request.user, mensagens=self.request.GET['resposta'], forum=self.request.GET['obje'])
		kwargs['respostas'] = models.Respostas.objects.all()
		return super(AdicionarRespotas, self).get_context_data(**kwargs)


class TimeLine(ListView):
	model = models.Arts
	template_name = 'post/time_line.html'

	def get_queryset(self):
		return models.Arts.objects.all()


class Animes(ListView):
	model = models.Anime
	template_name='post/anime.html'

	def get_quaryset(self):
		return models.Anime.objects.all()


class CriarArte(CreateView):
	model = models.Arts
	template_name='post/CriarArte.html'
	fields = ['titulo', 'descricao', 'anime', 'foto']

class CriarForum(CreateView):
	model = models.Forum
	template_name='post/CriarForum.html'
	fields = ['descricao', 'assunto']

	
		
		
