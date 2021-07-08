import os
import csv

CSV_PATH = 'csv_files/jester-v1-validation.csv'
DATASET_PATH = '20bn-jester-v1/'
NEW_CSV = 'dataset_refined.csv'



if __name__ == "__main__":
    gestures_dir = os.listdir(DATASET_PATH)
    # print(gestures_dir, len(gestures_dir))

    gestures = []
    with open(CSV_PATH, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            temp = []
            if str(row[0]).split(";")[0] in gestures_dir:
                temp = [ str(row[0]).split(";")[0], str(row[0]).split(";")[1] ]
                gestures.append(temp)
            
        
    # print(gestures)
    # print(len(gestures))


    with open(NEW_CSV, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(gestures)
    
