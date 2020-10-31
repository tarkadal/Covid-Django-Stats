from uk_covid19 import Cov19API
import jq

import core.coreconfig as coreconfig

import datanews
datanews.api_key = coreconfig.datanews_apikey

from pprint import pprint

def get_area_stat(area, stat):

    areaName = "areaName=" + area

    all_nations = [
        areaName,
    ]

    # Possibles:
    # "areaCode": "areaCode",
    # "newCasesByPublishDate": "newCasesByPublishDate",
    # "cumCasesByPublishDate": "cumCasesByPublishDate",
    # "newDeathsByDeathDate": "newDeathsByDeathDate",
    # "cumDeathsByDeathDate": "cumDeathsByDeathDate",
    # "cumDeaths28DaysByPublishDateRate": "cumDeaths28DaysByPublishDateRate",
    # "newAdmissions": "newAdmissions",
    # "cumAdmissions": "cumAdmissions",

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        stat: stat,
    }

    api = Cov19API(
        filters=all_nations,
        structure=cases_and_deaths
    )
    apiDict = api.get_json()
    apiDict = jq.compile(".data | unique ").input(apiDict)

    dataDict = {'data': []}
    listTemp = []

    for entry in apiDict.first():
        listTemp.append(entry)
    
    dataDict['data'] = listTemp

    return dataDict

def get_news(area):
    query = '(covid|covid-19|coronavirus|SARS-CoV-2)+' + area
    response = datanews.headlines(q=query, language=['en'], sortBy='date', size=100)
    
    pprint(response)
    return response
