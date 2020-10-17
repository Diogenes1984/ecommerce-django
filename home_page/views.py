from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import ContatoForm
from django.contrib import messages


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


class ContactView(FormView):
    template_name = 'home_page/contact.html'
    success_url = reverse_lazy('contact')

    form_class = ContatoForm

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contato'
        context['content'] = 'Formulário de contato'
        context['obrigatorio'] = '* Campos obrigatórios'
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(ContactView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(ContactView, self).form_invalid(form, *args, **kwargs)
