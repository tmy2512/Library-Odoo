from odoo import models, fields, api

from email.policy import default
from server.odoo.tools.populate import compute


class LibraryAuthor(models.Model):
    _name = 'library.author'

    name = fields.Char(string='Author Name', required=True, index=True)
    biography = fields.Text(string='Biography')
    date_of_birth = fields.Date(string='Date of Birth')
    nationality = fields.Char(string='Nationality')
    books = fields.Many2many('library.book', string='Books')
    rank_type = fields.Selection(
        [('obscure', 'Obscure '), ('rising_star', 'Rising Star '), ('well_known', 'Well-Known')], compute='_set_rank_type_as_book_quantity', index=True )

    @api.depends('books')
    def _set_rank_type_as_book_quantity(self):
        for record in self:
            book_count = len(record.books)
            if book_count == 0:
                record.rank_type = 'obscure'
            elif 0 < book_count <= 5:
                record.rank_type = 'rising_star'
            else:
                record.rank_type = 'well_known'

