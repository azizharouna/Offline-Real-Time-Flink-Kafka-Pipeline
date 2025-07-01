Here’s a concise **Docker & Docker Compose Cheat Sheet** tailored for you:

---

# 🚀 Docker & Docker Compose Cheat Sheet

## 🔹 Docker Commands

| Command                               | Description                                |
| ------------------------------------- | ------------------------------------------ |
| `docker ps`                           | List running containers                    |
| `docker ps -a`                        | List all containers (running + stopped)    |
| `docker images`                       | List all downloaded images                 |
| `docker rmi <image_id>`               | Remove a specific image                    |
| `docker rmi $(docker images -q)`      | Remove **all** images                      |
| `docker rm <container_id>`            | Remove a specific stopped container        |
| `docker rm $(docker ps -a -q)`        | Remove **all** stopped containers          |
| `docker logs <container_id>`          | Show logs of a container                   |
| `docker exec -it <container_id> bash` | Open bash shell inside a running container |

---

## 🔹 Docker Compose Commands

| Command                | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `docker compose up`    | Start containers, pull images if not present     |
| `docker compose up -d` | Start containers in detached (background) mode   |
| `docker compose down`  | Stop and remove containers, networks, volumes    |
| `docker compose ps`    | List containers started by compose               |
| `docker compose logs`  | View logs of all containers in the compose setup |
| `docker compose stop`  | Stop running containers without removing         |

---

## 🔹 Common Flags

| Flag  | Use                                                     |
| ----- | ------------------------------------------------------- |
| `-a`  | Show all (e.g., `docker ps -a` for all containers)      |
| `-q`  | Quiet mode — output only IDs (e.g., `docker images -q`) |
| `-d`  | Detached mode (run containers in the background)        |
| `-it` | Interactive terminal mode (e.g., `docker exec -it`)     |

---

## 🔹 Notes

* `docker compose down` **does not delete images**, only containers, networks, and volumes.
* Use `docker rmi` to clean up images.
* Use `docker rm` to clean up stopped containers.
* Always check running containers with `docker ps` before removing.

---



+ + + 

# Docker & Docker Compose Cheat Sheet

## Docker Basics

| Command                       | Description                                  |
|-------------------------------|----------------------------------------------|
| `docker images`               | List all downloaded Docker images             |
| `docker ps`                   | List all running containers                    |
| `docker ps -a`                | List all containers (running + stopped)       |
| `docker rmi <image_id>`       | Remove a specific Docker image                 |
| `docker rmi $(docker images -q)` | Remove **all** Docker images (use carefully) |

---

## Docker Compose

| Command                             | Description                                   |
|------------------------------------|-----------------------------------------------|
| `docker compose up`                 | Create and start containers (pull images if missing) |
| `docker compose up -d`              | Run containers in detached (background) mode |
| `docker compose down`               | Stop and remove containers defined in compose file |
| `docker compose ps`                 | List containers started by compose            |
| `docker compose logs`               | View logs from containers                      |
| `docker compose logs -f`            | Follow logs live                               |

---

## Useful Tips

- To rebuild images after changes:  
  ```bash
  docker compose up --build
