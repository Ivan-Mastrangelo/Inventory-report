import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith("json"):
            with open(file_name) as file:
                file_reader = json.loads(file.read())
            return file_reader
        else:
            raise ValueError("Arquivo inválido")
