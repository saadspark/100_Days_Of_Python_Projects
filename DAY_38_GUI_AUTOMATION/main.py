import pyautogui
import time

# Give you time to switch to the desktop if needed
print("You have 5 seconds to switch to the desktop...")
time.sleep(5)

# Click on the Windows icon using the provided coordinates
print("Clicking on the Windows icon...")
pyautogui.click(x=468, y=1055)  # Coordinates for the Windows icon
time.sleep(1)  # Wait for the Start Menu to open

# Type "FileZilla"
print("Searching for 'FileZilla'...")
pyautogui.typewrite('FileZilla', interval=0.1)  # Type the search query
time.sleep(4)  # Wait for search results to appear
pyautogui.press('enter')
# Click on the FileZilla icon at the specified coordinates
print("Clicking on the FileZilla icon...")
pyautogui.leftClick(x=24, y=48)  # Coordinates for the FileZilla icon
time.sleep(2)  # Wait for FileZilla to open

print("Automation complete.")


# print("Move your mouse to the desired position...")
# print("You have 5 seconds to move the mouse.")
# time.sleep(5)  # Wait for 5 seconds

# Get the current mouse position
# x, y = pyautogui.position()
# print(f"Mouse position: x={x}, y={y}")
