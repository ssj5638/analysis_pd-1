import matplotlib.pyplot as plt
import pandas as pd

def graph_scatter(result_analysis):
    fig, subplots = plt.subplots(1, len(result_analysis), sharey=True)
    print(fig)
    print(subplots)

    for index, result in enumerate(result_analysis):        # enumerate에서 index받을 수 있음
        subplots[index].set_xlabel('{0}인 입국자 수'.format(result['country_name']))
        index == 0 and subplots[index].set_ylabel('관광지 입장객 수')
        subplots[index].set_title('r={:.5f}'.format(result['r']))     # .5f 소수점 포함 5자리
        subplots[index].scatter(result['x'], result['y'], c='black', s=6)
    plt.subplots_adjust(wspace=0)   # 여백 줄이기
    plt.show()


def graph_scatter_2(result_analysis):
    print(result_analysis)

    graph_table = pd.DataFrame(result_analysis, columns=['tourist_spot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tourist_spot')

    graph_table.plot(kind='bar')
    plt.show()