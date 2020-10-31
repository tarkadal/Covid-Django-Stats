from django.shortcuts import render
from django.utils.safestring import SafeData, SafeString
import json

import core.covid as covid
import core.coreconfig as coreconfig


def index(request, area="Trafford"):

    cumDeathsByDeathDateJSON = covid.get_area_stat(area, "cumDeathsByDeathDate")
    newDeathsByDeathDateJSON = covid.get_area_stat(area, "newDeathsByDeathDate")
    articles = covid.get_news(area)
    # articles = coreconfig.test_news

    ctx = {
        "area": area,
        "cumDeathsByDeathDateJSON": SafeString(cumDeathsByDeathDateJSON),
        "newDeathsByDeathDateJSON": SafeString(newDeathsByDeathDateJSON),
        "articles": articles,
    }

    return render(request, 'index.html', ctx )