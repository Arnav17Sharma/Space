import requests
import json
def get_data():
	API_KEY = '7QwSQ0CFZLiQDeEymYbcBZAXcUbDL0ZFI1xc0m9i'
	r = requests.get(f'https://api.nasa.gov/insight_weather/?api_key={ API_KEY }&feedtype=json&ver=1.0')
	package_json = r.json()

	dict_Sol = {}

	sol_list = list(i for i in package_json.keys() if i.isdigit())

	for sol in sol_list:
		dict_Sol[sol] ={
			'sol':sol,
			'date':'',
			'time':'',
			'atm_temp':{
					'total_cases':'',
					'avg_temp':'',
					'max_temp':'',
					'min_temp':''
				},
			'hws':{
					'total_cases':'',
					'avg_hws':'',
					'max_hws':'',
					'min_hws':''
				},
			'pre':{
					'total_cases':'',
					'avg_pre':'',
					'max_pre':'',
					'min_pre':''
				},
			'season':'',
			'wd':{
					'compass_degrees':'',
					'compass_point':''
				}
		}
		try:
			date_time = package_json[sol]['First_UTC'].split('T')
			dict_Sol[sol]['date'] = date_time[0]
			dict_Sol[sol]['time'] = date_time[1][:-1]
		except:
			break
		for sol_info in package_json[sol]:
			if sol_info == 'AT':
				dict_Sol[sol]['atm_temp']['total_cases'] = str(package_json[sol][sol_info]['ct'])
				dict_Sol[sol]['atm_temp']['avg_temp'] = str(round(package_json[sol][sol_info]['av'], 2))
				dict_Sol[sol]['atm_temp']['max_temp'] = str(round(package_json[sol][sol_info]['mn'], 2))
				dict_Sol[sol]['atm_temp']['min_temp'] = str(round(package_json[sol][sol_info]['mx'], 2))
			if sol_info == 'HWS':
				dict_Sol[sol]['hws']['total_cases'] = package_json[sol][sol_info]['ct']
				dict_Sol[sol]['hws']['avg_hws'] = str(round(package_json[sol][sol_info]['av'], 2))
				dict_Sol[sol]['hws']['max_hws'] = str(round(package_json[sol][sol_info]['mn'], 2))
				dict_Sol[sol]['hws']['min_hws'] = str(round(package_json[sol][sol_info]['mx'], 2))
			if sol_info == 'PRE':
				dict_Sol[sol]['pre']['total_cases'] = package_json[sol][sol_info]['ct']
				dict_Sol[sol]['pre']['avg_pre'] = str(round(package_json[sol][sol_info]['av'], 2))
				dict_Sol[sol]['pre']['max_pre'] = str(round(package_json[sol][sol_info]['mn'], 2))
				dict_Sol[sol]['pre']['min_pre'] = str(round(package_json[sol][sol_info]['mx'], 2))

			if sol_info == 'Season':
				dict_Sol[sol]['season'] = package_json[sol][sol_info].capitalize()
			try:
				if sol_info == 'WD':
					dict_Sol[sol]['wd']['compass_degrees'] = package_json[sol][sol_info]['most_common']['compass_degrees']
					dict_Sol[sol]['wd']['compass_point'] = package_json[sol][sol_info]['most_common']['compass_point']
			except:
				dict_Sol[sol]['wd']['compass_degrees'] = 'Not Available'
				dict_Sol[sol]['wd']['compass_point'] = 'Not Available'
	return dict_Sol, sorted(dict_Sol, reverse=True)


# get_str = json.dumps(get_data(), indent=3)
# print(get_str)



def get_images():
	l = []
	API_KEY = '7QwSQ0CFZLiQDeEymYbcBZAXcUbDL0ZFI1xc0m9i'
	r = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={ API_KEY }')
	package_json = r.json()
	package_str = json.dumps(package_json['photos'], indent=2)
	for img_info in package_json['photos']:
		img_link = img_info['img_src']
		l.append(img_link)
	return l