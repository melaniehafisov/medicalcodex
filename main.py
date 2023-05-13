from fastapi import FastAPI
import pandas as pd 

df = pd.read_csv('./data/diagnoses2019.csv')

app = FastAPI()

@app.get('/')
def home():
    return 'this is a API service for MN ICD code details'

@app.get('/preview')
async def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.get('/age/{value}')
async def agecode(value):
    print('value: ', value)
    valueNumber = int(value)
    filtered = df[df['age_group_code'] == valueNumber]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.get('/age/{value}/member/{value2}') 
async def agecode2(value, value2):
    valueNumber = int(value)
    filtered = df[df['age_group_code'] == valueNumber]
    filtered2 = filtered[filtered['unique_member_cnt'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")    
    
   
