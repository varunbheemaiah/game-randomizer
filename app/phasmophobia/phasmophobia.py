from jinja2 import Environment, FileSystemLoader
from app.phasmophobia.choices import *
from os import path
import random

def pick_map_size():
	"""
	This function will pick a phasmophobia map size to play on.
	"""
	return random.choice(map_size)

def pick_map(size):
	"""
	This function will pick a phasmophobia map to play on.
	"""
	return random.choice(maps[size])

def pick_difficulty():
	"""
	This function will pick a phasmophobia difficulty to play on.
	"""
	return random.choice(difficulty)

def pick_challenge():
	"""
	This function will pick a phasmophobia challenge to play on.
	"""
	return random.choice(challenges)

def choose_equipment(challenge):
	"""
	This function will choose equipment for the phasmophobia game.
	"""
	allowed_equipment = {}

	if challenge == 'Only starter items':
		for key in equipment['starter']:
			allowed_equipment[key] = 1
		for key in equipment['optional']:
			allowed_equipment[key] = 0

	elif challenge == 'Only 1 flashlight':
		flashlightType = random.choice(flashlightTypes)
		allowed_equipment[flashlightType] = 1
		for fType in flashlightTypes:
			if fType != flashlightType:
				allowed_equipment[fType] = 0

	elif challenge == 'No Sanity Pills or Crucifix':
		allowed_equipment['Sanity Pills'] = 0
		allowed_equipment['Crucifix'] = 0

	elif challenge == 'No Flashlight':
		allowed_equipment['Flashlight'] = 0
		allowed_equipment['Strong Flashlight'] = 0

	elif challenge == 'No Smudge Sticks':
		allowed_equipment['Smudge Sticks'] = 0

	for key in equipment['starter']:
		if key not in allowed_equipment:
			allowed_equipment[key] = random.randint(1, equipment['starter'][key])
	
	for key in equipment['optional']:
		if key not in allowed_equipment:
			allowed_equipment[key] = random.randint(0, equipment['optional'][key])

	return allowed_equipment

def generate_game(map_size = True, map_name = True, difficulty = True, challenge = True, equipment = True):
	"""
	This function will generate a phasmophobia game.
	"""
	if map_size or map_name:
		map_size = pick_map_size()
	if map_name:
		map_name = pick_map(map_size)
	if difficulty:
		difficulty = pick_difficulty()
	if challenge:
		challenge = pick_challenge()
	if equipment:
		equipment = choose_equipment(challenge)

	return {
		"difficulty": difficulty,
		"map_size": map_size,
		"map": map_name,
		"challenge": challenge,
		"equipment": equipment
	}

def sentence_case(string):
	"""
	This function will convert a string to sentence case.
	"""
	return string.capitalize()

def get_game_html(data):
	folder = path.abspath("static")
	templateLoader = FileSystemLoader(folder)
	templateEnv = Environment(loader=templateLoader)
	templateEnv.globals['sentence_case'] = sentence_case
	template = templateEnv.get_template('phasmophobiaResponse.html')

	htmlData = template.render(data = data)

	return htmlData