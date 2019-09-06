# classifier-creator

This project takes the manipulated images from the pattern detection model, collates the images and sends them to a new classifier to train for individual seal identification.

The idea of this project is to automate creating a classifier based on cropped images of patterns of seals.

To kick off, it requires the following criteria:

- the object detection iteration ID, so that it can collect the correct photos
- the minimum % certainty found in the object detection images
- the minimum image size that it should include, even if the % certainty is correct
