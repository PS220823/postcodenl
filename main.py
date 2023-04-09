from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv('postcodes.csv')

@app.get("/{postcode}/{house_number}")
async def get_place(postcode: str, house_number: str):
    postcode = postcode.lower() # or postcode.upper()
    row = df.loc[df["postal_code"].str.lower() == postcode]
    if not row.empty:
        return {"straat": row.iloc[0]["street"],
                "huisnummer": house_number,
                "postcode": row.iloc[0]["postal_code"],
                "stad": row.iloc[0]["city"],
                "provincie": row.iloc[0]["province"]}
    else:
        return {"error": "postcode not found"}