"""
__author__ = "Bella Cromwell"
__email__ = "cromweli@my.erau.edu"
__version__ = "1.0"

How to calculate the best route to visit 5 given cities in 5 days.

"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

HOTEL_BUDGET = 850


def cost_route_org(route):
    """
    Finding the highest average temperature of the entire trip
    Setting the "temp" variable to 0
    Creating a "for" loop to go through each permutation of city temps
    Returning the highest average temp of the correct permutation route
    """
    temp = 0
    for i in range(len(route)):
        city = route[i]
        temp += city_temps[city][i]
    return temp/len(route)


def best_route_func(cities):
    """
    Finding all permutations of the cities:
    Setting "max" to 0.
    Setting "best" as an empty list.
    Creating a "for" loop to go through each city within the city_temps dictionary.
    Adding an if statement by stating that if the max is less than the average temp.
    while max equals the average temp and then having the "best" variable print out the correct
    list of cities.
    """
    perm = permutations(list(cities))

    max = 0
    best = []
    for r in perm:
        avg_temp = cost_route_org(r)
        if max < avg_temp:
            max = avg_temp
            best = r
    return max, best


def max_budget_func(hotels):
    """
    Finding hotels to stay in that will best max out the given budget.
    Using "combinations_with_replacement" imported by itertools to find all possible
    combinations of hotels corresponding with the 5 days of travel.
    Setting "cost" and "max_cost" variables to 0 since we are using integers.
    Setting "best_option" as an empty list.
    Creating a "for" loop to analyze each combination.
    Analyzing each hotel in each combination with corresponding values.
    Returning the "max_cost" value and "best_option" list of hotels.
    """
    perm = combinations_with_replacement(hotels, 5)
    cost = 0
    max_cost = 0
    best_option = []

    for i in perm:
        cost = 0
        for s in i:
            cost += hotel_rates[s]
        if max_cost < cost <= HOTEL_BUDGET:
            max_cost = cost
            best_option = i
    return max_cost, best_option


if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())
    best_route = best_route_func(cities)
    print(f'Here is your best route: {best_route[1]} the average of the daily max temp. is {best_route[0]}F')
    best_hotels = max_budget_func(hotels)
    print(f'To max out your hotel budget, stay at these hotels: {best_hotels[1]}, totaling ${best_hotels[0]}')
