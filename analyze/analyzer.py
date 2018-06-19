import json
import pandas as pd


def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data=json.loads(infile.read())
        # print(json_data)

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])    #해당 데이터만
    # print(tourspotvisitor_table)

    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())        # date를 기준으로 그룹화
    # print(temp_tourspotvisitor_table)

    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data=json.loads(infile.read())

        tourspotvisitor_table=pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        print(tourspotvisitor_table)