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

    #analysis
    result_analysis = analyze.analysis_correlation(resultfiles)
    print(result_analysis)
    #visualize
    visualize.graph_scatter(result_analysis)

