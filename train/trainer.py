from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry
import os

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
CLASSIFIER_FOLDER = '../for-classifier/'

# Replace with a valid key
training_key = "<your training key>"
prediction_key = "<your prediction key>"
prediction_resource_id = "<your prediction resource id>"


def create_classifier_model():
    trainer = CustomVisionTrainingClient(training_key, endpoint=ENDPOINT)

    # Create a new project
    print ("Creating project...")
    project = trainer.create_project("Seal ID Classifier")

    tags = {}
    # Make tags for seals
    for subdir, dirs, files in os.walk(CLASSIFIER_FOLDER):

        for subdirname in dirs:
            seal_name = subdirname
            print seal_name

            #tags[seal_name] = trainer.create_tag(project.id, seal_name)

        for file in files:

            print("Adding images...")

            image_list = []
            path_name = os.path.join(subdir, file)
            seal_folder_name = subdir.split('/')[2]
            with open(path_name, "rb") as image_contents:
                print path_name
                print seal_folder_name
                #image_list.append(ImageFileCreateEntry(name=file, contents=image_contents.read(), tag_ids=[tags[seal_folder_name].id]))

    # upload_result = trainer.create_images_from_files(
    #     project.id, images=image_list)
    # if not upload_result.is_batch_successful:
    #     print("Image batch upload failed.")
    #     for image in upload_result.images:
    #         print("Image status: ", image.status)
    #     exit(-1)
