from uk_covid19 import Cov19API
import json
import jq


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
