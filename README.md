# Python Text-To-Audio Converter

This project is a simple yet powerful Python script that converts PDF documents into audio files. Leveraging the pyttsx3 and PyPDF2 libraries, it reads a provided PDF document and generates an MP3 file of the document's text spoken aloud. This tool is perfect for anyone looking to listen to written content on the go, such as audiobooks, lecture notes, or any other PDF document.

## Features
Convert any text-based PDF document into an MP3 audio file.
Utilizes pyttsx3 for text-to-speech (TTS) conversion, allowing for customization of the voice properties.
Uses PyPDF2 for efficient PDF processing and text extraction.

## Installation
Before running the script, ensure you have Python installed on your system. This script was developed with Python 3.9, but it should be compatible with other versions that support the libraries used.

To get started, clone this repository to your local machine:

```
git clone https://github.com/yourusername/Python_Text_To_Audio.git
cd Python_Text_To_Audio
```
Install the required Python packages using pip:

```
pip install pyttsx3 PyPDF2
```

## Usage
Place the PDF document you want to convert into the same directory as the script and name it book.pdf. This version uses "The Time Machine" by H.G. Wells as an example, but you can use any text-based PDF.

Run the script with Python:

```
python main.py
```

The script will process each page of the PDF, output the text to the console, and save the spoken audio to an MP3 file named audio.mp3 in the same directory.

## Customization
The script uses the default voice installed on your system. However, you can customize the voice, speech rate, and volume by modifying the pyttsx3 initialization settings in main.py. Refer to the pyttsx3 documentation for more details on voice properties.

## Contributing
Contributions are welcome! If you have suggestions for improving this script, please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open source and available under the MIT License.
