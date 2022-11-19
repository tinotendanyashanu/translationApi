from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator 
import task

app = FastAPI()

langueges = ["English" , "French","German","Romanian"]

class Translation(BaseModel):
    text: str
    base_lang:str
    final_lang: str 

    @validator('base_lung','final_lang')
    def valid_lang(cls,lang):
        if lang not in langueges:
            raise ValueError("Invalid languege")
        return lang

## route 1
## Test if evrything is working 
## {"mmessage": "Hellow world"}
@app.get("/")
def get_root():
    return {"mmessage": "Hellow world"} 

## route 2: / translate 
## Take in translation request , and store in the db 
## Return a translation id 

@app.post("/translate")
def post_translation(t:Translation , background_task:BackgroundTasks):
    ## store the translation
    ##run
    
    pass
## route 3 : / results
## Take in a translation id 
## return the translated id 

