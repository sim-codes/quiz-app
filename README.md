# Django Quiz App

This project is a Django API for quiz.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your local machine:

- Python 10+
- Django 5+
- Any additional dependencies, if required

### Installing

1. Clone the repository to your local machine:

```
git clone https://github.com/sim-codes/quiz-app.git
```

2. Navigate to the project directory:

```
cd quiz-app
```

3. Create a virtual environment:

```
python -m venv .venv
```

4. Activate the virtual environment:

- For Windows:
  ```
  .venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source .venv/bin/activate
  ```

5. Install the dependencies:

```
pip install -r requirements.txt
```

6. Perform database migrations:

```
python manage.py migrate
```

7. Create a superuser (admin account):

```
python manage.py createsuperuser
```

8. Start the development server:

```
python manage.py runserver
```
The server will start running at [http://localhost:8000](http://localhost:8000).

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please create a new issue in the [issue tracker](https://github.com/sim-codes/quiz-app/issues) or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your needs.
 