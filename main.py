import cv2

# Open video file
video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Couldn't open video file {video_path}")
    exit()

# Access each frame
frame_number = 0
while True:
    ret, frame = cap.read()
    
    if not ret:
        print("End of video or error reading frame.")
        break
    
    # Process the frame (e.g., display or save)
    print(f"Processing frame {frame_number}")
    
    # Example: Display the frame
    cv2.imshow('Frame', frame)
    
    # Wait for 'q' key to stop, or proceed to next frame
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
    frame_number += 1

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
