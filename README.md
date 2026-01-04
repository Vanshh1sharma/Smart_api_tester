# Smart API Tester

Smart API Tester is a beginner-friendly web application that helps users test APIs and understand their responses in simple language.

When learning APIs, many students find tools like Postman overwhelming. They show too many options and technical terms without clearly explaining what went wrong when a request fails. This project was built to make API testing easier to understand by focusing on clarity instead of complexity.



## 🚀 Features

- Send **GET** and **POST** API requests  
- View API responses in a clean, readable format  
- Get **plain-English explanations** for common HTTP status codes  
- Measure how long each request takes  
- Handle common errors like invalid URLs, bad JSON, or timeouts  



## 🛠️ Tech Stack

- Python  
- Flask  
- Requests  
- HTML  
- CSS  



## 📁 Project Structure

smart_api_tester/
├── app.py
├── requirements.txt
├── templates/
│ └── index.html
└── static/
└── style.css



## ▶️ How to Run Locally

1. Clone the repository  
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Start the application:


python app.py
Open your browser and visit:


http://127.0.0.1:5000

🧪 Example APIs You Can Test

GET Requests :

https://jsonplaceholder.typicode.com/posts/1

https://dog.ceo/api/breeds/image/random

https://randomuser.me/api/

https://official-joke-api.appspot.com/random_joke


POST Request : 

https://jsonplaceholder.typicode.com/posts


Example JSON body:
{
  "title": "Hello",
  "body": "This is a test post",
  "userId": 1
}


# 📚 What I Learned
How HTTP requests and responses work

The difference between GET and POST methods

Meaning of common HTTP status codes

Handling API errors gracefully

Building a simple backend web app using Flask

# 🎯 Why This Project Is Useful

Smart API Tester is useful for:

Students who are new to APIs

Beginners who want to understand API errors instead of guessing

Anyone who wants a simple way to test APIs without complex tools

# 🏁 Future Improvements

Support for custom headers

Authentication support

Saving request history

More detailed error explanations

# 👤 Author

Built by a computer science student as part of a hackathon project to improve understanding of APIs and backend development.