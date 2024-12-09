import cv2
import imagezmq
import socket

# Automatically get the local device's IPv4 address
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Print detected IP for debugging
print(f"Detected local IP: {local_ip}")

# Use the local IPv4 address to connect to the client
sender = imagezmq.ImageSender(connect_to=f'tcp://{local_ip}:5555')  

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
