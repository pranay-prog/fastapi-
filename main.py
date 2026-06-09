from fastapi import FastAPI
app = FastAPI()

#users?name=rohith    ? here is the query parameter 
#it is basically a filter 

@app.get("/users")
def get_users(name: str = None,price: int=0):
    return {"name":name
            "price":price
    }
#u can handel multiple parameters using query parameter 
