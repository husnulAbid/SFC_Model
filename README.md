# SFC_Model

Using SFC models, we can call API to get output from various data analytics code and machine learning model. This tool has been designed and implemented by Husnul Abid.


## Features 

    * Meat consumption data analysis
    * War effect data analysis


## Setup SFC_Model Locally

1. Please clone the repository

2. Create a virtual environment 

3. Install the libraries from requirement.txt

4. Run ``` flask run ``` command

5. The application should run at http://127.0.0.1:5000


## Setup SFC_Model Locally using Docker

1. Dockerfile and docker-compose.yml have been implemented with this project

2. To run in Docker, Please install Docker and make sure it's running

3. Run ``` docker-compose up --build ``` and it will export the application and database into images

4. The application should run at http://127.0.0.1:5100

5. Request the API with appropriate body


## Tech Stack Used

    - Flask
    - Data Analytics
    - Machine Learning