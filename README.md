# classifier-creator

This project takes the manipulated images from the object detection model, collates the images and sends them to a new classifier to train for individual seal identification.

To kick off, it requires the following criteria:

- the object detection iteration ID, so that it can collect the correct photos
- the minimum % certainty found in the object detection images
- the minimum image size that it should include, even if the % certainty is correct
