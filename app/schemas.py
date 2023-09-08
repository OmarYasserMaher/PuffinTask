from pydantic import BaseModel

class FinanceCharacteristicsBase(BaseModel):
    name: str
    value: str

class FinanceCharacteristicsCreate(FinanceCharacteristicsBase):
    pass

class FinanceCharacteristics(FinanceCharacteristicsBase):


    class Config:
        orm_mode = True

class FinanceDataBase(BaseModel):
    pass

class FinanceDataCreate(FinanceDataBase):
    characteristics: list[FinanceCharacteristicsCreate] = []

class FinanceData(FinanceDataBase):
    id: int
    characteristics: list[FinanceCharacteristics] = []

    class Config:
        orm_mode = True