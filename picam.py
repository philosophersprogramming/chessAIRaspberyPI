import io
import picamera
from time import sleep

def capture_as_stream():
    # Initialize the camera
    with picamera.PiCamera() as camera:
        # Wait for the camera to warm up
        sleep(2)
        
        # Capture a photo into a byte stream
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        stream.seek(0)
        
        return stream

# Call the function to capture the photo as a byte stream
photo_stream = capture_as_stream()

# Now you can use `photo_stream` as needed, for example, you can send it via HTTP request.
