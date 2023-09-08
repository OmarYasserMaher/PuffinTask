from .models import FinanceData,FinanceCharacteristics

def transform_scrap_data(data:list):
    transformed_data = []
    for item in data:
        finance_data = FinanceData()
        finance_data.characteristics = []
        for key, value in item.items():
            characteristics = FinanceCharacteristics(name = key, value = value)
            finance_data.characteristics.append(characteristics)
        transformed_data.append(finance_data)
    return transformed_data



