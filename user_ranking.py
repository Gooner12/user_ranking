import argparse
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from scipy import stats

# Run function

def ask():
    prompt = input('Do you want to exit the program? Type "Yes" or "No". ')
    if ('yes' in prompt.lower()):
        exit()
    elif ('no' in prompt.lower()):
        check_function()
    else:
        print('Only type "Yes" or "No"')
        ask()

def check_function():
    url = input('Enter the url of a stackoverflow user: ')

    pattern = re.compile(r'^(https?://)?(w{3}\.)?(stackoverflow\.com/users)(/[0-9]+)(/[a-z0-9-]+)')
    if (pattern.search(url)):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        page_status = soup.find_all('h1', attrs={'class':'fs-headline1 mb4'})
        if(len(page_status) != 0):
            print("Page does not exist! Check and enter the URL again.")
            ask()
        else:
            process_function(soup, url)
    else:
        print ("Please enter the correct URL.")
        ask()

def process_function(soup, user_url):
    reputation = soup.find_all('div', attrs={'class':'my12 fw-normal lh-sm'})
    status = soup.find_all('div', attrs={'class':'grid--cell fl-shrink0 pr24 wmx3'})
    badges = soup.find_all('div', attrs={'id':'badges'})
    reputation_data = reputation[0]
    reputation_interim = reputation_data.find('div', attrs={'class':'grid--cell fs-title fc-dark'}).text
    reputation_in_number = int(reputation_interim.replace(",",""))
    status_required = status[0]
    answer_status=status_required.contents[1].find('div', attrs={'class':'grid--cell'})
    answer_interim=answer_status.find('div',attrs={'class':'grid--cell fs-body3 fc-dark fw-bold'})
    answer=int(answer_interim.text)
    question_status=answer_status.find_next_sibling('div')
    question_interim=question_status.find('div',attrs={'class':'grid--cell fs-body3 fc-dark fw-bold'})
    question=int(question_interim.text)
    people_reached_status=question_status.find_next_sibling('div')
    people_reached_interim=people_reached_status.find('div',attrs={'class':'grid--cell fs-body3 fc-dark fw-bold'})
    people_reached_interim2=people_reached_interim.text[1:]
    if('k' in people_reached_interim2):
        people_reached = int(people_reached_interim2.replace('k',''))*1000
    else:
        people_reached = int(people_reached_interim2)

    #Extracting badges
    badges_required=badges[0]
    gold_badges=badges_required.contents[3].find('div', attrs={'class':'grid--cell px12 br bc-black-2'})
    number_of_gold_interim=gold_badges.find('div', attrs={'class':'grid--cell fs-headline1 lh-sm'})
    number_of_gold=int(number_of_gold_interim.text)
    silver_badges=gold_badges.find_next_sibling('div')
    number_of_silver_interim=silver_badges.find('div', attrs={'class':'grid--cell fs-headline1 lh-sm'})
    number_of_silver=int(number_of_silver_interim.text)
    bronze_badges=silver_badges.find_next_sibling('div')
    number_of_bronze_interim=bronze_badges.find('div', attrs={'class':'grid--cell fs-headline1 lh-sm'})
    number_of_bronze=int(number_of_bronze_interim.text)

    # Extracting user Id
    url_string = user_url
    url_tuple = url_string.split('/')
    for users in url_tuple:
        if(re.match('[0-9]+', users)):
            user_link = int(users)
    df2 = pd.read_csv('./QueryResults.csv', sep=",")
    array_reputation = df2.iloc[:,2:3]
    percentile_score = 100 - (int(stats.percentileofscore(array_reputation, reputation_in_number, kind = 'weak')))
    print('The user %s is in the top %d percent of Melbourne Stackoverflow users based on reputation.' %(url_tuple[5], percentile_score))
    print()
    print('Users statistics:')
    print()
    print('Number of answers recorded: ',answer)
    print('Number of questions asked: ',question)
    print('Number of people reached: ',people_reached)
    print('Number of gold badges: ',number_of_gold)
    print('Number of silver badges: ',number_of_silver)
    print('Number of bronze badges: ', number_of_bronze)


url = input('Enter the url of a stackoverflow user: ')
pattern = re.compile(r'^(https?://)?(w{3}\.)?(stackoverflow\.com/users)(/[0-9]+)(/[a-z0-9-]+)')
if (pattern.search(url)):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    page_status = soup.find_all('h1', attrs={'class':'fs-headline1 mb4'})
    if(len(page_status) != 0):
        print('Page does not exist!. Check and enter the URL again.')
        ask()
    else:
        process_function(soup, url)
else:
    print ("Please enter the correct URL.")
    ask()
