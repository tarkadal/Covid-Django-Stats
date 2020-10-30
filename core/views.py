from django.shortcuts import render
from django.utils.safestring import SafeData, SafeString
import json

import core.covid as covid


def index(request, area="Trafford"):

    cumDeathsByDeathDateJSON = covid.get_area_stat(area, "cumDeathsByDeathDate")
    newDeathsByDeathDateJSON = covid.get_area_stat(area, "newDeathsByDeathDate")

    ctx = {
        "area": area,
        "cumDeathsByDeathDateJSON": SafeString(cumDeathsByDeathDateJSON),
        "newDeathsByDeathDateJSON": SafeString(newDeathsByDeathDateJSON),
    }

    return render(request, 'index.html', ctx )