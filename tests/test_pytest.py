import app
import pytest


class TestFunction:

    @classmethod
    def setup_class(cls):
        cls.test_doc = {
            "type": "test_doc",
            "number": "test_number",
            "name": "test_owner"
        }

        cls.test_shelf_number = "test_shelf_number"

        #app.documents.append(cls.test_doc)

    def test_add_new_doc(self):
        assert app.add_new_doc(TestFunction.test_doc, TestFunction.test_shelf_number) == TestFunction.test_shelf_number
        assert TestFunction.test_doc in app.documents
        assert TestFunction.test_shelf_number in app.directories
        assert TestFunction.test_doc["number"] in app.directories[TestFunction.test_shelf_number]

    def test_show_document_info(self):
        assert app.show_document_info(TestFunction.test_doc) == tuple(TestFunction.test_doc.values())

    """
    #протестировано в add_new_doc
    def test_add_new_shelf(self): 
        assert app.add_new_shelf(TestFunction.test_shelf_number)
        assert TestFunction.test_shelf_number in app.directories

    #протестировано в add_new_doc
    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf(TestFunction.test_doc["number"], TestFunction.test_shelf_number)
        assert TestFunction.test_doc["number"] in app.directories[TestFunction.test_shelf_number]
    """

    def test_get_doc_owner_name(self):
        assert app.get_doc_owner_name(TestFunction.test_doc["number"]) == TestFunction.test_doc["name"]

    def test_get_all_doc_owners_names(self):
        assert TestFunction.test_doc["name"] in app.get_all_doc_owners_names()

    def test_get_doc_shelf(self):
        assert app.get_doc_shelf(TestFunction.test_doc["number"]) == TestFunction.test_shelf_number

    def test_delete_doc(self):
        assert app.delete_doc(TestFunction.test_doc["number"])
        assert TestFunction.test_doc not in app.documents
        assert TestFunction.test_doc["number"] not in app.directories[TestFunction.test_shelf_number]


    @pytest.mark.parametrize("doc_number, exist", [
        ("11-2", True),
        ("test_number", False)
    ])
    def test_check_document_existance(self, doc_number, exist):
        assert app.check_document_existance(doc_number) == exist


    @classmethod
    def teardown_class(cls):
        app.directories.pop(TestFunction.test_shelf_number, None)
        #на случай если не сработало штатное удаление документа delete_doc
        for current_document in app.documents:
            if current_document == TestFunction.test_doc:
                app.documents.remove(current_document)

