import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Removed classify_image function as it is not needed for live camera feed
def start_camera():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame
        img_array = cv2.resize(frame, (224, 224))
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Predict the class of the frame
        predictions = model.predict(img_array)
        decoded_predictions = decode_predictions(predictions, top=1)[0]

        # Draw bounding box and label
        for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
            if score > 0.5:  # Only draw if confidence is above 50%
                cv2.putText(frame, f"{label} ({score:.2f})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.rectangle(frame, (10, 10), (frame.shape[1] - 10, frame.shape[0] - 10), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Camera', frame)

        # Break the loop on 'q' key press or window close
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('Camera', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

# Start the camera
start_camera()