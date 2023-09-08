from sqlalchemy.orm import Session
from . import models

def get_finance_data(db: Session, finance_data_id: int):
    return db.query(models.FinanceData).filter(models.FinanceData.id == finance_data_id).first()

def get_finance_data_all(db: Session,skip: int = 0, limit: int = 100 ,characteristics_name: str = None, characteristics_value: str = None):
    query= db.query(models.FinanceData)
    if characteristics_name:
        query = query.join(models.FinanceData.characteristics).filter(models.FinanceCharacteristics.name == characteristics_name)
    if characteristics_value:
        query = query.join(models.FinanceData.characteristics).filter(models.FinanceCharacteristics.value == characteristics_value)
    return query.offset(skip).limit(limit).all()


def delete_finance_data_all(db: Session):
    db.query(models.FinanceCharacteristics).delete()
    db.query(models.FinanceData).delete()
    db.commit()
    return True

def create_finance_data_bulk(db: Session, finance_data: list[models.FinanceData]):
    db.add_all(finance_data)
    db.commit()
    return finance_data