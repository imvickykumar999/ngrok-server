import cv2
import imagezmq

# Initialize the ImageHub to receive frames
# Bind to all network interfaces on port 5555
receiver = imagezmq.ImageHub(open_port='tcp://*:5555')  

print("Client is ready to receive stream...")

try:
    while True:
        # Receive the image frame
        device_name, frame = receiver.recv_image()
        
        # Display the frame
        cv2.imshow(f'Remote Webcam - {device_name}', frame)
        
        # Send acknowledgment
        receiver.send_reply(b'OK')
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Viewer stopped.")

finally:
    cv2.destroyAllWindows()
