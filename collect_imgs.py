import os
import cv2


directory = './data'
if not os.path.exists(directory):
    os.makedirs(directory)

number_of_classes = 26
dataset_size = 100

capture = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(directory, str(j))):
        os.makedirs(os.path.join(directory, str(j)))

    print('Collecting data for dataset{}'.format(j))

    done = False
    while True:
        ret, frame = capture.read()
        cv2.putText(frame, 'Ready? Press "A" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('a'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = capture.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(directory, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

capture.release()
cv2.destroyAllWindows()
