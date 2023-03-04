# ms-fastapi-django

## Project Overview
This project is a web application built with FastAPI, Tesseract OCR, and Uvicorn. 
The application is designed to extract text from images using Tesseract OCR and display the results through a web interface.

## Getting Started
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

## Deploying to AWS
    1. Create an AWS account if you don't already have one.
    2. Set up an EC2 instance to host the application.
    3. Install Docker on the EC2 instance.
    4. Build a Docker image of the application.
    5. Push the Docker image to a container registry such as Docker Hub or Amazon ECR.
    6. Create an Elastic Container Service (ECS) cluster.
    7. Create a task definition for the application.
    8. Create a service for the task definition.
    9. Access the application through the public IP address of the EC2 instance.
