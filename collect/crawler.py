from .api import api


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
#        for month in range(1, 13):
        for month in range(1, 5):
            data = api.pd_fetch_foreign_visitor(country[1], year, month)
            if data is None:
                continue

            preprocess_foreign_visitor(data)
            results.append(data)

    # save data to file
    print(results)

