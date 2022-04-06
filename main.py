from fastapi import Request, FastAPI
from json import JSONDecodeError
# import JSONDecodeError

from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from vehicules import Voiture, Bateau, Moto, Avion, voiture1, voiture2, voiture3

app = FastAPI()
@app.get('/vehicules')
def univ():
    return {'info': 'TEST'}

@app.get('/vehicules/{id}')
def getUser(id: int):
    print(f"l'id est le suivant {id}")
    return {'userpage': True}

@app.get('/start')
async def getInfo(request: Request):
    try:
        data = await request.json()
        for i in data:
            print(i)
    except JSONDecodeError:
        return JSONResponse({'error': 'il n y a pas de body'})
    except:
        return JSONResponse({'error': 'interne depuis le serveur'})
    print(f'{data}')
    return JSONResponse({'test': "test"})

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse({"message": "Cette route n'existe pas" })

@app.get('/vehicules/Voiture') 
def getNombreVoiture():
    return 'Nombre de voitures :', {Voiture.counter}

@app.get('/vehicules/Bateau') 
def getNombreBateau():
    return 'Nombre de bateaux :', {Bateau.counter}

@app.get('/vehicules/Moto') 
def getNombreMoto():
    return 'Nombre de motos :', {Moto.counter}

@app.get('/vehicules/Avion') 
def getNombreAvion():
    return 'Nombre d\'avions :', {Avion.counter}

@app.get('/vehicules') 
def getNombreVehicules():
    return 'Nombre de vehicules :', {Voiture.counter+Bateau.counter+Moto.counter+Avion.counter}

@app.get('/km=450000') 
def getNombreKm():
    return 'Nombre de km  :', {voiture1, voiture2, voiture3.counter}

@app.get('/vitesse=240') 
def getVitesseMax():
    return 'Vitesse Max :', {voiture1, voiture2, voiture3.counter}




