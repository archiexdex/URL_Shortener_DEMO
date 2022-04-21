
<!-- ABOUT THE PROJECT -->
## URL Shortener DEMO
URL Shortener is a popular service like reurl.cc. The demo uses python flask as backend and SQLite as database. Since AWS service needs to cost money, the CI/CD and AWS CodeDeploy won't put on this repo.

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

#### pipenv
  ```sh
  pip install pipenv
  pipenv --version # pipenv, version 2022.4.8
  ```

### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/archiexdex/URL_Shortener_DEMO.git
  ```
2. Install python packages
  ```sh
  cd ./URL_Shortener_DEMO
  # Install the package
  pipenv install
  # Enter the environment
  pipenv shell
  ```
3. Set your `.env`
  ```sh
  SECRET_KEY=<YOUR SECRET KEY>
  DATABASE_URL=sqlite:///url.db
  APP_SETTINGS=config.DevelopmentConfig
  FLASK_APP=core
  ```
4. Run `.env`
  ```sh
  source .env
  ```
5. Build your database
  ```sh
  flask db init
  #flask db migrate
  #flask db upgrade
  ```
6. Run with flask
  ```sh
  flask run
  ```
