import pandas as pd

data = pd.read_csv('data.csv')
running = True



def information():
    print(data.shape)
    data.info()
    print(data.head())

def mean_medium_mode():

    bmidata = data[(data['BMI']  >= 34.5) & (data['BMI'] <= 37.0)]
    print(bmidata.shape)
    bmidata.to_csv('bmidata.csv')
    print('here is the sorted data....')
    print(bmidata)
    print(bmidata.mean())
    print('the medium of the data is......')
    print(bmidata.median())
    print('The mode of the data is.......')
    print(bmidata.mode())

def compare():

    print('Here are the values for each Pregnancies......')
    print(data['Pregnancies'].value_counts())
    print('the comparison with Pregnancies and diabeties are the following.......')
    print(data.value_counts(subset=['Pregnancies', 'Outcome']))

def group_by():
    print('The mean for each number of Pregnancies are .........')
    print(data.groupby('Pregnancies').mean())
    print('the min of data with Pregnancies lined with outcome of diabeties tests are......')
    print(data.groupby(['Pregnancies', 'Outcome']).min())

while running == True:
    print('Welcome to the Pandas  example program.')
    print('Please pick an option')
    print('*' * 20)
    print('Press i for information')
    print('Press m ffor mean, medium and mode')
    print('press c for comparison')
    print('press g for group by example')
    print('press q to quit')
    print('please type in a input' + '*' * 10)
    option = input().lower()
    
    if option.lower() == 'i':
        information()
    elif option.lower() == 'm':
        mean_medium_mode()
    elif option.lower() == 'c':
        compare()
    elif option.lower() == 'g':
        group_by()
    elif option.lower() == 'q':
        running = False
