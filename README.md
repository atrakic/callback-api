# OpenAPI Prototype

This repository provides a Dockerized prototype environment using the OpenAPI specification. It simplifies the process of testing and developing APIs by leveraging tools like Swagger UI and a Python-based testing framework.

## Features
- Dockerized environment for easy setup and use.
- OpenAPI specification for API documentation and testing.
- Python-based API testing suite.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/atrakic/openapi-prototype.git
   cd openapi-prototype
   ```

2. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

3. Access the Swagger UI at `http://localhost:8080`.

## Testing Instructions

1. Install Python dependencies:
   ```bash
   pip install requests pytest
   ```

2. Run the API tests:
   ```bash
   pytest tests/
   ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss your ideas.
