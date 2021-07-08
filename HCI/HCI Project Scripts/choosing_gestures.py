import os
import csv
import shutil

DATASET_PATH = '20bn-jester-v1/'
NEW_CSV = 'dataset_refined.csv'

GESTURES = ['Swiping Down', 'Swiping Left', 'Swiping Right', 'Swiping Up', 'Thumb Down', 'Thumb Up', 'Zooming In With Full Hand', 'Zooming In With Two Fingers', 'Zooming Out With Full Hand', 'Zooming Out With Two Fingers', 'No gesture']


if __name__ == "__main__":
    gestures_dir = os.listdir(DATASET_PATH)
    # print(gestures_dir, len(gestures_dir))


    gestures = []
    with open(NEW_CSV, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] in GESTURES:
                # print(row[0], row[1])
                gestures.append(row[0])
            
            


    # print(gestures, len(gestures))

    count = 0
    for data in gestures_dir:
        if data not in gestures:
            count +=1
            print(DATASET_PATH + data)
            shutil.rmtree(DATASET_PATH + data)

    print(count)
