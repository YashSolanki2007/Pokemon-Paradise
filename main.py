# Imports
from flask import Flask, request, render_template
import requests
import constants
import random 

# Setup the app 
app = Flask(__name__)
app.secret_key = "yashisthesecretkeytotheapp"

# Global Varable
pokemon_name = ""
base_attack = ""
base_defence = ""
base_stamina = ""
computer_poke_choice = ""
poke_name_in_res = ""
comp_choice = ""
decision = ""
player_score = 0 
computer_score = 0

# Making the home page
@app.route("/")
def home():
	return render_template("home_page.html")

# Making the poke battle page
@app.route("/poke_battle", methods=['GET', 'POST'])
def poke_battle():
	global poke_name_in_res, pokemon_name, base_attack, base_defence, base_stamina
	global decision, computer_poke_choice, comp_choice, player_score, computer_score

	if request.method == "POST":
		webpage = request.form
		pokemon_name = str(webpage['choiceInp'])
		url = "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json"

		headers = {
		    'x-rapidapi-key': "77ee9999bdmsh61f74ea752bc214p12f26cjsn3bc1f1725b22",
		    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers)

		# 1282 in jsonated response

		jsonated_response = response.json()

		random_no = random.randint(0, 1282)

		# Fancy way of json random response
		comp_choice = str(jsonated_response[random_no]['pokemon_name'])
		comp_choice_attack = jsonated_response[random_no]['base_attack']
		comp_choice_defence = jsonated_response[random_no]['base_defense']
		comp_choice_stamina = jsonated_response[random_no]['base_stamina']

		for i in range(len(jsonated_response)):
			poke_name_in_res = str(jsonated_response[i]['pokemon_name'])

			if pokemon_name == poke_name_in_res:
				base_attack = jsonated_response[i]['base_attack']
				base_defence = jsonated_response[i]['base_defense']
				base_stamina = jsonated_response[i]['base_stamina']

				# Making the comparisions for the attack and defence 
				if comp_choice_attack > base_attack:
					print("lost")
					decision = "You Lost To Bad!!"
					computer_score += 1

				elif comp_choice_attack < base_attack:
					print("win")
					decision = "You Won Yay!!"
					player_score += 1

				else:
					decision = "You Tied!!"

				# Making the Win or Lose conditions 
				if player_score == 5:
					player_score = 0
					computer_score = 0
					decision = "You Won Yay. Poke Champion!!!" 

				elif computer_score == 5:
					player_score = 0
					computer_score = 0
					decision = "You Lost the Sorry!!!"

				print(pokemon_name)
				print(comp_choice)
				break

			else:
				pass

	return render_template("poke_battle_page.html", computer_score=computer_score, player_score=player_score, computer_choice=comp_choice, user_choice=pokemon_name, beckon_text='VS', decision=decision)

# Making the search_engine page 
@app.route("/search_engine", methods=['GET', 'POST'])
def search_engine():
	global poke_name_in_res, pokemon_name, base_attack, base_defence, base_stamina

	if request.method == "POST":
		webpage = request.form
		pokemon_name = str(webpage['pokeNameInp'])
		print(pokemon_name)

		url = "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json"

		headers = {
		    'x-rapidapi-key': "77ee9999bdmsh61f74ea752bc214p12f26cjsn3bc1f1725b22",
		    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com"
		}

		response = requests.request("GET", url, headers=headers)

		# 1282 in jsonated response

		jsonated_response = response.json()

		for i in range(len(jsonated_response)):
			poke_name_in_res = str(jsonated_response[i]['pokemon_name'])

			if pokemon_name == poke_name_in_res:
				base_attack = jsonated_response[i]['base_attack']
				base_defence = jsonated_response[i]['base_defense']
				base_stamina = jsonated_response[i]['base_stamina']

				print(f"The Base Attack Of the pokemon {poke_name_in_res} is {base_attack}")
				break

			else:
				pass

	return render_template("search_engine.html", pokemon_name=poke_name_in_res, base_attack=base_attack, base_defence=base_defence, base_stamina=base_stamina)

# Run the app 
if __name__ == '__main__':
	app.run(debug=True)