# Architecting AgriProject: A Microservices Journey

When building scalable platforms for agriculture, managing hundreds of APIs and concurrent user states can quickly become a bottleneck. In our project **AgriProject** (often referred to as FarmFlow), we decided to adopt a microservices architecture right from the start to ensure high availability, clean separation of concerns, and seamless integration of Machine Learning models.

## Why Spring Boot for the Backend?

Spring Boot remains the gold standard for enterprise backend development. Its massive ecosystem and built-in support for Cloud-native patterns made it an obvious choice to handle our **120+ REST APIs**. We utilized:

- **Spring Cloud Eureka** for Service Discovery, allowing our backend components to dynamically find each other.
- **Spring Security + JWT** for stateless, secure authentication across all services, with role-based access for Admins, Farmers, and Users.
- **Caffeine Cache** for high-performance, local caching of static geographical and crop data.
- **HikariCP** for robust database connection pooling against our MySQL instance.

## Integrating Python ML Models

One of the core requirements of AgriProject was running predictive models for smart farming. Instead of trying to force Python ML scripts into a Java environment, we decoupled them:

1. **Python Flask/FastAPI** microservices wrap the Scikit-learn models. We successfully deployed three core models achieving **95%+ accuracy**:
   - **Crop Recommendation** (Model 5)
   - **Smart Pump Control** (Model 6)
   - **Fertilizer Recommendation** (Model 7)
2. The Spring Boot backend acts as an API Gateway and orchestrator, sending asynchronous requests to the Python services using REST clients.
3. Everything is containerized using **Docker** and orchestrated via **Docker Compose** for local development, allowing us to spin up MySQL, Eureka (port 8761), the Java Backend (port 8080), and the ML Service (port 5000) with a single command.

```java
// Example of a simple REST call from Spring Boot to the Python ML Service
@Service
public class YieldPredictionService {
    
    private final RestTemplate restTemplate;
    
    public PredictionResponse getPrediction(PredictionRequest request) {
        String mlServiceUrl = "http://localhost:5000/predict";
        return restTemplate.postForObject(mlServiceUrl, request, PredictionResponse.class);
    }
}
```

## The Modern Frontend Experience

To bring this powerful backend to the users, we built a **React application using Vite**. It features a premium, glassmorphism UI that includes:
- A complete e-commerce shopping flow (Cart → Checkout → Orders).
- Complex address management supporting all 37 Indian states and UTs.
- Interactive dashboards tailored for Users, Farmers, and Admins.

By keeping the frontend completely decoupled from the backend and communicating purely via REST APIs, we achieved a highly scalable and maintainable architecture. Next time, I'll dive deeper into how we transition these containerized services to a Kubernetes cluster with Horizontal Pod Autoscaling!
