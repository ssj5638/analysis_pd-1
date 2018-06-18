import collect
from config import CONFIG

if __name__ == '__main__':
    #collect
    collect.crawling_tourspot_visitor(
        district=CONFIG['district'],
        # start_year=CONFIG['common']['start_year'],
        # end_year=CONFIG['common']['end_year']
        **CONFIG['common'])

    for country in CONFIG['countries']:
            collect.crawling_foreign_visitor(country, **CONFIG['common'])

    #analysis

    #visualize