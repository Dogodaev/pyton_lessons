current = { 'temperatupe':22.0,'humidity':'58%','location':{'city':'London','country':'UK'}}
loc = current['location']
print('Город:', loc['city']+',', loc['country'] +'.','Температура: '+ str(current['temperatupe'])+' °C')
