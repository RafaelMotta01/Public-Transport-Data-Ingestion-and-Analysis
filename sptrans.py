# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252
#!/usr/bin/python3.4
if __name__ == '__main__':
    import requests
    import json
    import time
    h = time.strftime("%H:%M")
    import datetime
    session = requests.Session()
    headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
    
                }
    
    url = "http://api.olhovivo.sptrans.com.br/v2.1/"
    r = session.post(url+"Login/Autenticar?token=9dac5122b12c0e6aacfc7b6922dead75ce7368011c53b6ee9ea9011f5cc5ac24", headers=headers)
    #print(r)
    
    
    def _get(path):
        response = session.get(url + path)
        data = response.json()
        return data
    
    line = _get("Posicao")
    #line = _get("Posicao/Linha?codigoLinha=1273")
    #print(line)
    j = json.dumps(line)
    jj = json.loads(j)
    hora = ''
    linha = ''
    origem = ''
    destino = ''
    x = ''
    y = ''
    hora = ''
    for key, value in jj.items():
        k1 = key
        v1 = value
        if k1 == 'l':
            count = len(v1)
            for idx, item in enumerate(v1):
                a = v1[idx]
                for key2, value2 in a.items(): 
                    if key2 == 'c': 
                        linha = value2 
                    if key2 == 'lt0': 
                        origem = value2 
                    if key2 == 'lt1': 
                        destino = value2 
                    if key2 == 'vs': 
                        v2 = value2[0] 
                        for key3, value3 in v2.items(): 
                            if key3 == 'py': 
                                y = value3 
                            if key3 == 'px': 
                                x = value3 
                            if key3 == 'ta':
                                hora = value3
                                hora = datetime.datetime.strptime(hora.replace('Z',''), '%Y-%m-%dT%H:%M:%S')
                                print("{};{};{};{};{};{}".format(hora, linha, origem, destino,x,y))

					

