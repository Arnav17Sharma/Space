import requests
import json

# 7QwSQ0CFZLiQDeEymYbcBZAXcUbDL0ZFI1xc0m9i
global d
d = '''{"sol_keys": [ "259", "260", "261", "262", "263", "264", "265" ],"259": {"AT": { "av": -71.233, "ct": 326642, "mn": -101.024, "mx": -27.149 },"HWS": { "av": 4.35, "ct": 154146, "mn": 0.156, "mx": 17.617 },"PRE": { "av": 761.006, "ct": 163012, "mn": 742.1498, "mx": 780.3891 },"WD":{"most_common": { "compass_degrees": 202.5, "compass_point": "SSW", "compass_right": -0.382683432365,"compass_up": -0.923879532511, "ct": 28551 },"8": { "compass_degrees": 180.0, "compass_point": "S", "compass_right": 0.0,"compass_up": -1.0, "ct": 17699 },"9": { "compass_degrees": 202.5, "compass_point": "SSW", "compass_right": -0.382683432365,"compass_up": -0.923879532511, "ct": 28551 },"10": { "compass_degrees": 225.0, "compass_point": "SW", "compass_right": -0.707106781187,"compass_up": -0.707106781187, "ct": 27124 }},"First_UTC": "2019-08-19T08:03:59Z", "Last_UTC": "2019-08-20T08:43:34Z", "Season": "winter"},"260": {"AT": { "av": -75.95, "ct": 300789, "mn": -101.715, "mx": -28.634 },"PRE": { "av": 762.462, "ct": 149206, "mn": 741.1254, "mx": 777.796 },"WD": { "most_common": 0 },"First_UTC": "2019-08-20T08:43:34Z", "Last_UTC": "2019-08-21T09:23:09Z", "Season": "winter"},"261": "{...}","262": "{...}","263": "{...}","264": "{...}","265": "{...}","validity_checks": {"sol_hours_required": 18,"sols_checked": ["258","259","260","261","262","263","264","265"],"258": {"AT": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true },"HWS": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true },"PRE": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true },"WD": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true }},"259": {"AT": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true },"HWS": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true },"PRE": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true },"WD": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],"valid": true }},"260": {"AT": { "sol_hours_with_data": [0,1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23],"valid": true },"HWS": { "sol_hours_with_data": [ 0,1,2,3,4,5,6,7,15,16,17,18,19,20,21,22,23],"valid": false }, "PRE": { "sol_hours_with_data": [ 0,1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23], "valid": true }, "WD": { "sol_hours_with_data": [ 0,1,2,3,4,5,6,7,15,16,17,18,19,20,21,22,23], "valid": false } },"261": "{...}", "262": "{...}", "263": "{...}","264": "{...}","265": "{...}"} }'''


def get_data():
    API_KEY1 = '7QwSQ0CFZLiQDeEymYbcBZAXcUbDL0ZFI1xc0m9i'
    API_KEY2 = 'GQTy0PABPwM6YcSxKjJASJaLoiWClsAXNUb1MR1O'
    link = f'https://api.nasa.gov/insight_weather/?api_key={API_KEY1}&feedtype=json&ver=1.0'
    r = requests.get(link)

    package_json = r.json()

    # return (package_json)
    dict_Sol = {}

    sol_list = list(i for i in package_json.keys() if i.isdigit())

    for sol in sol_list:
        dict_Sol[sol] = {
            'sol': sol,
            'date': '',
            'time': '',
            'atm_temp': {
                    'total_cases': '',
                    'avg_temp': '',
                                'max_temp': '',
                                'min_temp': ''
            },
            'hws': {
                'total_cases': '',
                'avg_hws': '',
                'max_hws': '',
                'min_hws': ''
            },
            'pre': {
                'total_cases': '',
                'avg_pre': '',
                'max_pre': '',
                'min_pre': ''
            },
            'season': '',
            'wd': {
                'compass_degrees': '',
                'compass_point': ''
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
                dict_Sol[sol]['atm_temp']['total_cases'] = str(
                    package_json[sol][sol_info]['ct'])
                dict_Sol[sol]['atm_temp']['avg_temp'] = str(
                    round(package_json[sol][sol_info]['av'], 2))
                dict_Sol[sol]['atm_temp']['max_temp'] = str(
                    round(package_json[sol][sol_info]['mn'], 2))
                dict_Sol[sol]['atm_temp']['min_temp'] = str(
                    round(package_json[sol][sol_info]['mx'], 2))
            if sol_info == 'HWS':
                dict_Sol[sol]['hws']['total_cases'] = package_json[sol][sol_info]['ct']
                dict_Sol[sol]['hws']['avg_hws'] = str(
                    round(package_json[sol][sol_info]['av'], 2))
                dict_Sol[sol]['hws']['max_hws'] = str(
                    round(package_json[sol][sol_info]['mn'], 2))
                dict_Sol[sol]['hws']['min_hws'] = str(
                    round(package_json[sol][sol_info]['mx'], 2))
            if sol_info == 'PRE':
                dict_Sol[sol]['pre']['total_cases'] = package_json[sol][sol_info]['ct']
                dict_Sol[sol]['pre']['avg_pre'] = str(
                    round(package_json[sol][sol_info]['av'], 2))
                dict_Sol[sol]['pre']['max_pre'] = str(
                    round(package_json[sol][sol_info]['mn'], 2))
                dict_Sol[sol]['pre']['min_pre'] = str(
                    round(package_json[sol][sol_info]['mx'], 2))

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


get_str = json.dumps(get_data(), indent=3)
print(get_str)


def get_images():
    l = []
    API_KEY = '7QwSQ0CFZLiQDeEymYbcBZAXcUbDL0ZFI1xc0m9i'
    r = requests.get(
        f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={ API_KEY }')
    package_json = r.json()
    package_str = json.dumps(package_json['photos'], indent=2)
    for img_info in package_json['photos']:
        img_link = img_info['img_src']
        l.append(img_link)
    return l


print()
print()
# print(get_images())
