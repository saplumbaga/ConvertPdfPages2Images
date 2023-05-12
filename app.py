import os
import argparse
from pdf2image import convert_from_path

# Command line argument
parser = argparse.ArgumentParser(description='Convert PDF pages to images.')
parser.add_argument('--only_cover', action='store_true', help='Only convert the first page (cover) of each PDF')
args = parser.parse_args()

# Folders
pdf_folder = 'PDF_Files'
output_folder = 'PNG_Outputs'

# Create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get all pdf files in the directory
pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

# Iterate over all pdf files
for pdf_file in pdf_files:
    # Full pdf path
    pdf_path = os.path.join(pdf_folder, pdf_file)

    # Convert pdf to image
    images = convert_from_path(pdf_path)

    # If only_cover is True, only keep the first image
    if args.only_cover:
        images = images[:1]

    # Save pages as images
    for i, image in enumerate(images):
        # Remove .pdf from the pdf file name
        output_filename = os.path.splitext(pdf_file)[0]

        # Append page number if pdf has multiple pages
        if len(images) > 1:
            output_filename = f"{output_filename}-Page{i+1}"

        # Full output path
        output_path = os.path.join(output_folder, f"{output_filename}.png")

        # Save image
        image.save(output_path, 'PNG')

        ## Print progress
        print(f"PDF: {pdf_file} | Page: {i+1} | Saved to: {output_path}")

print('PDF to PNG conversion done!')
