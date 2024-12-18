# Assignment 2 API Gateway - Local Gateway to Midterm Project

### Overview

This project is a **local API gateway** built with **Flask**. It acts as a proxy for the **CFW SE4458 Midterm Project**, enabling requests to be routed to appropriate endpoints of the midterm service.

---

### Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/BaburG/SE4458-AS2-API-gateway
   cd https://github.com/BaburG/SE4458-AS2-API-gateway
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the gateway**:
   ```bash
   python main.py
   ```

4. The API Gateway will be accessible at `http://127.0.0.1:3000`.

---

### Production

- This application can be containerized using the provided `Dockerfile`.

#### Build and Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t api-gateway .
   ```

2. Run the container:
   ```bash
   docker run -p 3000:3000 api-gateway
   ```

---

### Features

- **Proxying Requests**: The gateway forwards requests to the appropriate midterm project endpoints.
- **Dynamic Routing**: Supports HTTP methods like `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`.

---

### Routes

| **Route**                       | **Description**                                |
|----------------------------------|-----------------------------------------------|
| `GET /all`                      | Retrieve all listings.                        |
| `POST /auth`                    | Authenticate a user and return a JWT.         |
| `POST /host/insert-listing`     | Add a new listing (requires authentication).  |
| `GET /guest/query-listings`     | Search for available listings.                |
| `POST /guest/book`              | Book a listing (requires authentication).     |
| `POST /guest/rate`              | Rate a booking (requires authentication).     |
| `GET /admin/listing-by-rating`  | Fetch listings by rating (requires admin).    |

---

### Assumptions

- The gateway relies on the availability of the **Midterm Project API** at `https://cfw-se4458-midterm.babur-g.workers.dev/v1`.

---

### Example Request

- Proxying a request to retrieve all listings:
   ```bash
   curl --location 'http://127.0.0.1:3000/all'
   ```

---

### Documentation

- **YouTube Presentation & Explanation**: [YouTube Link](https://youtu.be/zr93YTaOJpU)

