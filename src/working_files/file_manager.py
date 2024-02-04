import os

from src.working_files.abc_file_manager import WorkingFiles
import json


class FileManager(WorkingFiles):

    def in_file(self, data: dict | list) -> None:
        """
        Запись json файла
        :param data: словарь с данными
        :return: None
        """
        try:
            with open(self.path, "w") as fp:
                json.dump(data, fp)
            # logger.info("[+] Function successfully")
        except Exception as error:
            # logger.error(f"[-] {error}")
            print(error)

    def out_file(self):
        """
        Чтение json файла
        :return: словарь с данными
        """
        try:
            with open(self.path, "r") as fp:
                account: dict = json.load(fp)
            # logger.info("[+] Function successfully")
            return account
        except Exception as error:
            # logger.error(f"[-] {error}")
            print(error)

    def del_file(self):
        try:
            os.remove(self.path)
            # logger.info("[+] Function successfully")

        except Exception as error:
            # logger.error(f"[-] {error}")

            print(error)


if __name__ == '__main__':
    FileManager().del_file()
    # FileManager()
