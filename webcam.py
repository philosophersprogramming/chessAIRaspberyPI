import cv2
import io

def capture_as_stream():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Couldn't open the webcam")
        return None

    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, save it as a byte stream
    if ret:
        # Encode the frame as JPEG
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        _, jpeg_data = cv2.imencode('.jpg', frame, encode_param)
        
        # Save the JPEG data into a byte stream
        stream = io.BytesIO(jpeg_data)
        
        # Release the webcam
        cap.release()
        
        return stream
    else:
        print("Error: Couldn't capture a frame")
        cap.release()
        return None

# Call the function to capture the photo as a byte stream
# photo_stream = capture_as_stream()

# Now you can use `photo_stream` as needed, for example, you can send it via HTTP request.
