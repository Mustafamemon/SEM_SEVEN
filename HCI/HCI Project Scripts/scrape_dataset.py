import os
import csv
import shutil

DATASET_PATH = '20bn-jester-v1/'
NEW_CSV = 'dataset_refined.csv'



if __name__ == "__main__":
    gestures_dir = os.listdir(DATASET_PATH)
    # print(gestures_dir, len(gestures_dir))


    dataset = []
    with open(NEW_CSV, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dataset.append(row[0])
            


    # print(dataset, len(dataset))

    count = 0
    for data in gestures_dir:
        if data not in dataset:
            count +=1
            print(DATASET_PATH + data)
            shutil.rmtree(DATASET_PATH + data)

    print(count)
