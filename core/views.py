from django.shortcuts import render
from django.utils.safestring import SafeData, SafeString
import json

import core.covid as covid


def index(request, area="Trafford"):

    # if area == "":
    #     area = "Trafford"

    cumDeathsByDeathDateJSON = covid.get_area_cumDeathsByDeathDate(area)
    newDeathsByDeathDateJSON = covid.get_area_newDeathsByDeathDate(area)

    ctx = {
        "area": area,
        "cumDeathsByDeathDateJSON": SafeString(cumDeathsByDeathDateJSON),
        "newDeathsByDeathDateJSON": SafeString(newDeathsByDeathDateJSON),
    }

    return render(request, 'index.html', ctx )