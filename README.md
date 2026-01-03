Smart API Tester

Smart API Tester is a simple web tool built to help beginners understand how APIs work.

When learning APIs, many students struggle with tools like Postman because they feel complex and overwhelming. Error messages and status codes are often shown without any explanation, which makes learning harder. This project was built to make API testing easier to understand by keeping things simple and explaining responses in plain language.

What This Project Does

Allows users to send GET and POST API requests

Displays API responses in a clean and readable format

Explains common HTTP status codes in simple English

Shows how long the request took

Handles common errors like invalid URLs or bad JSON input

Tech Stack Used

Python

Flask

Requests library

HTML and CSS

Project Structure
smart_api_tester/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css

How to Run the Project

Clone the repository

Install the required dependencies:

pip install -r requirements.txt


Start the application:

python app.py


Open your browser and visit:

http://127.0.0.1:5000

Sample APIs You Can Try

GET request

https://jsonplaceholder.typicode.com/posts/1


POST request

https://jsonplaceholder.typicode.com/posts


Example JSON body:

{
  "title": "Hello",
  "body": "This is a test",
  "userId": 1
}

What I Learned From This Project

How API requests and responses actually work

The difference between GET and POST methods

What common HTTP status codes mean

How to handle API errors properly

How to build a basic web application using Flask