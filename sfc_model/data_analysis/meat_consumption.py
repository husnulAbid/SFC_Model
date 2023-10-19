import pandas as pd


Current_year = 2023
dataset_file_name = 'meat_consumption_worldwide.csv'

def read_dataset(dataset_file_name):
    
    raw_df = pd.read_csv(f'datasets/{dataset_file_name}')
    raw_df = raw_df.loc[raw_df['TIME'] <= Current_year] 

    return raw_df


def get_all_type_consumption_over_time(df, country_name, time_start, time_end):
    df = df.loc[df['LOCATION'] == country_name]
    dfThTon = df.loc[df['MEASURE'] == 'THND_TONNE']
    dfThTon.drop(['LOCATION', 'MEASURE'], axis=1, inplace=True)

    dfThTon_over_time = dfThTon.loc[(dfThTon['TIME'] >= time_start) & (dfThTon['TIME'] <= time_end)]
    dfThTon_over_time = dfThTon_over_time.groupby(by = ['SUBJECT']).Value.sum()

    dfThTon_over_time_dict = dfThTon_over_time.to_dict()
    dfThTon_over_time_dict =  {k.lower(): round(v,3) for k, v in dfThTon_over_time_dict.items()}

    return dfThTon_over_time_dict



def get_country_stat_on_all_type_consumption(country_name, time_start, time_end):
    df = read_dataset(dataset_file_name)
    consumption_over_time = get_all_type_consumption_over_time(df, country_name, time_start, time_end)

    return consumption_over_time


def get_countries():
    df = read_dataset(dataset_file_name)
    available_countries = df['LOCATION'].unique().tolist()
    countries_dict = {'countries': available_countries}

    return countries_dict


def get_available_years():
    df = read_dataset(dataset_file_name)
    
    start_year = df['TIME'].min()
    end_year = df['TIME'].max()

    years_dict = {'start_year': str(start_year), 'end_year': str(end_year)}

    return years_dict


# print('\n\n-------------------------\n\n')
# print(stat_1)
# print('\n\n-------------------------\n\n')