from typing import Union
def inr_to_usd(value:float) -> Union [float,None]:
    try:
        conversion_rate = 75
        value = value / conversion_rate
        return value
    except TypeError :
        return None
    inr_to_usd('23')
     
    


    