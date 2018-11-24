import os
import time

# import face_recognition
import cv2

import bot_telegram

def fill_arrays():
    map = {}
    encodings = []
    i = 0
    for file in os.listdir('img'):
        id, name = file.split('__')
        name = name.split('.')[0]
        map[i] = (id,name,True)
        # encodings.append(face_recognition.
        #           face_encodings(face_recognition.load_image_file(file))[0])
        i+=1
    return map, encodings

def updates_arrays(map, encodings):
    names = []
    for ind in map:
        names.append(map[ind][1])
    for file in os.listdir('img'):
        id, name = file.split('__')
        name = name.split('.')[0]
        if name not in names:
            map[len(map)] = (id,name,True)
            # encodings.append(face_recognition.
            #       face_encodings(face_recognition.load_image_file(file))[0])
    return map, encodings




video_capture = cv2.VideoCapture(0)

# # Load a sample picture and learn how to recognize it.
# tommy_Face = face_recognition.load_image_file("img/img.jpg")
# tommy_face_encoding = face_recognition.face_encodings(tommy_Face)[0]
#
# # Load a second sample picture and learn how to recognize it.
# biden_image = face_recognition.load_image_file("unknown-images/winner.jpg")
# biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Create arrays of known face encodings and their names
# known_face_encodings = [
#     tommy_face_encoding,
#     biden_face_encoding
# ]
# known_face_names = [
#     "Tommy",
#     "Second Tommy"
# ]


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
map = []
known_face_encodings = []

while True:
    if len(map) > 0:
        map, known_face_encodings = updates_arrays(map, known_face_encodings)
    # Grab a single frame of video
    else:
        map, known_face_encodings = fill_arrays()
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = map[first_match_index][1]
                if map[first_match_index][2]:
                    bot_telegram.send_mess(map[first_match_index][0],
                                           "Congratulations {0}! You have a discount!".format(name))
                    map[first_match_index] = \
                        (map[first_match_index][0],map[first_match_index][1],False)
                    face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!§
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()