# gsensorAPI
API server

### Usage

```python
import requests

url = "http://127.0.0.1:5000/sensor"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print("CPU Temperature:", data['cpu_temperature'])
    print("CPU Usage:", data['cpu_usage'])
    print("Disk Usage:", data['disk_usage'])
    print("Memory Usage:", data['memory_usage'])
else:
    print("Erro ao acessar a API:", response.status_code)

```


### http

![image](https://github.com/JuanBindez/gsensorAPI/assets/79322362/f00f71c2-5ce5-4115-b7e9-9e95a54da55b)



