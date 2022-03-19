from app import app
from app.phasmophobia import phasmophobia
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

@app.get('/')
async def root():
	return {
		'Games':[
			"Phasmophobia"
		]
	}

@app.get("/phasmophobia-generate", response_class=HTMLResponse)
async def phasmophobia_game_generator(map_size: bool = False, map_name: bool = False, difficulty: bool = False, challenge: bool = False, equipment: bool = False):
	data = phasmophobia.generate_game(map_size = map_size, map_name = map_name, difficulty = difficulty, challenge = challenge, equipment = equipment)
	return phasmophobia.get_game_html(data)

app.mount("/", StaticFiles(directory="static",html = True), name="static")