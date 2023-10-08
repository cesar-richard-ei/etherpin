# EtherPin

EtherPin is a pinboard application for displaying badges earned by users.

## Getting Started

To get started with EtherPin, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run `docker-compose up -d` to start the development environment.
4. Run `docker-compose exec web python manage.py loaddata etherpin/user/fixtures/oauth_apps.json` to set up the OAuth client for development.

## Usage

Once the development environment is set up, you can access EtherPin by navigating to `http://localhost:8000` in your web browser.

## Contributing

If you would like to contribute to EtherPin, please fork the repository and submit a pull request.

## License

EtherPin is licensed under the MIT License. See `LICENSE` for more information.
