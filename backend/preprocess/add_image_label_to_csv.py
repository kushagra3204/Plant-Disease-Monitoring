import csv
import os

data_path = os.path.join('data','train')
with open('labels.csv','a',newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Id','Disease Type'])
    writer.writerow({'Id':'Id','Disease Type':'Disease Type'})
    for data1_path in os.listdir(data_path):
        new_data_path = os.path.join(data_path,data1_path)
        for data2_path in os.listdir(new_data_path):
            writer = csv.DictWriter(f, fieldnames=['Id','Disease Type'])
            writer.writerow({'Id':data2_path,'Disease Type':data1_path})