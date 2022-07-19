import time

import pandas as pd
import re


path = 'Z:\\dmitriy.chernykh@ecotomsk.com\\crispdm\\СПАРК 2020\\СПАРК_Выборка_компаний_20220617_1553.xlsx'


def read(path):
    data = pd.read_excel(
        path,
        sheet_name='report',
        engine='openpyxl',
        header=3,
    )

    regex = re.compile(r'(\d\d\d\d), (.+)')

    common_cols = []
    mapping = {}

    for column_name in data.columns:
        feature = regex.match(column_name)

        if feature:
            year = int(feature.group(1))

            if year not in mapping:
                mapping[year] = {}
            mapping[year][column_name] = feature.group(2)
        else:
            common_cols.append(column_name)

    result = None

    for y in mapping:
        df = data[common_cols + list(mapping[y].keys())]
        df = df.rename(columns=mapping[y])
        df['Year'] = y

        if result is not None:
            result = pd.concat([result, df])
        else:
            result = df

    return result


if __name__ == '__main__':
    start = time.time()
    x = read(path)
    print(x.head(3))
    print(x.shape)
    print(x.columns)
    print(time.time() - start)
