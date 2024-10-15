from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class LibraryBook(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Name', index=True)
    author_ids = fields.Many2many('library.author', string='Authors')
    genre_id = fields.Many2one('library.genre', string='Genres')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')
    publish_date = fields.Date(string='Publish Date')
    isbn = fields.Char(string='ISBN')
    price = fields.Float(string='Price')
    image_256 = fields.Image(string='Image')
    image_256_filename = fields.Char("Image Filename")
    created_time = fields.Datetime(string='Created Time', default=fields.Datetime.now)

    # @api.constrains('name', 'author_ids', 'genre_id', 'publisher_id', 'publish_date')
    # def _check_data(self):
    #     for record in self:
    #         if not record.name or not record.author_ids or not record.genre_id or not record.publisher_id:
    #             raise ValidationError("Please fill in all required fields.")
    #         if  record.publish_date > fields.Date.today():
    #             raise ValidationError("Publish date must be in the past!")

    # _sql_constraints = [
    #    ('name_code_unique', 'unique (name)', 'Name address already exists!'),
    # ]
    def change_name_book(self):
        for record in self:
            record.image_256_filename = 'Update Book Image'
    def action_add_record(self):
        # Logic xử lý thêm bản ghi
        new_record = self.create({
            'name': 'Bản Ghi Mới',
            'author_ids': [(0, 0, {
                'name': 'Tác Giả Mới',
            })]
        })

        # Xử lý reset lại fields
        for record in self:
            record.update({
                'name': False,
                'author_ids': [(5, 0, 0)],
                'genre_id': False,
                'publisher_id': False,
                'publish_date': False,
                'isbn': False,
                'price': False,
                'image_256': False,
                'image_256_filename': False,
            })

        # Thông báo cho người dùng
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'library.book',
            'res_id': new_record.id,
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'current',
        }
