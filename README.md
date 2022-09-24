# marqo-django

A simple Django web application demonstrating [marqo.ai](https://www.marqo.ai/).

## Setup
1. Clone this repository 
2. Install marqo using the command below (make sure Docker is already installed):
   * `docker rm -f marqo;docker run --name marqo -it --privileged -dp 8882:8882 --add-host host.docker.internal:host-gateway marqoai/marqo:0.0.3`
3. Download the [MovieLens 25M Dataset ](https://files.grouplens.org/datasets/movielens/ml-25m.zip). Extract the downloaded file and copy the `links.csv` and `movies.csv` to the project root directory.
4. Run `install` on the terminal to setup this project.

## Running the Project
1. Open a terminal and change the current working directory to the root directory of this project.
2. Activate virtual environment (the venv directory). On Linux and Mac, you can use the `source venv/bin/activate`.
3. Run the command `python src/manage.py runserver` to run the development server.

## Requirements
* Docker for the marqo to run
* Python 3 for this project