import json
import pandas as pd
import scipy.stats as ss
import matplotlib.pyplot as plt
import math

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
        foreignvisitor_table = foreignvisitor_table.set_index('date')   # date값으로 인덱스

        merge_table = pd.merge(temp_tourspotvisitor_table, foreignvisitor_table, left_index=True, right_index=True)
        print(merge_table)
        y = list(merge_table['visit_count'])
        x = list(merge_table['count_foreigner'])

        country_name = foreignvisitor_table['country_name'].unique().item(0)    # 중국/일본/미국
        r = ss.pearsonr(x, y)[0] # scipy라이브러리 상관계수  => r = np.corrcoe(x, y)[0] numpy 라이브러리
        results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})
        # print({'x': x, 'y': y, 'country_name': country_name, 'r': r})
        merge_table['visit_count'].plot(kind='bar')
        plt.show()

    return results

def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'],'r',encoding='utf-8') as infile:
        json_data = json.loads(infile.read())
        # print(json_data)
    tourspot_table = pd.DataFrame(json_data, columns=['count_foreigner', 'date', 'tourist_spot'])
    # print(tourspot_table)
    tourist_spot = tourspot_table['tourist_spot'].unique()
    print(tourist_spot)
    results = []
    for tourspot in tourist_spot:
        temp_table = tourspot_table[tourspot_table['tourist_spot'] == tourspot]
        temp_table = temp_table.set_index('date')
        # print(temp_table)
        # temp_tourspotvisitor_table = pd.DataFrame(temp_table.groupby('tourist_spot')['count_foreigner'].sum())
        # tourist_spot을 중심으로 방문자수 합하기 //
        r = []
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            foreignvisitor_table = foreignvisitor_table.set_index('date')
            # print(foreignvisitor_table)
            # temp_foreignvisitor_table = pd.DataFrame(foreignvisitor_table.groupby('country_name')['visit_count'].sum())
            # 나라별 한해동안의 방문자수
            merge_table = pd.merge(temp_table, foreignvisitor_table, left_index=True, right_index=True)
            # print(merge_table)

            y = list(merge_table['visit_count'])
            x = list(merge_table['count_foreigner'])

            tourist_spot = temp_table['tourist_spot'].unique().item(0)  # 관광지별
            print(tourist_spot)
            print(temp_table['tourist_spot'])
            r.append(analysis_correlation_by_torspot(x,y))
        results.append({'tourspot': tourist_spot, 'r_중국': r[0], 'r_일본': r[1], 'r_미국': r[2]})

    return results


def analysis_correlation_by_torspot(x,y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except Exception as e:
        r = 0.0

    return r