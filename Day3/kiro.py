import time
import msvcrt

# Initialize count and sleep time
count = 0
sleep_time = 1.0

# Run the loop indefinitely
while True:
    # Increment count
    count += 1
    
    # Print the current count
    print("Count:", count)
    
    # Check if any key is pressed
    if msvcrt.kbhit():
      key = msvcrt.getch().decode('utf-8')  # Decode the key press to string
      print(f"You hit the '{key}' key")
      if key == 'w':  # Increase sleep time with "w"
          sleep_time += 0.1
      elif key == 's':  # Decrease sleep time with "s"
        sleep_time -= 0.1
        # Ensure sleep_time doesn'  go below 0.1
        sleep_time = max(sleep_time, 0.1)
    
      # Flush the input buffer
      while msvcrt.kbhit():
          key = msvcrt.getch()
          print(key)
    # Wait for the adjusted sleep time
    time.sleep(sleep_time)
