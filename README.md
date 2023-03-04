# ms-fastapi-django

## Project Overview
This project is a web application built with FastAPI, Tesseract OCR, and Uvicorn. 
The application is designed to extract text from images using Tesseract OCR and display the results through a web interface.

## Project Overview
To get started, you will need to clone the repository to your local machine:  
 ``` 
git clone https://github.com/ruzica4/ocr-using-fastAPI-tesseract.git 
```
Next, you will need to install the project dependencies. You can use pip for this:  
 ``` 
pip install -r requirements.txt
 ``` 
To run the application locally, you can use the following command:  
 ``` 
uvicorn app.main:app --reload 
``` 
This will start the application and make it available at http://localhost:8000.
