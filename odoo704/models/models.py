# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo704(models.Model):
#     _name = 'odoo704.odoo704'
#     _description = 'odoo704.odoo704'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class videojuego(models.Model):
	_name = 'odoo704.videojuego'
	_description = 'videojuego'

	name = fields.Char('id_videojuego',required=True)
	titulo= fields.Char(string='titulo',required=True)
	descripcion= fields.Char(string='descripcion',required=False)
	id_compania = fields.Char(string='id_compania',required=True)
	creador_videojuego_id=fields.Many2one('odoo704.creador',string='creador:')
	personaje_videojuego_id=fields.Many2many('odoo704.personaje','personaje_videojuego_id', string='personaje')
	videojuego_compania_ids=fields.Many2one('odoo704.compania', string='compania')



class creador(models.Model):
	_name = 'odoo704.creador'
	_description = 'creador'

	name = fields.Char('id_creador',required=True)
	nombre = fields.Char(string='nombre',required=True)
	apellidos= fields.Char(string='apellidos',required=False)
	videojuego_creador_ids=fields.One2many('odoo704.videojuego','creador_videojuego_id', string='videojuego:')



class personaje(models.Model):
	_name = 'odoo704.personaje'
	_description = 'personaje'

	name = fields.Char('id_personaje',required=True)
	nombre = fields.Char(string='Nombre',required=True)
	apellidos= fields.Char(string='Apellidos',required=True)

	# relaciones
	videojuego_personaje_id=fields.Many2many('odoo704.videojuego', string='videojuego:')
	personaje_frases_id=fields.One2many('odoo704.personaje_frases','frases_personaje_ids', string='personaje_frases')

class personaje_frases(models.Model):
	_name = 'odoo704.personaje_frases'
	_description = 'personaje_frases'

	name = fields.Char('id_frase',required=True)
	id_personaje = fields.Char(string='id_personaje',required=False)
	id_videojuego= fields.Char(string='id_videojuego',required=False)
	frase= fields.Char(string='frase',required=True)
	frases_personaje_ids=fields.Many2one('odoo704.personaje',string='frases')

	# relaciones


class compania(models.Model):
	_name = 'odoo704.compania'
	_description = 'compania'

	name = fields.Char('id_compania',required=True)
	nombre = fields.Char(string='nombre',required=True)
	direccion = fields.Char(string='direccion',required=True)

	compania_videojuego_ids=fields.One2many('odoo704.videojuego','videojuego_compania_ids',string='compania')


