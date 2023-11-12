import json
import pandas as pd



def get_json_entry(row):

    return {
        'Name': row['Name'],
        'Gender': row['Gender'],
        #'Age': int(row['Age']),
        #'Date of Birth': row['Date of Birth'],
        'Description' : row['Description'],
        'Occupation': row['Occupation'],
        'Interests': row['Interests'],
        'Likes': row['Likes'],
    }


if __name__ == '__main__':
    people_df = pd.read_csv('resources/output.csv')
    json_list = []
    for index in people_df.index:
        json_list.append(get_json_entry(people_df.loc[index]))
        print(index)

    with open('resources/people_dataset_filtered.json', 'w') as file:
        json_data = json.dumps(json_list)
        file.write(json_data)
