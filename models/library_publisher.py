from odoo import models, fields

class LibraryPublisher(models.Model):
    _name = 'library.publisher'

    name = fields.Char(string='Publisher Name', required=True, index=True)
    address = fields.Text(string='Address')
    books = fields.One2many('library.book', 'publisher_id', string='Books')