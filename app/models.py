from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class FinanceData(Base):
    __tablename__ = "finance_data"

    id = Column(Integer, primary_key=True, index=True)
     
    characteristics = relationship("FinanceCharacteristics", back_populates="finance_data", cascade="all, delete")

class FinanceCharacteristics(Base):
    """
    Finance Characteristics Table
    This approach is taken in case the columns change from the yahoo finance website
    """
    __tablename__ = "finance_characteristics"

    id = Column(Integer, primary_key=True, index=True)
    finance_data_id = Column(Integer, ForeignKey("finance_data.id"))
    name = Column(String, index=True)
    value = Column(String, index=True)

    finance_data = relationship("FinanceData", back_populates="characteristics")