from uk_covid19 import Cov19API
import json
import jq

def get_area_newDeathsByDeathDate(area):

    areaName = "areaName=" + area

    all_nations = [
        areaName,
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        # "areaCode": "areaCode",
        # "newCasesByPublishDate": "newCasesByPublishDate",
        # "cumCasesByPublishDate": "cumCasesByPublishDate",
        "newDeathsByDeathDate": "newDeathsByDeathDate",
        # "cumDeathsByDeathDate": "cumDeathsByDeathDate",
        # "cumDeaths28DaysByPublishDateRate": "cumDeaths28DaysByPublishDateRate",
        # "newAdmissions": "newAdmissions",
        # "cumAdmissions": "cumAdmissions",
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

def get_area_cumDeathsByDeathDate(area):

    areaName = "areaName=" + area

    all_nations = [
        areaName,
    ]

    cases_and_deaths = {
        "date": "date",
        "areaName": "areaName",
        # "areaCode": "areaCode",
        # "newCasesByPublishDate": "newCasesByPublishDate",
        # "cumCasesByPublishDate": "cumCasesByPublishDate",
        # "newDeathsByDeathDate": "newDeathsByDeathDate",
        "cumDeathsByDeathDate": "cumDeathsByDeathDate",
        # "cumDeaths28DaysByPublishDateRate": "cumDeaths28DaysByPublishDateRate",
        # "newAdmissions": "newAdmissions",
        # "cumAdmissions": "cumAdmissions",
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