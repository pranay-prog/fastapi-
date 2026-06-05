from fastapi import FastAPI

app = FastAPI()

#users dynamic routes 
@app.get("/users/{user_id}")
def get_users(user_id:int):
    return{"user_id": user_id }

@app.get("/marks/{marks_scored}")
def get_marks(marks_scored:int):
    return{"marks_scored": marks_scored}

@app.get("/names/{name_ofstudent}")
def get_names(name_ofstudent:str):
    return{"name_ofstudent":name_ofstudent}
