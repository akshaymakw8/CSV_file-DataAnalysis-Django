# Django Data Analysis Web Application

Project Description:

This Django-based web application allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface. The application includes features for file upload, basic data analysis, and data visualization.

Features:
1.File Upload:
- Users can upload CSV files through a simple web interface.
- Uploaded files are stored temporarily for processing.
  
2. Data Processing:

- The application reads the uploaded CSV file using pandas.
- Displays the first few rows of the data.
- Calculates summary statistics (mean, median, standard deviation) for numerical columns.
- Identifies and handles missing values.

3. Data Visualization:

- Generates basic plots such as histograms for numerical columns using matplotlib or seaborn.
- Displays the plots on the web page.

4. User Interface:

- Simple and user-friendly interface using Django templates.
- Organized display of data analysis results and visualizations.

Setup Instructions:

Prerequisites
- Python 3.x
- Django 3.x or 4.x
- pandas
- numpy
- matplotlib
- seaborn

Installation
1. Clone the repository:
  -  git clone https://github.com/akshaymakw8/CSV_file-DataAnalysis-Django.git
  -  cd CSV_file-DataAnalysis-Django
2. Create and activate a virtual environment:
  - python -m venv env
  - source env/bin/activate  # On Windows use `env\Scripts\activate`
3. Install the required packages:
4. Run database migrations:
  - python manage.py makemigration
  - python manage.py migrate
5. Start the Django development server:
  - python manage.py runserver
6. Access the application:
  - Open your web browser and navigate to 'http://127.0.0.1:8000/'.

Usage
1. Upload a CSV File:

  - Navigate to the file upload page.
  - Select and upload a CSV file.
2. View Data Analysis Results:

  - After uploading, the application will display the first few rows of the data.
  - Summary statistics and visualizations will be generated and displayed.

 UI:
 ![image](https://github.com/akshaymakw8/CSV_file-DataAnalysis-Django/assets/126386461/ea5915d1-6904-4e94-9239-06ade2d60565)

 Data Analysis Result:
 ![image](https://github.com/akshaymakw8/CSV_file-DataAnalysis-Django/assets/126386461/587caf7d-b6b6-4eab-84b3-fdf8877a31a7)
 ![image](https://github.com/akshaymakw8/CSV_file-DataAnalysis-Django/assets/126386461/d5e26bf7-f382-478c-9a22-7cb995ed9aa5)
 another csvfile result.
 ![image](https://github.com/akshaymakw8/CSV_file-DataAnalysis-Django/assets/126386461/87c98590-2289-4a47-b054-b13d4ffcabe8)



