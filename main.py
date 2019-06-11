import glob
import os
import csv

ROOT_FOLDER = '../seal-images/'
ACCURACY = 12
MIN_IMG_WIDTH = 100
MIN_IMG_HEIGHT = 100
ITERATION = '208ff343-ec75-4138-813d-84376fedeea2'
# seal-images/
#   LF1/
#       originals/
#       {iter-id-1}/
#       {iter-id-2}/
#   LF28/
#       originals/
#       {iter-id-1}/
#       {iter-id-2}/

# Get the iteration ID to know which folders to look through
# Loop through each seal's iteration folder
# Loop through each image, and pick out the img size and prediction score
# Compare the prediction and size against params and save file if OK to separate folder
# Create a classifier programmatically and send images


def process_images_for_classifier():

    for pathName in glob.glob(ROOT_FOLDER + '*/[A-Z][0-9]-' + '208ff343-ec75-4138-813d-84376fedeea2' + '.csv'):
        file = open(pathName, "rU")
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            for column in row:
                print(column)


if __name__ == '__main__':
    process_images_for_classifier()
