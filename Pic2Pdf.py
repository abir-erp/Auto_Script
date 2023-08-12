from fpdf import FPDF
import os

screenshot_path = 'C:/Setup_code/unique_screenshots/'

# Get a list of all image files in the directory
image_files = [os.path.join(screenshot_path, file) for file in os.listdir(screenshot_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Create a PDF object
pdf = FPDF()

# Add images to the PDF
for image_file in image_files:
    pdf.add_page()
    pdf.image(image_file, x=10, y=10, w=190)  # Adjust coordinates and size as needed

# Save the PDF
pdf_output_path = os.path.join(screenshot_path, 'screenshots.pdf')
pdf.output(pdf_output_path)
