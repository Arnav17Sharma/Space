def rocket_list():
    import requests
    from bs4 import BeautifulSoup

    def from_wiki(link):
        source = requests.get(link).text
        soup = BeautifulSoup(source, 'lxml').body
        # print(soup.prettify())
        lst = []
        for img in soup.find_all('img'):
            lst.append(img['src'])
        return lst[3]

    # testing
    # from_wiki('https://en.wikipedia.org/wiki/Falcon_9')

    url = "https://api.spacexdata.com/v3/rockets"

    payload = {}
    files = {}
    headers = {}

    response = requests.request(
        "GET", url, headers=headers, data=payload, files=files)

    # spacex_rocket = {
    #     'id': ['', {
    #         'name': '',
    #         'mass': '',
    #         'height': '',
    #         'desc': '',
    #         'wiki': '',
    #         'img_src': []}]
    # }

    rocket_list = []

    list = response.json()
    for json in list:
        spacex_rocket = {}
        id = json['id']
        country = json['country']
        cost = str(json['cost_per_launch'])
        wiki = json['wikipedia']
        desc = json['description']
        name = json['rocket_name']
        type = json['rocket_type']
        mass = str(json['mass']['kg'])
        height = str(json['height']['meters'])

        spacex_rocket['info'] = [id, {
            'name': name,
            'cost': cost,
            'mass': mass,
            'height': height,
            'desc': desc,
            'wiki': wiki,
            'img_src': from_wiki(wiki),
            'country': country
        }]
        # print(spacex_rocket)
        # print()
        # print()
        rocket_list.append(spacex_rocket)

    return rocket_list


print(rocket_list())


'''
[{1: [1, {'name': 'Falcon 1', 'mass': '30146', 'height': '22.25', 'desc': 'The Falcon 1 was an expendable launch system privately developed and manufactured by SpaceX during 2006-2009. On 28 September 2008, Falcon 1 became the first privately-developed liquid-fuel launch vehicle to go into orbit around the Earth.', 'wiki': 'https://en.wikipedia.org/wiki/Falcon_1', 'img_src': ['//upload.wikimedia.org/wikipedia/commons/thumb/7/75/Web-browser.svg/40px-Web-browser.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Falcon_1_Flight_4_liftoff.jpg/220px-Falcon_1_Flight_4_liftoff.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/RocketSunIcon.svg/16px-RocketSunIcon.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/9/9c/SpaceX_falcon_in_warehouse.jpg/220px-SpaceX_falcon_in_warehouse.jpg', '//upload.wikimedia.org/wikipedia/en/2/26/Falcon_1_Flight.jpg', '//upload.wikimedia.org/wikipedia/en/timeline/85a1910f0d6746284d85626e7fb2d1f6.png', '//upload.wikimedia.org/wikipedia/en/thumb/9/93/Spacex_067.jpg/220px-Spacex_067.jpg', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/100px-SpaceX-Logo-Xonly.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/8/89/Symbol_book_class2.svg/16px-Symbol_book_class2.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/12px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/150px-SpaceX-Logo-Xonly.svg.png', '//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1', '/static/images/footer/wikimedia-button.png', '/static/images/footer/poweredby_mediawiki_88x31.png']}]}, {2: [2, {'name': 'Falcon 9', 'mass': '549054', 'height': '70', 'desc': 'Falcon 9 is a two-stage rocket designed and manufactured by SpaceX for the reliable and safe transport of satellites and the Dragon spacecraft into orbit.', 'wiki': 'https://en.wikipedia.org/wiki/Falcon_9', 'img_src': ['//upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Falcon_9_logo.svg/90px-Falcon_9_logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/2/2b/SpaceX_Demo-2_Launch_%28NHQ202005300044%29_%28cropped%29.jpg/220px-SpaceX_Demo-2_Launch_%28NHQ202005300044%29_%28cropped%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Falcon9_rocket_family.svg/290px-Falcon9_rocket_family.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/5/55/SpaceX_Falcon_9_launch_with_COTS_Demo_Flight_1_%28low_quality%29.ogv/270px--SpaceX_Falcon_9_launch_with_COTS_Demo_Flight_1_%28low_quality%29.ogv.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/6/64/ORBCOMM-2_First-Stage_Landing_%2823271687254%29.jpg/270px-ORBCOMM-2_First-Stage_Landing_%2823271687254%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/5/57/Falcon_9.stl/270px-Falcon_9.stl.png', '//upload.wikimedia.org/wikipedia/commons/thumb/2/29/SpX_CRS-2_launch_-_further_-_cropped.jpg/270px-SpX_CRS-2_launch_-_further_-_cropped.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/5/58/Falcon_9_v1.0_and_v1.1_engine.svg/270px-Falcon_9_v1.0_and_v1.1_engine.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/5/58/Launch_of_Falcon_9_carrying_CASSIOPE_%28130929-F-ET475-012%29.jpg/270px-Launch_of_Falcon_9_carrying_CASSIOPE_%28130929-F-ET475-012%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Second-generation_titanium_grid_fins%2C_Iridium-2_Mission_%2835533873795%29.jpg/270px-Second-generation_titanium_grid_fins%2C_Iridium-2_Mission_%2835533873795%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/c/ca/SES-10_Launch_-_world%27s_first_reflight_of_an_orbital_class_rocket_%2832915200224%29.jpg/270px-SES-10_Launch_-_world%27s_first_reflight_of_an_orbital_class_rocket_%2832915200224%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/9/91/CRS-6_first_stage_booster_landing_attempt.jpg/270px-CRS-6_first_stage_booster_landing_attempt.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Launch_of_Falcon_9_carrying_ABS-EUTELSAT_%2816510241270%29.jpg/290px-Launch_of_Falcon_9_carrying_ABS-EUTELSAT_%2816510241270%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/RocketSunIcon.svg/28px-RocketSunIcon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/2/24/Wikinews-logo.svg/40px-Wikinews-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/b/bc/COTS2Dragon.6.jpg/85px-COTS2Dragon.6.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Crew_Dragon_at_the_ISS_for_Demo_Mission_1_%28cropped%29.jpg/85px-Crew_Dragon_at_the_ISS_for_Demo_Mission_1_%28cropped%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/100px-SpaceX-Logo-Xonly.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/8/89/Symbol_book_class2.svg/16px-Symbol_book_class2.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/12px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/150px-SpaceX-Logo-Xonly.svg.png', '//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1', '/static/images/footer/wikimedia-button.png', '/static/images/footer/poweredby_mediawiki_88x31.png']}]}, {3: [3, {'name': 'Falcon Heavy', 'mass': '1420788', 'height': '70', 'desc': 'With the ability to lift into orbit over 54 metric tons (119,000 lb)--a mass equivalent to a 737 jetliner loaded with passengers, crew, luggage and fuel--Falcon Heavy can lift more than twice the payload of the next closest operational vehicle, the Delta IV Heavy, at one-third the cost.', 'wiki': 'https://en.wikipedia.org/wiki/Falcon_Heavy', 'img_src': ['//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Falcon_Heavy_logo.svg/90px-Falcon_Heavy_logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Falcon_Heavy_Demo_Mission_%2839337245145%29.jpg/220px-Falcon_Heavy_Demo_Mission_%2839337245145%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/a/a3/SpaceX_breaks_ground_at_Vandenberg_Air_Force_Base.jpg/220px-SpaceX_breaks_ground_at_Vandenberg_Air_Force_Base.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Falcon_rocket_family6.svg/280px-Falcon_rocket_family6.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/5/59/Falcon_Heavy_Demo_Mission_%2840126461851%29.jpg/220px-Falcon_Heavy_Demo_Mission_%2840126461851%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Falcon_Heavy_cropped.jpg/220px-Falcon_Heavy_cropped.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/4/44/SpaceX_Testing_Merlin_1D_Engine_In_Texas.jpg/220px-SpaceX_Testing_Merlin_1D_Engine_In_Texas.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/3/31/Arabsat-6A_Mission_%2840628437283%29.jpg/220px-Arabsat-6A_Mission_%2840628437283%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Falcon_heavy_June_2019.jpg/220px-Falcon_heavy_June_2019.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/5/52/Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_%2825254688767%29.jpg/280px-Falcon_Heavy_Side_Boosters_landing_on_LZ1_and_LZ2_-_2018_%2825254688767%29.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Wiki_letter_w_cropped.svg/20px-Wiki_letter_w_cropped.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/RocketSunIcon.svg/28px-RocketSunIcon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/a/a4/Flag_of_the_United_States.svg/32px-Flag_of_the_United_States.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Industry5.svg/28px-Industry5.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/100px-SpaceX-Logo-Xonly.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/8/89/Symbol_book_class2.svg/16px-Symbol_book_class2.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/12px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/150px-SpaceX-Logo-Xonly.svg.png', '//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1', '/static/images/footer/wikimedia-button.png', '/static/images/footer/poweredby_mediawiki_88x31.png']}]}, {4: [4, {'name': 'Starship', 'mass': '1335000', 'height': '118', 'desc': 'Starship and Super Heavy Rocket represent a fully
reusable transportation system designed to service all Earth orbit needs as well as the Moon and Mars. This two-stage vehicle —
composed of the Super Heavy rocket (booster) and Starship (ship) — will eventually replace Falcon 9, Falcon Heavy and Dragon.',
'wiki': 'https://en.wikipedia.org/wiki/SpaceX_Starship', 'img_src': ['//upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Starship_SN8.jpg/220px-Starship_SN8.jpg', '//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/d/db/Super_heavy-lift_launch_vehicles.png/290px-Super_heavy-lift_launch_vehicles.png', '//upload.wikimedia.org/wikipedia/commons/thumb/f/f8/BFR_at_stage_separation_2-2018.jpg/290px-BFR_at_stage_separation_2-2018.jpg', '//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/d/da/SpaceX_Starhopper.jpg/290px-SpaceX_Starhopper.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Starship_sn5.jpg/250px-Starship_sn5.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/d/d6/RocketSunIcon.svg/28px-RocketSunIcon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/6/62/PD-icon.svg/15px-PD-icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/30px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/3/36/SpaceX-Logo-Xonly.svg/100px-SpaceX-Logo-Xonly.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/8/89/Symbol_book_class2.svg/16px-Symbol_book_class2.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/12px-Commons-logo.svg.png', '//upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Progress_M-52.jpg/100px-Progress_M-52.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/e/e6/S66-63536.jpg/130px-S66-63536.jpg', '//upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Artemis_program_%28original_with_wordmark%29.svg/80px-Artemis_program_%28original_with_wordmark%29.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/48/Folder_Hexagonal_Icon.svg/16px-Folder_Hexagonal_Icon.svg.png', '//upload.wikimedia.org/wikipedia/en/thumb/4/4a/Commons-logo.svg/12px-Commons-logo.svg.png', '//en.wikipedia.org/wiki/Special:CentralAutoLogin/start?type=1x1', '/static/images/footer/wikimedia-button.png', '/static/images/footer/poweredby_mediawiki_88x31.png']}]}]
'''
