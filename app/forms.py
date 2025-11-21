from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ProdutoForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    preco = FloatField('Preço', validators=[DataRequired(), NumberRange(min=0)])
    quantidade = IntegerField('Quantidade', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Salvar')


class DeleteForm(FlaskForm):
    submit = SubmitField('Deletar')
