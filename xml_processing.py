from lxml import etree
from glob import glob
from tqdm import tqdm
import csv
import re


def search_in_xml(dirpath):
    with open("efrsb.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['№', 'Огрн', 'Инн', 'Дата банкротства'])

        n = 0
        prefix_map = {"xsi": 'http://www.w3.org/2001/XMLSchema-instance'}

        regex = re.compile(r".{4}-.{2}-.{2}")

        for year in glob(dirpath + '/*'):

            for file in tqdm(glob(year+'/*.xml'), desc="Files"):
                root = etree.parse(file).getroot()

                for elem in root.findall(""".//Bankrupt[@xsi:type="Bankrupt.Company.v2"]""", prefix_map):
                    ogrn_elem = elem.find('./Ogrn')
                    ogrn = ogrn_elem.text if ogrn_elem is not None else ''
                    inn_elem = elem.find('./Inn')
                    inn = inn_elem.text if inn_elem is not None else ''
                    publish_date_elem = elem.find('../PublishDate')
                    publish_date = publish_date_elem.text if publish_date_elem is not None else ''
                    publish_date = regex.match(publish_date)[0]

                    writer.writerow([n, ogrn, inn, publish_date])
                    n += 1


if __name__ == '__main__':
    search_in_xml(r'\\192.168.100.50\usershare\dmitriy.chernykh@ecotomsk.com\crispdm\ЕФРСБ')
