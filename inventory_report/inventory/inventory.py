import csv
import json
from xml.etree import ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    @classmethod
    def import_data(cls, path, report):
        if path.endswith("csv"):
            return cls.csv_reports(path, report)

        if path.endswith("json"):
            return cls.json_reports(path, report)

        if path.endswith("xml"):
            return cls.xml_reports(path, report)

    @classmethod
    def csv_reports(cls, path, report):
        with open(path) as file:
            file_reader = list(csv.DictReader(file))
            if report == "simples":
                return SimpleReport.generate(file_reader)
            if report == "completo":
                return CompleteReport.generate(file_reader)

    @classmethod
    def json_reports(cls, path, report):
        with open(path) as file:
            file_reader = json.loads(file.read())
            if report == "simples":
                return SimpleReport.generate(file_reader)
            if report == "completo":
                return CompleteReport.generate(file_reader)

    @classmethod
    def xml_reports(cls, path, report):
        tree = ET.parse(path)
        root = list(tree.getroot())
        file_reader = []
        info_dict = {}

        for index in range(len(root)):
            for info in root[index]:
                info_dict[info.tag] = info.text
            file_reader.append(info_dict)
            info_dict = {}

        if report == "simples":
            return SimpleReport.generate(file_reader)
        if report == "completo":
            return CompleteReport.generate(file_reader)
