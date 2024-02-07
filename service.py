import requests
from bs4 import BeautifulSoup


def get_temperature():
    url = 'http://192.168.1.151/status.xml'
    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            temperature_element = soup.find('s33301')

            if temperature_element:
                temperature = float(temperature_element.text.strip().split(' ')[0])
                return temperature
            else:
                raise ValueError("Temperature element not found")
        else:
            raise Exception("Error executing the request:", response.status_code)
    except Exception as e:
        raise e



