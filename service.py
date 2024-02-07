import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException


def get_temperature(url):
    link = f'{url}/status.xml'
    try:
        response = requests.get(link, timeout=3)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            temperature_element = soup.find('s33301')

            if temperature_element:
                temperature = float(temperature_element.text.strip().split(' ')[0])
                return temperature
            else:
                raise HTTPException(status_code=400, detail="Temperature element not found")
        else:
            raise HTTPException(status_code=400, detail=f"Error executing the request: {response.status_code}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error executing the request: {str(e)}")
