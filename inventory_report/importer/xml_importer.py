from xml.etree import ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        if file_name.endswith("xml"):
            tree = ET.parse(file_name)
            root = list(tree.getroot())
            file_reader = []
            info_dict = {}

            for index in range(len(root)):
                for info in root[index]:
                    info_dict[info.tag] = info.text
                file_reader.append(info_dict)
                info_dict = {}
            return file_reader
        else:
            raise ValueError("Arquivo inválido")
