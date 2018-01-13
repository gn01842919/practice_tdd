from django.test import TestCase
from lists.forms import ItemForm, EMPTY_ITEM_ERR


class ItemFormTest(TestCase):

    def test_form_item_input_has_placehodler_and_css_classes(self):
        form = ItemForm({'text': ''})
        self.assertFalse(form.is_valid())

        self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERR])

