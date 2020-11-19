import pandas as pd

PATH = "C:\\Users\\User\\Desktop\\allin_tasks\\Pandas Exercise\\Automobile_data.csv"


def question1():
    df = pd.read_csv(PATH)
    print(df.head(5))

    print(df.tail(5))


def question2():
    df = pd.read_csv(PATH, na_values={
        'price': ["?", "n.a"],
        'stroke': ["?", "n.a"],
        'horsepower': ["?", "n.a"],
        'peak-rpm': ["?", "n.a"],
        'average-mileage': ["?", "n.a"]})
    print(df)

    df.to_csv(PATH)


def question3():
    df = pd.read_csv(PATH)
    df = df[['company', 'price']][df.price == df['price'].max()]
    print(df)


def question4():
    df = pd.read_csv(PATH)
    car_manufacturers = df.groupby('company')
    toyota = car_manufacturers.get_group('toyota')
    print(toyota)


def question5():
    df = pd.read_csv(PATH)
    counts = df['company'].value_counts()
    print(counts)


def question6():
    df = pd.read_csv(PATH)
    car_manufacturers = df.groupby('company')
    price_df = car_manufacturers['price'].max()
    print(price_df)


def question7():
    df = pd.read_csv(PATH)
    car_manufacturers = df.groupby('company')
    mileage = car_manufacturers['company', 'average-mileage'].mean()
    print(mileage)


def question8():
    df = pd.read_csv(PATH)
    df = df.sort_values(by=['price'], ascending=False)
    print(df.head(5))


def question9():
    german_cars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
    cars_df1 = pd.DataFrame.from_dict(german_cars)

    japanese_cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}
    cars_df2 = pd.DataFrame.from_dict(japanese_cars)

    cars_df = pd.concat([cars_df1, cars_df2], keys=["Germany", "Japan"])
    print(cars_df)


def question10():
    car_price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
    car_price_df = pd.DataFrame.from_dict(car_price)
    car_horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
    cars_horsepower_df = pd.DataFrame.from_dict(car_horsepower)

    cars_df = pd.merge(car_price_df, cars_horsepower_df, on="Company")
    print(cars_df)


