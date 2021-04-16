import json
import csv

with open ('C:/Users/dfocus/PycharmProjects/pythonProject/center_GIN00010M.json', 'r', encoding='UTF8') as in_file, open ('C:/Users/dfocus/PycharmProjects/pythonProject/test.txt', 'w', newline='') as out_file:

    json_data = json.load(in_file)

    csv = csv.writer(out_file)

    # print(json.dumps(json_data, indent='\t'))
    # print(json_data[0]['LA']);

    csv.writerow(['LGDNG_CD', 'CTPV_NM', 'CTGG_NM', 'EMD_NM', 'LA', 'LNGT'])

    for player in json_data:

        # print(player['CTPV_NM', 'CTGG_NM'] + '\t' + player['CTGG_NM'] + '\t' + player['EMD_NM'])

        csv.writerow([player['LGDNG_CD'], player['CTPV_NM'], player['CTGG_NM'], player['EMD_NM'], player['LA'], player['LNGT']])