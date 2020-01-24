# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class xogadores(models.Model):
    _name = "miro_daniel.xogadores"
    _description = "Datos dos xogadores"

    name = fields.Char(compute="_nome_completo", store=True)
    nome = fields.Char(required=True, string="Nome")
    apelidos = fields.Char(required=True, string="Apelidos")
    clube = fields.Many2one('miro_daniel.clubes', string="Clube")
    elo = fields.Integer(string="ELO")
    telefono = fields.Char(string="Teléfono")
    data_nacemento = fields.Date(string="Data Nacemento", required=True)
    foto = fields.Binary(string="Foto")
    data_partida = fields.Date(string="Data Partida")
    xogador_blancas = fields.Char(string="Xogador con Blancas")
    xogador_negras = fields.Char(string="Xogador con Negras")
    resultado = fields.Char(string="Resultado")

    @api.depends('nome', 'apelidos')
    def _nome_completo(self):
        for rexistro in self:
            if rexistro.nome and rexistro.apelidos:
                rexistro.name = str(rexistro.nome) + " " + str(rexistro.apelidos)

    @api.constrains('data_nacemento')
    def _constrain_data(self):
        for rexistro in self:
            if rexistro.data_nacemento > fields.Date.today():
                raise ValidationError(
                    'A data de nacemento ten que ser menor a %s ' % fields.Date.today().strftime("%d do %m do %Y"))
