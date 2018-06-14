import os
import json
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


def preprocess_foreign_visitor(data):
    # ed
    del data['ed']

    # edCd
    del data['edCd']

    # rnum
    del data['rnum']

    #나라 코드
    data['country_code'] = data['natCd']
    del data['natCd']

    #나라 이름
    data['country_name'] = data['natKorNm'].replace(' ', '')
    del data['natKorNm']

    #방문자 수
    data['visit_count'] = data['num']
    del data['num']

    # 년월
    if 'ym' not in data:
        data['date'] = ''
    else:
        data['date'] = data['ym']
        del data['ym']


def crawling_tourspot_visitor():
    pass


def crawling_foreign_visitor(country, start_year, end_year):
    results = []

    for year in range(start_year, end_year+1):
        for month in range(1, 13):
            data = api.pd_fetch_foreign_visitor(country[1], year, month)
            if data is None:
                continue

            preprocess_foreign_visitor(data)
            results.append(data)

    # save data to file
    filename = '%s/%s(%s)_foreignvisitor_%s_%s.json' % (RESULT_DIRECTORY, country[0], country[1], start_year, end_year)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)


if not os.path.exists(RESULT_DIRECTORY):
    os.makedirs(RESULT_DIRECTORY)
