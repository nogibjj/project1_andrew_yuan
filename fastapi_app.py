from fastapi import FastAPI
import uvicorn
from data_processing import fetch_country_info

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, welcome to the covid-19 cases dataset!"}

@app.get("/{country_name}")
async def query(country_name):

    result = fetch_country_info(country_name)
    string = "Data for {} is:  {}".format(country_name,result.to_json())
    return {string}


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')