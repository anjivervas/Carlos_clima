from app.core import ClimaScrap

scrap = ClimaScrap()
temp_promedio = scrap.get_temperature_average()

print(temp_promedio)