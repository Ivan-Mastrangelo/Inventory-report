import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @classmethod
    def import_data(cls, path, report):
        with open(path) as file:
            file_reader = list(csv.DictReader(file))
            if report == "simples":
                return SimpleReport.generate(file_reader)
            if report == "completo":
                return CompleteReport.generate(file_reader)
