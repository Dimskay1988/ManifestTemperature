# ManifestTemperature

Obtaining temperature value from STE 2 lite sensor

<div style="text-align:center;">
    <img src="images/image_2024_02_15T10_42_27_147Z.png" alt="Temperature Sensor">
</div>

# Installation and start project
<details>

Create a virtual environment
```sh
python -m venv venv
```
Then activate the virtual environment
```sh
source venv/bin/activate  
```
Install all dependencies
```sh
pip install -r requirements.txt  
```
Start the project
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```
</details>

# Start at the exhibition
<details>
Go to project directory

```sh
cd Documents/ManifestTemperature
```

Activate the virtual environment

```sh
source venv/bin/activate
```

Start the project
```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

Start the serveo in the new terminal
```sh
ssh -R manifest-temperature-sensor:80:localhost:8000 serveo.net
```
</details>

# Command to start a domain

<details>

```sh
ssh -R manifesttemperaturesensor:80:localhost:8000 serveo.net
```

```sh
ssh -R manifest-temp-sensor:80:localhost:8000 serveo.net
```

```sh
ssh -R manifest-temperature-sensor:80:localhost:8000 serveo.net
```

url to temperature:

https://manifest-temperature-sensor.serveo.net/get_temperature

</details>


# Utilities
<details>

Link for device information
https://www.hw-group.com/device/ste2-lite

Link for settings domain
https://serveo.net/

Link to a program for searching for devices on the network, available only on the Windows operating system
https://www.hw-group.com/files/download/sw/version/hwg-config_1-2-3.exe

</details>