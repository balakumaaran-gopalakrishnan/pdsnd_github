import time
import pandas as pd
import numpy as np
# first edit for udacity
# second edit for udacity
# third edit for udacity
# fourth edit for udacity
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DAY = { 'month': 'month',
              'day': 'day',
              'none': 'none' }
MONTH = { 'january': '1','february': '2', 'march': '3', 'april': '4','may': '5', 'june': '6'  ,'july': '7','august': '8', 'september': '9', 'october': '10','november': '11', 'december': '12'   }
DAY = { 'm': 'Monday','tu': 'Tuesday', 'w': 'Wednesday', 'th': 'Thursday','f': 'Friday', 'sa': 'Saturday' ,'su':'Sunday'   }

def city_input():
        #print('inside city')
        cityBool = False
        while True:    
            city=input('Would you like to see data for Chicago, New York, or Washington? \n')
            city=city.lower()
            #print(city)
            cityBool = city in CITY_DATA
            if cityBool == True:
                print('Looks like you want to hear about '+ city +'! if this is not true, restart the program ' )
                restart=input("Would you like to restart ? Type 'yes' or /'no'. \n" )
                if restart.upper() == 'YES' or restart.upper() == "Y":
                    main()
                
                return city
            else:
                print('\n*********Something went wrong, Please enter one of the below city\n')
                cityBool = False
                
def month_input():
        #print('inside month/day')
        month_dayBool = False
        while True:    
            month_day=input('\nWould you like to filter data by month, day, or not at all? Type "none" for no time filter.\n')
            month_day=month_day.lower()
            print(month_day)
            month_dayBool = month_day in MONTH_DAY
            if month_dayBool == True:
                
                
                if month_day == 'month':
                    print('Looks like you want to filter by '+ month_day +'! if this is not true, restart the program ' )
                    restart=input("Would you like to restart ? Type 'yes' or /'no'. \n" )
                    if restart.upper() == 'YES' or restart.upper() == "Y":
                        main()
                    
                    mon=input('\nwhich month ? January, February, March, April, May, or June ? Plese type out the full month name.\n')
                   
                    monLower=mon.lower()
                    monBool = monLower in MONTH
                    if monBool == True:
                        #print('month valid')
                        return month_day,mon
                    else:
                        print('\nPlease enter a valid input from the below\n')
                        print('-'*40)
                        month_input()
                    
                   
                elif month_day=='day':
                    print('Looks like you want to filter by '+ month_day +'! if this is not true, restart the program ' )
                    restart=input("Would you like to restart ? Type 'yes' or /'no'. \n" )
                    if restart.upper() == 'YES' or restart.upper() == "Y":
                        main()
                    
                    day=input('\nwhich day ? Please type a day M, Tu, W, Th, F, Sa, Su.\n')
                    print('-'*40)
                    dayLower=day.lower()
                    dayBool = dayLower in DAY
                    if dayBool == True:
                        return month_day,day
                        #print('returning to base')
                    else:
                        print('Please enter a valid input from the below')
                        month_input()
               
                elif month_day=='none':
                    print('Looks like you dont want to filter! if this is not true, restart the program ' )
                    restart=input("Would you like to restart ? Type 'yes' or /'no'. \n" )
                    if restart.upper() == 'YES' or restart.upper() == "Y":
                        main()
                    
                    month_day='none'
                    day='none'
                    return month_day,day
                                        
            
            else:
                print('*********Something went wrong, Please enter one of the below options')
                month_dayBool = False
            

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('-'*40)
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = city_input()         
        
    # TO DO: get user input for month (all, january, february, ... , june)
    mon_day_val,mon_day=month_input()
    #input(' Would you like to filter the data by month, day, or not at all? Type "none" for no time filter ')
    #print(city)

    
    print('-'*40)
    return city, mon_day_val, mon_day
	
def load_data(city, mon_day_val, mon_day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('Loading'+ city + '.......')
    df = pd.read_csv(CITY_DATA[city])
    #print(df.dtypes)
    #extracting from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month
    df["day_of_month"] = df["Start Time"].dt.day
    #print(df.dtypes)   
    #print(df.head())
    if mon_day_val == 'month':
        print('Data Loading for Month  ->'+ mon_day+'.....\n')
        #print(MONTH[mon_day])
        monfilter=int(MONTH[mon_day])
        #print(monfilter)
        df=df[df['month']==monfilter]
        return df 
    elif mon_day_val=='day':
        print('Data Loading for Day   ->'+ DAY[mon_day]+'......\n')
        #print(DAY[mon_day])
        dayfilter=(DAY[mon_day])
        df=df[df['day_of_week']==dayfilter]
        return df 
    else:
        return df    
    
def time_stats(df,mon_day_val):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    monthsDsply = ['january', 'february', 'march', 'april', 'may', 'june']
    
    if mon_day_val == 'month':
        print('Not Applicable since the selection is month ....')
        print('-'*40)
    elif mon_day_val=='day' :
        coMonth= int(df.month.mode()[0])
        popMonth = monthsDsply[coMonth - 1].capitalize()
        print('most common month ...'+str(popMonth))
        print('-'*40)
    else:
        coMonth= df.month.mode()[0]
        popMonth = monthsDsply[coMonth - 1].capitalize()
        print('most common month ...'+str(popMonth))
        print('-'*40)
        
    

    # TO DO: display the most common day of week
    if mon_day_val == 'day':
       print('Not Applicable since the selection is Day ....')  
       print('-'*40)
    elif mon_day_val=='month' :
        coDOW= df.day_of_week.mode()[0]
        print('most common day of week ...'+str(coDOW))
        print('-'*40)
    else:
        coDOW= df.day_of_week.mode()[0]
        print('most common day of week ...'+str(coDOW))
        print('-'*40)


    # TO DO: display the most common start 
    df['hour'] = df['Start Time'].dt.hour
    coStartTime= df.hour.mode()[0]
    print('most common start hour ...'+ str(coStartTime))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    coStartStation= df['Start Station'].mode()[0]
    print('most common start  station ...'+str(coStartStation))
    print('-'*40)

    # TO DO: display most commonly used end station
    coEndStation= df['End Station'].mode()[0]
    print('most common start  station ...'+str(coEndStation))
    print('-'*40)

    # TO DO: display most frequent combination of start station and end station trip
    FreqComb = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nmost frequent combination of start station and end station trip\n')
    print(FreqComb)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['TravelTime'] = df['End Time'] - df['Start Time']
    totTravelTime = np.sum(df['TravelTime'])
    print('total travel time.......'+str(totTravelTime))
    # TO DO: display mean travel time
    meanTravelTime = np.mean(df['TravelTime'])
    meanTravelTimeDays = str(meanTravelTime).split()
    print("mean travel time...... " + str(meanTravelTimeDays) + "  \n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Types of users: subscribers, customers, others\n')
    print(user_types)

    # TO DO: Display counts of gender
    if city=='washington':
        print('counts of gender.......')
        print(" N/A since the column is not available in  "+ city  )
    else:
        print('counts of gender')
        print(df['Gender'].value_counts())
        
    


    # TO DO: Display earliest, most recent, and most common year of birth
    if city=='washington':
        print(" N/A since the column is not available in  "+ city  )
    else:
        print('earliest, most recent, and most common year of birth........')
        earliest = np.min(df['Birth Year'])
        print ("\nearliest year of birth is " + str(earliest) + "\n")
        latest = np.max(df['Birth Year'])
        print ("latest year of birth is " + str(latest) + "\n")
        most_frequent= df['Birth Year'].mode()[0]
        print ("most frequent year of birth is " + str(most_frequent) + "\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():

        
        city, mon_day_val,mon_day = get_filters()        
        df = load_data(city, mon_day_val, mon_day)
        print(df.dtypes)
        time_stats(df,mon_day_val)        
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        
        restart = input("\nWould you like to do it again and perform another analysis? Type \'yes\' or \'no\'.\n")
        if restart.upper() == 'YES' or restart.upper() == "Y":
            main()
       
        
if __name__ == "__main__":
	main()
       