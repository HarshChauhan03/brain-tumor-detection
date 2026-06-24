import cv2

# Load MRI Image

image = cv2.imread("brain_mri.jpg")

# Resize Image
image = cv2.resize(
    image,
    (128, 128)
)

print(
    "Image Shape:",
    image.shape
)

print(
    "MRI Preprocessing Completed"
)