import collect
import analyze
import visualize
from config import CONFIG

if __name__ == '__main__':
    resultfiles = dict()
    #collect
    resultfiles['tourspot_visitor'] = collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        # start_year=CONFIG['common']['start_year'],
        # end_year=CONFIG['common']['end_year']
        **CONFIG['common'])

    resultfiles['foreign_visitor'] = []
    for country in CONFIG['countries']:
        rf = collect.crawling_foreign_visitor(country, **CONFIG['common'])
        resultfiles['foreign_visitor'].append(rf)

    # # 1. analysis and visualize
    # result_analysis = analyze.analysis_correlation(resultfiles)
    # print(result_analysis)
    #
    # # 2. analysis and visualize
    # visualize.graph_scatter(result_analysis)


    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)      # 장소별로 상관계수 구하기기

    visualize.graph_scatter_2(result_analysis)
