from flask import Flask, render_template, request
from wtforms import Form, StringField, EmailField, PasswordField, SubmitField, validators

app = Flask("meuapp")

class FormCadastro(Form):
    class Meta:
        csrf = True
        
    nome=StringField('Nome')
    email=EmailField('Seu e-mail' )
    password=PasswordField(
        'Sua senha',
        [validators.equal_to('passwordConfirm', message=' As senhas são diferentes'),
         validators.length(min=5, max=20, message='O tamanho precisa ser entre %(min)d e %(max)d')
         ])
    passwordConfirm=PasswordField('Confirme sua senha' )

    btn = SubmitField('criar')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    form = FormCadastro(request.form)

    if request.method == 'POST' and form.validate():
        return 'OK'

    return render_template('cadastro.html', form=form)

app.run()