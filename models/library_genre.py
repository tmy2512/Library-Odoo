from odoo import models, fields

class LibraryGenre(models.Model):
    _name = 'library.genre'

    name = fields.Char(string='Genre Name', required=True, index=True)
    description = fields.Text(string='Description', default='Description')
    books = fields.One2many('library.book', 'genre_id', string='Books')