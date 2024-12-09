import cv2
import imagezmq

CLIENT_IP = input('Enter CLIENT IP : ')
# Initialize the ImageSender to send frames to a specific address
sender = imagezmq.ImageSender(connect_to=f'tcp://{CLIENT_IP}:5555')  

print("Server is ready to stream...")

# Capture frames from the webcam
cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        # Send the frame with a device name
        sender.send_image('webcam', frame)

except KeyboardInterrupt:
    print("Streaming stopped.")

finally:
    cap.release()
