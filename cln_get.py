import requests

requests
res = requests.post('http://localhost:5000/api/sort_avg/', 
                    json={"l_data":[1, '4', 5, 6 , 'a', 'azaza', 12, 34, 0]})
if res.ok:
    print(res.json())