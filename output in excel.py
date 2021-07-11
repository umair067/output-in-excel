import pandas as pd
import json, datetime, functools

My_Dict = {
'person_1': { 'name': 'Abdul Rafay', 'age': 22, 'Interests': ['football', 'cricket'], 'amount_deposited': [24000, 26000]},
'person_2': { 'name': 'Nancy James', 'age': 23, 'Interests': ['baseball', 'cricket'], 'amount_deposited': [24000, 27000]},
'person_3': { 'name': 'Selena Gomez', 'age': 26, 'Interests': ['baseball', 'table tennis'], 'amount_deposited': [24000, 28000]}
}

a_to_g = [chr(x) for x in range(97, 104)]
s_m_k = [chr(x) for x in [107, 109, 115]]

CURRENT_DATE = datetime.date.today()

def processing(record):
    if record[1]["name"][0].lower() in a_to_g:
        record[1]["name"] = 'Mr. '+record[1]["name"]
    else:
        record[1]["name"] = 'Ms. ' + record[1]["name"]
    temp = record[1].pop('amount_deposited')
    record[1]["Year"] = str(int(CURRENT_DATE.year) - int(record[1]["age"]))
    record[1]["amount_deposited"] = int(functools.reduce(lambda x,y: x+y, temp))
    return record


def writing_file(data):
    try:
        with open('names.json', 'w') as file:
            json.dump(data, file, indent=6)
        return True
    except Exception as e:
        return False


def main():
    mapped = dict(list(map(processing, list(filter(lambda record: record[1]["name"][0].lower() not in s_m_k, My_Dict.items())))))
    data = {
        'Current_Date': CURRENT_DATE.strftime('%d-%b-%Y'),
        'Data': mapped
    }

    if writing_file(data):
        print('File Successfully Written.')
    else:
        print('Error Writing File. Please Check That File Have Proper Permissions.')
mapped = dict(list(map(processing, list(filter(lambda record: record[1]["name"][0].lower() not in s_m_k, My_Dict.items())))))
data = {
    'Current_Date': CURRENT_DATE.strftime('%d-%b-%Y'),
    'Data': mapped}

if writing_file(data):
    print('File Successfully Written.')
else:
    print('Error Writing File. Please Check That File Have Proper Permissions.')

x=[]
for k ,i in mapped.items():
  x.append(i)


dataframe = pd.DataFrame(x)
dataframe.to_csv('csv_file3.csv')

for key, value in mapped.items():
  print (value)