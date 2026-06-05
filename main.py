from fastapi import FastAPI

app = FastAPI()

#home route
@app.get("/")
def home():
    return {"message": "welcome to fastapi"}

#about route
@app.get("/users")
def get_users():
    return {"users": ["mohith", "pranay"]}

#another route
@app.get("/rollno")
def rollno():
    return{"rollno" : [10,20]}