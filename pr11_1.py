def function(city, country, population=''):
	if population:
		message = city.title()+", "+country.title()+' - population '+population
	else:
		message = city.title()+", "+country.title()
	return message