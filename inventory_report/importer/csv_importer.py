import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith("csv"):
            with open(file_name) as file:
                file_reader = list(csv.DictReader(file))
            return file_reader
        else:
            raise ValueError("Arquivo inválido")
