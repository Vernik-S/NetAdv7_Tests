from YaCreator import YaCreator
import pytest


class TestYandex:

    def test_create_dir(self):
        with open("..\yandex_token.txt") as token_file:
            token = token_file.read()

        test_yandex = YaCreator(token)

        test_dir_name = "Netology_test_dir"
        assert test_yandex.create_dir(test_dir_name) == 201
        assert test_yandex.create_dir(test_dir_name) == 409 #отрицательный тест при попытке создания существующей папки
        assert "disk:/"+test_dir_name in test_yandex.get_dir_list()
        test_yandex.del_dir(test_dir_name)
