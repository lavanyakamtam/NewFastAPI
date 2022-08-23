from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def show():
    return {'data':{'current':'work'}}

@app.get('/about')
def about():
    return {'data':'about page'}
