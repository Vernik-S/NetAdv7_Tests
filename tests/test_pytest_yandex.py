from YaCreator import YaCreator
import pytest


class TestYandex:

    @classmethod
    def setup_class(cls):
        cls.test_dir_name = "Netology_test_dir"

    def test_create_dir(self):
        with open("..\yandex_token.txt") as token_file:
            token = token_file.read()

        test_yandex = YaCreator(token)

        test_dir_name = TestYandex.test_dir_name
        assert test_yandex.create_dir(test_dir_name) == 201
        assert test_yandex.create_dir(test_dir_name) == 409 #отрицательный тест при попытке создания существующей папки
        assert "disk:/"+test_dir_name in test_yandex.get_dir_list()
        test_yandex.del_dir(test_dir_name)

    @pytest.mark.xfail()
    def test_create_empty_dir(self):
        with open("..\yandex_token.txt") as token_file:
            token = token_file.read()

        test_yandex = YaCreator(token)
        assert test_yandex.create_dir("") == 201

    @pytest.mark.xfail()
    def test_create_no_authentication(self):
        test_yandex = YaCreator("")
        assert test_yandex.create_dir(TestYandex.test_dir_name) == 201
