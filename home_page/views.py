from django.views.generic import TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'home_page/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Página Principal'
        context['content'] = 'Bem-vindo a página principal'
        return context


class AboutView(TemplateView):
    template_name = 'home_page/about.html'
    success_url = reverse_lazy('about')

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'Página Sobre'
        context['content'] = 'Bem-vindo a página sobre'
        return context


class ContactView(TemplateView):
    template_name = 'home_page/contact.html'
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(*kwargs)
        context['title'] = 'Página Contato'
        context['content'] = 'Bem-vindo a página contato'
        return context
