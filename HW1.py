# EE2405 HW1 by ChenFangYi

# import module #
import csv

# initialize #
cwb_filename = '107061207.csv'
data = []
header = []
target_data = [['C0A880', 0], ['C0F9A0', 0], ['C0G640', 0], ['C0R190', 0], ['C0X260', 0]]

with open(cwb_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        # the following delet unreasonable value of HUMD #
        if float(row['HUMD']) != -99.000 and float(row['HUMD']) != -999.000 :
            # store station id and HUMD to data #
            data.append([row['station_id'], row['HUMD']])
            # summation HUMD if station id is one of tagets #
            if row['station_id'] == 'C0A880' :
                target_data[0][1] += float(row['HUMD'])
            elif row['station_id'] == 'C0F9A0' :
                target_data[1][1] += float(row['HUMD'])
            elif row['station_id'] == 'C0G640' :
                target_data[2][1] += float(row['HUMD'])
            elif row['station_id'] == 'C0R190' :
                target_data[3][1] += float(row['HUMD'])
            elif row['station_id'] == 'C0X260' :
                target_data[4][1] += float(row['HUMD'])
# check if the sum of targets'HUMD is zero #
for i in range(5):
    if target_data[i][1] == 0 :
        target_data[i][1] = 'None'
# print result #
print(target_data)
