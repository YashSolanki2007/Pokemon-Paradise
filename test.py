import requests

url = "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json"

headers = {
    'x-rapidapi-key': "77ee9999bdmsh61f74ea752bc214p12f26cjsn3bc1f1725b22",
    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

# 1282 in jsonated response

jsonated_response = response.json()

pokemon_name = input("Enter the name of the pokemon: ")

for i in range(len(jsonated_response)):
	poke_name_in_res = str(jsonated_response[i]['pokemon_name'])

	if str(pokemon_name) == poke_name_in_res:
		base_attack = jsonated_response[i]['base_attack']
		print(f"The Base Attack Of the pokemon {poke_name_in_res} is {base_attack}")
		break

	else:
		pass