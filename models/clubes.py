# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class clubes (models.Model):
    _name="miro_daniel.clubes"
    _description = "Xestión de clubes"

    name = fields.Char(string="Nome do clube", store=True, required=True)
    telefono = fields.Char(string="Teléfono", size=9)
    nif = fields.Char(string="NIF", required=True)
    cod_rexistro = fields.Char(string="Código de Rexistro")
    local = fields.Text(string="Local de xogo(Enderezo)")
    localidade = fields.Char(string="Localidade")
    cod_postal = fields.Char(string="Código Postal", size=5)
    pais = fields.Many2one('res.country',
                           default=lambda self: self.env['res.country'].search([('name','=',"España")]),
                           string="País")
    id_pais = fields.Integer(related='pais.id')
    provincia = fields.Many2one('res.country.state',
                                string="Provincia",
                                default=lambda self: self.env['res.country.state'].search(
                                    [('name', '=', 'Pontevedra')], limit=1),
                                domain="[('country_id','=',id_pais)]")