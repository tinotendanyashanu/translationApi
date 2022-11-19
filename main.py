from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, validator 

## route 1
## Test if evrything is working 
## {"mmessage": "Hellow world"}

## route 2: / translate 
## Take in translation request , and store in the db 
## Return a translation id 

## route 3 : / results
## Take in a translation id 
## return the translated id 

