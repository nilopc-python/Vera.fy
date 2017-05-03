import requests
r = requests.post("http://verafy.herokuapp.com/input/", data={'input_str': "ucla is a university"})
print r.text
