import pandas as pd


def read_dataset(dataset_file_name):
    
    raw_df = pd.read_csv(f'datasets\{dataset_file_name}')

    return raw_df


def get_total_consumption_over_time(df, country_name, time_start, time_end):

    df = df.loc[df['LOCATION'] == country_name]

    dfThTon = df.loc[df['MEASURE'] == 'THND_TONNE']
    dfThTon.drop(['LOCATION', 'MEASURE'], axis=1, inplace=True)

    dfThTon_over_time = dfThTon.loc[(dfThTon['TIME'] >= time_start) & (dfThTon['TIME'] <= time_end)]
    dfThTon_over_time = dfThTon_over_time.groupby(by = ['SUBJECT']).Value.sum()

    dfThTon_over_time_dict = dfThTon_over_time.to_dict()
    dfThTon_over_time_dict =  {k.lower(): round(v,3) for k, v in dfThTon_over_time_dict.items()}

    return dfThTon_over_time_dict



def get_country_stat(country_name, time_start, time_end):

    dataset_file_name = 'meat_consumption_worldwide.csv'
    df = read_dataset(dataset_file_name)

    consumption_over_time = get_total_consumption_over_time(df, country_name, time_start, time_end)

    return consumption_over_time




# print('\n\n-------------------------\n\n')
# print(stat_1)
# print('\n\n-------------------------\n\n')