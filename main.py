import re
import os
import csv
import math
import config
from shutil import copy2
from PIL import Image
from train.trainer import create_classifier_model

ITERATION = config.ITERATION


ROOT_FOLDER = '../seal-images/'
CLASSIFIER_FOLDER = '../for-classifier/' + ITERATION + '/'
TEST_IMAGE_FOLDER = '../classifier-test-images/' + ITERATION + '/'
ACCURACY = 12
MIN_IMG_WIDTH = 100
MIN_IMG_HEIGHT = 100
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
# Loop through the seal folders to find the CSV file for the iteration
# Loop through each image, and pick out the prediction score > ACCURACY
# Save the file to a classifier folder
# Compare the prediction and size against params and save file if OK to separate folder
# Create a classifier programmatically and send images


def pick_images_for_classifier():
    print 'pick_images_for_classifier'
    for subdir, dirs, files in os.walk(ROOT_FOLDER):
        regex = '.*-' + ITERATION + '.csv'
        for file in files:
            if re.search(regex, file):
                seal_name = subdir.split('/')[2]

                pathName = os.path.join(subdir, file)
                file = open(pathName, "rU")
                reader = csv.reader(file, delimiter=',')
                for row in reader:
                    for column in row:
                        split_file = column.split('.')
                        if len(split_file) > 2:
                            percentage = float('0.' + split_file[1])
                            if percentage > 0.12:
                                image_path = os.path.join(
                                    subdir, ITERATION, column)
                                folder = CLASSIFIER_FOLDER + seal_name + '/'
                                if not os.path.exists(folder):
                                    os.makedirs(folder)
                                copy2(image_path, folder)


def remove_small_images():
    print 'remove_small_images'
    for subdir, dirs, files in os.walk(CLASSIFIER_FOLDER):
        for file in files:
            pathName = os.path.join(subdir, file)
            im = Image.open(pathName)
            width, height = im.size
            remove = False
            if width < MIN_IMG_WIDTH:
                remove = True
            if height < MIN_IMG_HEIGHT:
                remove = True

            if remove:
                os.remove(pathName)


def pick_out_test_images():
    print 'pick_out_test_images'
    for subdir, dirs, files in os.walk(CLASSIFIER_FOLDER):

        for subdirname in dirs:
            subdir_path = os.path.join(subdir, subdirname)

            number_of_files = len([name for name in os.listdir(
                subdir_path) if os.path.isfile(os.path.join(subdir_path, name))])

            print subdirname
            print subdir_path
            print number_of_files

            test_images = math.ceil(number_of_files*0.1) + 1

            if test_images > 1:

                test_seal_image_folder = TEST_IMAGE_FOLDER + subdirname
                if not os.path.exists(test_seal_image_folder):
                    os.makedirs(test_seal_image_folder)

                for subdir_images, dirs_images, files_images in os.walk(subdir_path):
                    num = 0
                    for file in files_images:
                        if num < test_images:
                            image_path = os.path.join(subdir_images, file)
                            #shutil.move(image_path, test_seal_image_folder)
                            print 'Going to move'
                            print (image_path, test_seal_image_folder)
                            num += 1
                        else:
                            break


if __name__ == '__main__':
    # pick_images_for_classifier()
    # remove_small_images()
    # create_classifier_model()
    pick_out_test_images()
