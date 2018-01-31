# from timeit import default_timer as timer
import numpy
import timeit
import gc

from pandas import DataFrame, Series

def create_medals_data_frame():
    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    olympic_medal_counts = {'country_name':countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    df = DataFrame(olympic_medal_counts)
    return df

def mean_from_DataFrame(df):
    return df.mean()

def mean_from_numpy(df):
    return df.apply(numpy.mean)

def filter_at_least_one_medal(df):
    return df[(df.gold + df.silver + df.bronze) > 0]

def countries_points(df):
     df['points'] = df[['gold','silver','bronze']].dot([4, 2, 1])
     return df[['country_name','points']]

print('Using df.mean()')
start = timeit.default_timer()
df = create_medals_data_frame()
df = filter_at_least_one_medal(df)
mean_from_DataFrame(df)
print(timeit.default_timer()-start)
#print(timeit.timeit('df.mean()', setup='gc.enable()', number=1, globals=globals()))

print('Using numpy.mean')
start = timeit.default_timer()
df = create_medals_data_frame()
df = filter_at_least_one_medal(df)
df = df[['gold','silver', 'bronze']]
mean_from_numpy(df)
print(timeit.default_timer()-start)
#print(timeit.timeit("df.apply(numpy.mean)", setup='gc.enable()', number=1, globals=globals()))

print('Country points')
df = create_medals_data_frame()
print(countries_points(df))
