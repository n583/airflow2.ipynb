def ver_very_important():
    import requests
    import pandas as pd
    import numpy as np
    import pandasql as ps

    url = "https://api.covid19india.org/data.json"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    data = response.text
    print(type(data))
    json_file = open("data1.json", "w")
    json_file.write(data)
    json_file.close()

    import json

    res = json.loads(response.text)
    print(type(res))

    covi_state = res["statewise"]
    print(type(covi_state))

    df = pd.DataFrame(covi_state)
    df2 = df.set_index('state')
    df2.to_csv("final_covid_table.csv")




