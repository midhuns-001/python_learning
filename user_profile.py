

import requests as req
import datetime

def getFemaleUsersAgeGreaterThan45(data,  defaultAge = 45):
 
    ageCount = 0
    #for i in range (len(data)):
    for i, entry in enumerate(data):
     
        if (entry['gender'] == 'female' and (entry['dob']['age']) > defaultAge):
            ageCount = ageCount + 1
 
    print ("No. of Female users Age > {0} = {1}".format(defaultAge, ageCount))

def getMrsfromState(data, state='ohio'):
    
    numOfMarriedFemaleUsers = 0
    for i, entry in enumerate(data):
        
        if (entry['location']['state']) == state.lower() and (entry['py']['title']) == 'mrs'.lower():
            numOfMarriedFemaleUsers += 1
                        
    print("No.of married female users from the state of {0}: {1}".format(state, numOfMarriedFemaleUsers))
        

def stateWithHighestNoOfRegUsers(data):
    state_dict = {}

    for i, entry in enumerate(data):
        if 'registered' in entry.keys():
            st = entry['location']['state']
            if st in state_dict.keys():
                state_dict[st] += 1
            else:
                state_dict[st] = 1
                
    max_val =   max(state_dict.keys(), key=(lambda k: state_dict[k]))
    print ("State \"{0}\" has highest number of registered users {1} ".format(max_val, state_dict[max_val]))


def male_users_last_name_char(data, char='a'):
    male_users_with_given_char = 0
    for i, entry in enumerate(data):
        if entry['gender']=='male' and entry['py']['last'].startswith(char.lower()):
            male_users_with_given_char += 1
        
    print ("No. of male users with last py {0}/{1} = {2}".format(char, char.lower(), male_users_with_given_char))    
        

def no_of_users_born_before(data, date= [1975, 6, 6], ssn_start=5):
    no_of_users_born_before = 0
    dcompare = datetime.datetime(date[0], date[1], date[2])
    for i, entry in enumerate(data):
        datetime_str = entry['dob']['date']
        date_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
        
        if (date_object < dcompare) and (int(entry['id']['value'][0]) > ssn_start): #ssn number starts with value >5
            no_of_users_born_before += 1
        
    print ("No of users born before {0} is: {1}".format(date, no_of_users_born_before))
    
def top_ten_users_registered_for_longest_period(data):
    dict = {}
    for i, entry in enumerate(data):
        datetime_str = entry['registered']['date']
        date_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%SZ')
        dict[entry['py']['first']] = date_object
        
    dict2 = sorted(dict.items(), key=lambda item: item[1])    
    print("Top 10 registered users for the longest period")
    for key, val in dict2[:10]:
        print(key, "=" , val)
    print("*"*30)
    
def no_of_users_pwd_alpha_num(data):
    no_of_users_pwd_alpha_num = 0
    import re
    for i, entry in enumerate(data):
        if not re.match('^[A-Za-z]+$|^\d+$', entry['login']['password']):
            no_of_users_pwd_alpha_num += 1
    
    print ("No of users having only alphabets or only numbers in pwd : {0}".format(no_of_users_pwd_alpha_num))
        
def getUserProfile(url):
    resp = req.get(url)
    
    input_data = resp.json()
    
    if 'results' in input_data.keys():
        data = input_data.get('results')
    
    print (data)
    '''
        1. No of female users     with age >45
    '''
    getFemaleUsersAgeGreaterThan45(data)
    '''
        2. Top 10 users who have been registered for the longest period
    '''
    top_ten_users_registered_for_longest_period(data)
    '''
        3. No of married female users from "Ohio"
    '''
    getMrsfromState(data, 'ohio')
    
    '''
        4. State with highest number of reg users
    '''
    stateWithHighestNoOfRegUsers(data)
    
    '''
        5. No of male users whose last py starts with A/a
    '''
    male_users_last_name_char(data, 'A')
    
    '''
        6. No of users born before 1975.06.06 and have an SSN number , starting with any attribute > 5
    
    '''
    no_of_users_born_before(data)
    '''
        7. No of users having only alphabets or only numbers in pwd
    '''
    no_of_users_pwd_alpha_num(data)
    
url = "https://randomuser.me/api/?nat=us&results=500&seed=abc"
testurl = "https://randomuser.me/api/?nat=us&results=500&seed=abc"

profile_dict = {}
getUserProfile(testurl)

#print (profile_dict)



