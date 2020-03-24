import requests
import csv
import sys

# 'https://chrome.google.com/webstore/detail/speed-tweaks/nmmhkkegccagdldgiimedpiccmgmieda'
store_url='https://chrome.google.com/webstore/detail/speed-tweaks/'
extn_list = []
results = {}

print('reading list of extentions')
with open('extn_id.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sys.stdout.write('.')
        extn_list.append(row['extn_id'])


print("")
print('checking extension status')
for extn_id in extn_list:
    resp = requests.get(store_url+extn_id)
    results[extn_id] = resp.status_code
    sys.stdout.write('.')

print("")
print('writing results')
with open('extn_store_results.csv', 'w') as resultscsv:
    writer = csv.DictWriter(resultscsv, fieldnames=['extn_id', 'status_code'])
    writer.writeheader()
    for extn_id in extn_list:
        row = {'extn_id':extn_id, 'status_code':results[extn_id]}
        writer.writerow(row)
        sys.stdout.write('.')

print("")
print('done')
