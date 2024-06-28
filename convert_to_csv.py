import json
import csv

def extract_data_from_json_list(json_file_path, csv_file_path):
    # Define the headers
    headers = ['NCT Number', 'Study Title', 'Study Status', 'Study URL', 'Sponser', 'Condition', 'Study Type', 'Intervention']

    # Load the JSON file
    with open(json_file_path, 'r') as json_file:
        data_list = json.load(json_file)
    
    # Prepare the CSV file for writing
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the headers
        writer.writerow(headers)
        
        # loop through each trial and extract its data
        for data in data_list:
            
            # To get the values of Intervention list
            Intervention_list=data['protocolSection'].get('armsInterventionsModule', {}).get('interventions', [])
            # To get the values from the dictionaries inside the Intervention_list as a single string
            Intervention_names = '| '.join([intervention['name'] for intervention in Intervention_list if 'name' in intervention])

            # Extract the desired fields from each JSON object
            extracted_data = {
                'NCT Number': data['protocolSection']['identificationModule'].get('nctId',''),
                'Study Title': data['protocolSection']['identificationModule'].get('briefTitle', ''),
                'Study Status': data['protocolSection']['statusModule'].get('overallStatus', ''),
                'Study URL':"https://clinicaltrials.gov/study/"+data['protocolSection']['identificationModule'].get('nctId',''),
                'Sponser':data['protocolSection']['sponsorCollaboratorsModule']['leadSponsor'].get('name', ''),
                'Condition':'| '.join(data['protocolSection']['conditionsModule'].get('conditions', [])),
                'Study type':data['protocolSection']['designModule'].get('studyType', ''),
                'Interventions': Intervention_names
            }

            # Write the data
            writer.writerow(extracted_data.values())

# Example usage
extract_data_from_json_list('ctg-studies(6).json', 'data.csv')
