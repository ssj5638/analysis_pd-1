import json
import pandas as pd
import scipy.stats as ss


def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as infile:
        json_data=json.loads(infile.read())
        # print(json_data)

    tourspotvisitor_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])    #해당 데이터만
    # print(tourspotvisitor_table)

    temp_tourspotvisitor_table = pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum())        # date를 기준으로 그룹화

    # print(temp_tourspotvisitor_table)
    results=[]
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data=json.loads(infile.read())

        # tourspotvisitor_table=pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        # print(tourspotvisitor_table)

        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        foreignvisitor_table = foreignvisitor_table.set_index('date')
        merge_table = pd.merge(temp_tourspotvisitor_table, foreignvisitor_table, left_index=True, right_index=True)

        x = list(merge_table['visit_count'])
        y = list(merge_table['count_foreigner'])

        country_name = foreignvisitor_table['country_name'].unique().item(0)
        r = ss.pearsonr(x, y)[0] # scipy라이브러리 => r = np.corrcoe(x, y)[0] numpy 라이브러리
        results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})

    return results

