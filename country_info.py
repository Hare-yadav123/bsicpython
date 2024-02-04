# Any country information
'''.info()
(2).provinces() ,(3).alt_spellings() ,(4).area() (5).borders() ,(6).calling_codes()(7).capital()
(8).capital_latlng(),(9).currencies(),(10).demonym(),(11).geojson() ,(12).iso()(13).languages()
(14).latlng(), (15).native_name(),(16).population(),(17).region(),(18).subregion(),(19).timezones()
(20).tld(),(21).translations(),(22).wiki(),(23).all() '''

from countryinfo import CountryInfo
country=CountryInfo("India")
# #data=con.alt_spellings()
lang=country.languages()
print(f'\n langauge: {lang}')

country_capital =country.capital()
print(f'\n\nCapital:\n{country_capital}')

bord=country.borders()
print(f"boarder:{bord}")

cureency=country.currencies()
print(f"currency:{cureency}")

time=country.timezones()
print(f"timezone:{time}")

# all=country.all()
# print(f"all{all}")
wiki=country.wiki()
print(f"wiki: {wiki}")

