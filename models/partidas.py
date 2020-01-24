# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class partidas(models.Model):
    _name="miro_daniel.partidas"
    _description = "Datos das partidas"
    _sql_constraints = [('xogadores distintos', 'CHECK(xogador_blancas != xogador_negras)', 'Non pode ser o mesmo xogador')]

    name = fields.Char(compute="_nombre", required = True, string="Name", store=True)
    xogador_blancas = fields.Many2one('miro_daniel.xogadores', string="Xogador con Blancas")
    xogador_negras = fields.Many2one('miro_daniel.xogadores', string="Xogador con Negras")
    data_partida = fields.Date(string="Data Partida", required=True, default=lambda self: fields.Date.today())
    resultado = fields.Selection([('Victoria Blancas', 'blancas'), ('Táboas', 'taboas'), ('Victoria Negras', 'negras')], string = 'Resultado')
    adxunto = fields.Char(string="Adxunto")
    fichero = fields.Binary(string="Arquivo png")



    @api.depends('xogador_blancas', 'xogador_negras', 'data_partida')
    def _nombre(self):
        for rexistro in self:
            if rexistro.xogador_blancas and rexistro.xogador_negras and rexistro.data_partida:
                rexistro.name=rexistro.data_partida.strftime("%d/%m/%Y")+" "+rexistro.xogador_blancas + rexistro.xogador_negras

    @api.constrains('data_partida')
    def _constrain_data(self):
        for rexistro in self:
            if rexistro.data_partida > fields.Date.today():
                raise ValidationError('A data da partida ten que ser menor a %s ' %fields.Date.today().strftime("%d do %m do %Y"))

