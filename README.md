# Face Recognition App
It identifies unknown individuals and saves them for future investigation and also sends alerts to administrators or security personnel.

## Workflow
1. In every frame, the face locations and co-ordinates are captured.
2. The face-recognition library helps in recognizing the faces, and generate numeric encodings for them.
3. Try to match the generated encodings, with already known face's encodings.
4. If we find any unknown face, we save it to a folder and notify the security personnel.

The above mentioned process, will be repeated for every frame, that is captured during video recording.

**Language and Frameworks:** Python, Computer Vision, Face Recognition, PushBullet
