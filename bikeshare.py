import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('\nPlease make sure to enter correct spelling as instructed and all lowercased :D !\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        city = input('\nPlease enter city :chicago, new york city, washington\n').lower()
        if city == 'chicago' or city=='new york city' or city=='washington':
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        month = input('\nPlease enter month :all, january, february, march, april, may, june\n').lower()
        if month == 'all' or month=='january' or month=='february' or month=='march' or month=='april' or month=='may' or month=='june':
            break
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day = input('\nPlease enter day :all, monday, tuesday, wednesday, thursday, friday, saturday, sunday\n').lower()
        if day == 'all' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day =='sunday':
            break

    
        print('-'*40)
    message = '\nAnalysis of {} file with {} months filtered and {} days filtered\n'
    print(message.format(city,month,day))
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
def getMonthName(number):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(number, "Invalid month")

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    m = df['month'].mode()[0]
    
    print('\nMost Common Month is :',getMonthName(m),'\n')
  #  print(m)

    # TO DO: display the most common day of week
    print('\nMost Common Day is :',df['day_of_week'].mode()[0],'\n')

    # TO DO: display the most common start hour
    print('\nMost Common Start hour is :',df['Start Time'].mode()[0].hour,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost Common Used Start Station is: ',df['Start Station'].mode()[0],'\n')

    # TO DO: display most commonly used end station
    print('\nMost Common Used End Station is: ',df['End Station'].mode()[0],'\n')

    # TO DO: display most frequent combination of start station and end station trip
    
    print('\nMost Frequent Used Combination of Start Station and End Station Trip is: ',(df['Start Station'] + ',' + df['End Station']).mode()[0],'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltime = df['Trip Duration'].sum()
    print('\nTotal Travel Time is: ',str(datetime.timedelta(seconds = int(totaltime))),'\n')

    # TO DO: display mean travel time
    meantime = df['Trip Duration'].mean()
    print('\nMean Travel Time is: ',str(datetime.timedelta(seconds = int(meantime))),'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual data? Enter yes or no\n').title()
    if view_data == 'No':
        return
    start_loc = 0
    view_s = 'yes'
    while(view_s != 'no'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_s = input('\nWould you like to view 5 further rows of individual data? Enter yes or no\n').title()
        if view_s == 'No':
            return
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of User Types:\n',df['User Type'].value_counts(),'\n')

    try:
        # TO DO: Display counts of gender
        print('\nCounts of Gender:\n',df['Gender'].value_counts(),'\n')

        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest Year of Birth ',int(df['Birth Year'].min()),'\nMost Recent Year of Birth ' ,int(df['Birth Year'].max()),'\nMost Common Year of Birth         ',int(df['Birth Year'].mode()[0]),'\n')
    except:
        print("\nWashington doesn't have gender and birth dates realted data\n")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
