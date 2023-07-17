travel_log = []


def add_new_country(country_name, visit_time, visited_cities):
    new_country = {}
    new_country['country'] = country_name
    new_country['visits'] = visit_time
    new_country['cities'] = visited_cities

    travel_log.append(new_country)


add_new_country('Russia', 3, ['Moscow', 'Saint Petersburg', 'Dublin'])

print(travel_log)
