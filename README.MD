# remove_bg 🎨

A cloud-native image background removal service showcasing modern DevOps practices and multi-cloud architecture.

[![Deploy Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Docker](https://img.shields.io/badge/docker-automated-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)]()

---

## 📋 About

This is my personal project demonstrating a production-ready image background removal service. Users can upload images and get them back with backgrounds removed instantly. 

The project showcases my skills in:
- Building scalable cloud applications
- Implementing automated CI/CD pipelines
- Working with containerization and serverless technologies
- Deploying across multiple cloud providers
- Following DevOps and security best practices



**Architecture Overview:**
- **Frontend**: Static site hosted on Cloudflare Pages for global performance
- **Proxy Layer**: Cloudflare Worker handles routing, CORS, and security
- **Backend**: Python FastAPI service running on Google Cloud Run
- **Automation**: GitHub Actions manages the entire CI/CD pipeline
- **Containerization**: Docker ensures consistent deployments

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Cloudflare Pages | Global CDN, instant deploys |
| **Proxy/Gateway** | Cloudflare Workers | Edge computing, API protection |
| **Backend** | Python + FastAPI | RESTful API, image processing |
| **ML Model** | rembg / U2-Net | Background removal algorithm |
| **Containerization** | Docker | Portable, reproducible builds |
| **Compute** | Google Cloud Run | Serverless, auto-scaling containers |
| **CI/CD** | GitHub Actions | Automated testing and deployment |
| **Registry** | DockerHub | Container image storage |
| **Monitoring** | Cloud Logging + Cloudflare Analytics | Observability and metrics |

---

## ⚙️ CI/CD Pipeline

The project uses GitHub Actions for fully automated deployments:

```
Code Push → GitHub Actions
    ↓
    ├─→ Build Docker Image
    ├─→ Push to DockerHub
    ├─→ Deploy Backend (Cloud Run)
    ├─→ Deploy Proxy (Cloudflare Worker)
    └─→ Deploy Frontend (Cloudflare Pages)
    ↓
Production Ready ✅
```