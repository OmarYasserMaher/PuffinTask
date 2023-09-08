import datetime
import time
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from app.utils import transform_scrap_data
from app.webscraper import scrape_yahoo_finance
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/finance_data/all", response_model=list[schemas.FinanceData])
def read_finance_data_all(skip:int =0,limit :int = 100,name:str=None,value:str=None ,db: Session = Depends(get_db)):
    db_finance_data = crud.get_finance_data_all(db, skip=skip, limit=limit, characteristics_name=name, characteristics_value=value)
    if db_finance_data is None:
        raise HTTPException(status_code=404, detail="Finance Data not found")
    return db_finance_data

@app.get("/finance_data/{finance_data_id}", response_model=schemas.FinanceData)
def read_finance_data(finance_data_id: int, db: Session = Depends(get_db)):
    db_finance_data = crud.get_finance_data(db, finance_data_id=finance_data_id)
    if db_finance_data is None:
        raise HTTPException(status_code=404, detail="Finance Data not found")
    return db_finance_data



def cron_fill_data():
    """
    This should be done as a scheduled task using celery beat or something similar
    """
    #run every 6hours
    while True:
        crud.delete_finance_data_all(db=SessionLocal())
        for data in scrape_yahoo_finance():
            data = transform_scrap_data(data)
            crud.create_finance_data_bulk(db=SessionLocal(), finance_data=data)
        time.sleep(60*60*6)
    
import threading
t = threading.Thread(target=cron_fill_data)
t.start()