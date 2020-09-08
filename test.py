import unittest
from unittest.mock import patch
from main import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        update_date()

    def test_check_doc_exist(self):
        self.assertEqual(check_document_existance('11-2'), True)

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_owner_name(self, mock_input):
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    def test_all_doc_owners(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})

    def test_remove_doc_from_shelf(self):
        self.assertNotEqual(remove_doc_from_shelf('11-2'), directories)

    def test_add_new_shelf(self):
        new_shelf = 4
        self.assertEqual(add_new_shelf(new_shelf), (new_shelf, new_shelf in directories.keys()))

    def test_append_doc_to_shelf(self):
        doc_number = 12345
        shelf_number = 4
        append_doc_to_shelf(doc_number, shelf_number)
        self.assertIn(doc_number, directories[shelf_number])

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_input):
        delete_doc()
        self.assertFalse(check_document_existance('11-2'))

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual(get_doc_shelf(), '1')

    def test_move_doc_to_shelf(self):
        res = 'Документ номер 11-2 был перемещен на полку номер 2'
        self.assertEqual(move_doc_to_shelf('11-2', '2'), res)

    def test_show_all_documents_info(self):
        for document in documents:
            self.assertEqual(show_document_info(document), f'{document["type"]} "{document["number"]}" "{document["name"]}"')

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('666', 'visa', 'Dmitry Putin', '3'), '3')

if __name__ == '__main__':
    unittest.main ()
