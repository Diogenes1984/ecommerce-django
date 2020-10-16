from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(
        label='Nome',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome completo'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite seu email'
            }
        )
    )
    assunto = forms.CharField(
        label='Assunto',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Assunto'
            }
        )
    )
    mensagem = forms.CharField(
        label='Mensagem',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Assunto'
            }
        )
    )

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        n = 'Nome'
        e = 'E-mail'
        a = 'Assunto'
        m = 'Mensagem'

        conteudo = f'Nome: {n}\n'
        f'E-mail: {e}\n'
        f'Assunto: {a}\n'
        f'Mensagem: {m}'

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email='contato@fusion.com.br',
            to=['contato@fusion.com.br', ],
            headers={'Replay-To': email}
        )
        mail.send()
