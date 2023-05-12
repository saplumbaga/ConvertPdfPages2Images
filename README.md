# ConvertPdfPages2Images

This project contains a Python script that converts PDF files into PNG images. It uses the `pdf2image` library for the conversion. The script allows you to convert all pages of the PDF files or only the first page (cover page).

## Installation

1. Clone this repository:
```
git clone https://github.com/<your_username>/ConvertPdfPages2Images.git
```
2. Navigate to the project directory:
```
cd ConvertPdfPages2Images
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
**Note:** This script requires Poppler to be installed on your machine. You can install it using your package manager (e.g. `brew install poppler` for MacOS, `sudo apt-get install -y poppler-utils` for Ubuntu). If you are on Windows, you can find binaries [here](http://blog.alivate.com.au/poppler-windows/).

## Usage

1. Put all the PDF files you want to convert into the `PDF_Files` directory.
2. Run the script:
```
python app.py
```
3. The converted PNG images will be saved in the `PNG_Outputs` directory.

### Only convert the first page

By default, the script is set to convert only the first page of each PDF file. If you want to convert all pages, open `app.py` and change the `only_cover` variable at the top to `False`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
