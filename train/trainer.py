from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
import os
import config

ENDPOINT = config.ENDPOINT
TRAINING_KEY = config.TRAINING_KEY
ITERATION = config.ITERATION
ACCURACY = config.ACCURACY

CLASSIFIER_FOLDER = '../for-classifier/'


def create_classifier_model():
    trainer = CustomVisionTrainingClient(TRAINING_KEY, endpoint=ENDPOINT)

    # Create a new project
    project_name = "Seal ID Classifier-" + ITERATION + '-' + str(ACCURACY)
    print ("Creating project... " + project_name)
    project = trainer.create_project(project_name)

    tags = {}
    image_list = []

    for subdir, dirs, files in os.walk(CLASSIFIER_FOLDER):

        # Make tags for seals
        for subdirname in dirs:
            seal_name = subdirname
            print seal_name

            tags[seal_name] = trainer.create_tag(project.id, seal_name)

        for file in files:

            print("Adding images...")

            path_name = os.path.join(subdir, file)
            seal_folder_name = subdir.split('/')[2]
            with open(path_name, "rb") as image_contents:
                print path_name
                print seal_folder_name
                image_list.append(ImageFileCreateEntry(
                    name=file, contents=image_contents.read(), tag_ids=[tags[seal_folder_name].id]))

            # batch the requests
            if len(image_list) == 60:
                send_images(trainer, project, image_list)

                image_list = []

    # send last images not hitting the 60 limit
    send_images(trainer, project, image_list)


def send_images(trainer, project, image_list):
    trainer.create_images_from_files(project.id, images=image_list)
