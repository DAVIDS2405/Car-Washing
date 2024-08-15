# Car Washing Service Backend

## Overview

The **Car Washing Service Backend** is a robust API built with FastAPI to support a car washing service platform. It provides the necessary endpoints for managing customer bookings, tracking car wash status, managing employees, and generating reports.

## Features

- **Customer Management**:
  - APIs for customer registration and profile management
  - Endpoint for booking car wash services
  - Real-time updates on car wash status

- **Admin Features**:
  - Manage bookings and customer profiles through the API
  - Track and manage employee schedules
  - Generate and retrieve reports via API

- **Employee Management**:
  - APIs for viewing daily tasks and updating car wash status
  - Manage employee records and work logs

## Technology Stack

- **Backend**:
  - FastAPI (Python)
  - SQLAlchemy for database ORM
  - PostgreSQL for database management
  - Pydantic for data validation

- **Authentication**:
  - OAuth2 with JWT tokens

- **Deployment**:
  - Docker for containerization
  - CI/CD pipeline with GitHub Actions
  - Deployed on Koyeb

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/car-washing-service-backend.git
    cd car-washing-service-backend
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
   Use the provided `.env.example` file as a reference to create your `.env` file.

4. **Run the Application**:
    ```bash
    uvicorn app.main:app --reload
    ```
   The API will be available at `http://localhost:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation. Once the application is running, you can access the docs at:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please reach out to us at [sebastian2405lucero@hotmail.com](mailto:sebastian2405lucero@hotmail.com).

