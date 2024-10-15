odoo.define('library.new_book', function (require) {
    'use strict';

    var FormView = require('web.FormView');
    var core = require('web.core');

    var QWeb = core.qweb;

    // Kế thừa FormView để thêm validation
    FormView.include({
        // Override the 'on_save' function to add validation
        on_save: function (ev) {
            // Lấy dữ liệu từ form
            var title = this.$('input[name="name"]').val();
            var author = this.$('input[name="author_id"]').val();

            // Kiểm tra điều kiện
            if (!title || !author || !genre_id) {
                ev.preventDefault();
                console.log('kdkđjk')
                alert("Please fill in all required fields.");
                return;
            }

            // Nếu mọi thứ hợp lệ, gọi hàm cha để lưu
            this._super(ev);
            // Show a confirmation dialog after saving
            Dialog.alert(this, 'Book has been saved successfully!');
        }
    });
});
