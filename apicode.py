import requests

API_Key='bHGVRhRINKjyJFRXssqYOrfwggioaJlr'
API_Path='https://api.crxcavator.io/v1/'
extension='afebilemcaepdkmhmibgmnpfppnjimjf'

resp = requests.get(
    API_Path+'metadata/'+extension, 
    headers={'APIKey':API_Key})

print(resp.json())


#https://api.crxcavator.io/v1/metadata/afebilemcaepdkmhmibgmnpfppnjimjf?apikey=bHGVRhRINKjyJFRXssqYOrfwggioaJlr