#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lambda planets #5."""

from pprint import pprint as pp
from planets_data import get_planets_data


def lambda_planets_aggregate_by_population():
    """Lambda function #5."""
    data = get_planets_data()
    known_population = list(filter(lambda a: a['population'] is not 'unknown', data))
    unknown_population = list(filter(lambda a: a['population'] is 'unknown', data))
    planet_with_max_population = max(known_population, key=lambda a: int(a['population']))
    max_population = int(planet_with_max_population['population'])
    x = y = 1
    while x < max_population:
        x *= 10
        y += 1
    aggregate_population_ranges = [{'from': 0, 'to': 10}]
    l = 10
    for i in range(y-1):
        k = l
        l = 10**(i+2)
        r = {'from': k, 'to': l}
        aggregate_population_ranges.append(r)
    aggregate_planets_by_population = {}
    for rg in aggregate_population_ranges:
        aggregate_planets_by_population[str(rg['from']) + '-' + str(rg['to'])] = list(
            filter(
                lambda a: rg['from'] <= int(a['population']) < rg['to'],
                known_population))
    aggregate_planets_by_population['unknown'] = unknown_population
    pp(aggregate_planets_by_population)

lambda_planets_aggregate_by_population()
