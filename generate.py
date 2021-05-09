import requests
import os
import time


def gen_country(country, path, url):
    with open(path.format(country), "w+") as file:
        count = 0
        while (not (p := requests.get(url.format(country))).ok) and count < 7:
            time.sleep(12)
            count += 1
        if count == 7:
            print("Failed", country)
        else:
            print("Passed", country)
            file.write(p.content.decode())
        count = 0


if __name__ == '__main__':
    URL = "https://api.covid19api.com/total/dayone/country/{}"
    rel_path = "../countries/{}"
    countries = ['northern-mariana-islands', 'puerto-rico', 'united-arab-emirates', 'lebanon', 'liberia', 'rwanda', 'spain', 'tokelau', 'grenada', 'mauritius', 'gibraltar', 'kuwait', 'south-georgia-and-the-south-sandwich-islands', 'croatia', 'germany', 'palestine', 'tonga', 'honduras', 'jamaica', 'niger', 'fiji', 'indonesia', 'french-southern-territories', 'iceland', 'iran', 'netherlands', 'new-zealand', 'nicaragua', 'angola', 'congo-kinshasa', 'turkmenistan', 'togo', 'virgin-islands', 'algeria', 'burkina-faso', 'turkey', 'gambia', 'maldives', 'belgium', 'botswana', 'kazakhstan', 'saint-martin-french-part', 'vanuatu', 'comoros', 'tanzania', 'united-states', 'lao-pdr', 'namibia', 'chad', 'hungary', 'mali', 'morocco', 'nauru', 'serbia', 'zimbabwe', 'guyana', 'mauritania', 'russia', 'british-virgin-islands', 'cambodia', 'qatar', 'belarus', 'eritrea', 'french-guiana', 'ghana', 'mozambique', 'dominica', 'greece', 'india', 'sri-lanka', 'micronesia', 'sao-tome-and-principe', 'tajikistan', 'antarctica', 'madagascar', 'cote-divoire', 'el-salvador', 'iraq', 'kenya', 'somalia', 'turks-and-caicos-islands', 'benin', 'bolivia', 'chile', 'martinique', 'south-sudan', 'albania', 'anguilla', 'latvia', 'uganda', 'finland', 'holy-see-vatican-city-state', 'macao-sar-china', 'pakistan', 'congo-brazzaville', 'san-marino', 'christmas-island', 'cuba', 'ecuador', 'luxembourg', 'paraguay', 'us-minor-outlying-islands', 'canada', 'seychelles', 'bahrain', 'korea-north', 'wallis-and-futuna-islands', 'guatemala', 'nepal', 'czech-republic', 'equatorial-guinea', 'moldova', 'trinidad-and-tobago', 'brazil', 'malawi', 'sierra-leone', 'slovenia', 'egypt', 'jordan', 'australia', 'burundi', 'cyprus', 'saudi-arabia', 'malta', 'saint-lucia', 'israel', 'malaysia', 'mongolia', 'niue', 'saint-vincent-and-the-grenadines', 'belize', 'falkland-islands-malvinas', 'ukraine', 'guinea', 'panama', 'british-indian-ocean-territory', 'monaco', 'solomon-islands', 'estonia', 'france', 'sudan', 'haiti', 'montenegro', 'uruguay', 'uzbekistan', 'djibouti', 'italy', 'korea-south', 'saint-kitts-and-nevis', 'bangladesh', 'bouvet-island', 'guinea-bissau', 'saint-barthélemy', 'singapore', 'south-africa', 'afghanistan', 'bhutan', 'montserrat', 'costa-rica', 'faroe-islands', 'greenland', 'heard-and-mcdonald-islands', 'timor-leste', 'brunei', 'cayman-islands', 'denmark', 'venezuela', 'armenia', 'aruba', 'thailand', 'bosnia-and-herzegovina', 'china', 'andorra', 'ireland', 'romania', 'united-kingdom', 'norfolk-island', 'samoa', 'taiwan', 'tunisia', 'lithuania', 'norway', 'liechtenstein', 'marshall-islands', 'kiribati', 'argentina', 'georgia', 'papua-new-guinea', 'syria', 'myanmar', 'cameroon', 'lesotho', 'american-samoa', 'palau', 'peru', 'tuvalu', 'ala-aland-islands', 'cook-islands', 'ethiopia', 'azerbaijan', 'hong-kong-sar-china', 'mexico', 'kyrgyzstan', 'libya', 'réunion', 'suriname', 'vietnam', 'cocos-keeling-islands', 'guadeloupe', 'austria', 'new-caledonia', 'cape-verde', 'guam', 'isle-of-man', 'mayotte', 'netherlands-antilles', 'bermuda', 'dominican-republic', 'macedonia', 'nigeria', 'poland', 'bahamas', 'barbados', 'french-polynesia', 'oman', 'pitcairn', 'saint-helena', 'zambia', 'slovakia', 'yemen', 'svalbard-and-jan-mayen-islands', 'western-sahara', 'japan', 'philippines', 'jersey', 'saint-pierre-and-miquelon', 'kosovo', 'sweden', 'central-african-republic', 'portugal', 'swaziland', 'colombia', 'antigua-and-barbuda', 'bulgaria', 'gabon', 'guernsey', 'senegal', 'switzerland']
    for c in countries:
        gen_country(c, rel_path, URL)