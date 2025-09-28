# Docker Setup & Testing Instructions
## 0. 
    While in the main project root directory...
## 1. Build Docker Images

```bash
docker build -t iteminfod ./iteminfod
docker build -t stockinfod ./stockinfod
docker build -t aggregatord ./aggregatord
```

## 2. Create Docker Network

```bash
docker network create microservices-net
```

- Note: This needs to be done to avoid "Internal Server Error" due to aggregator being unable to reach the port which microservices are run on.

## 3. Run Microservices on the Network

```bash
docker run --name iteminfod --network microservices-net -p 8080:8080 iteminfod
docker run --name stockinfod --network microservices-net -p 8081:8081 stockinfod
docker run --name aggregatord --network microservices-net -p 8082:8082 aggregatord
```

## 4. Test Aggregator Endpoint

```bash
curl -X POST http://localhost:8082/lookup -d '{"productID":"XYZ-12345"}' -H "Content-Type: application/json"
```

**Notes:**
- If you get a container name conflict, remove the old container:
	```bash
	docker rm <container_name>
	```
- Make sure all services are running before testing.

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/W4tgy1bp)

