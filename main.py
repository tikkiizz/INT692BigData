import pandas as pd

def run():
    f_path = [
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Aotizhongxin_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Changping_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Dingling_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Dongsi_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Guanyuan_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Gucheng_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Huairou_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Nongzhanguan_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Shunyi_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Tiantan_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Wanliu_20130301-20170228.csv',
        'C:/Users/user/Downloads/PRSA2017/PRSA/PRSA_Data_Wanshouxigong_20130301-20170228.csv',
    ]
    for i, f in enumerate(f_path):

        df = pd.read_csv(f)
        df = df.drop(['No'], axis=1)
        df = df.drop(['station'], axis=1)
        df = df[df['year'] >= 2016]
        df = df[df['PM2.5'].notnull()]
        df = df[df['PM10'].notnull()]
        df = df[df['SO2'].notnull()]
        df = df[df['NO2'].notnull()]
        df = df[df['CO'].notnull()]
        df = df[df['O3'].notnull()]
        df = df[df['TEMP'].notnull()]
        df = df[df['PRES'].notnull()]
        df = df[df['DEWP'].notnull()]
        df = df[df['RAIN'].notnull()]
        df = df[df['wd'].notnull()]
        df = df[df['WSPM'].notnull()]

        y = pd.get_dummies(df['wd'], prefix='wd')
        # df = df.drop(['wd'], axis=1)
        df = pd.concat([df, y], axis=1)

        if i == 0:
            df.to_csv('C:/Users/user/Downloads/PRSA2017/PRSA/PRSA.csv', columns=df.columns, index=False)
        else:
            df.to_csv('C:/Users/user/Downloads/PRSA2017/PRSA/PRSA.csv', header=False, index=False, mode='a')


if __name__ == '__main__':
    run()

