# Shortener App

Shortener App is a DRF application for shortening URLs and redirecting to original URLs.

## Requirements

- Python 3.11.5
- Django 5.0.4
- Django REST Framework 3.15.1

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/propercja/shortener-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd shortener-app
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database in `settings.py`.

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

## Usage

1. Run the development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and go to `http://localhost:8000/` to access the API endpoints.

## Contribution

Contributions to the Shortener App are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License
