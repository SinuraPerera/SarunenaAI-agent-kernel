# 🌱 SaruNena AI – Smart Farming Multi-Agent System

## 🧠 Overview
SaruNena AI is a multi-agent intelligent farming assistant designed to help Sri Lankan farmers make better agricultural decisions using real-time data, AI reasoning, and modular agent-based architecture.

The system combines weather intelligence, crop disease analysis, market insights, risk evaluation, and personalized recommendations into a single smart assistant.

---

## ❗ Problem Statement
Farmers in Sri Lanka face major challenges such as:

- Unpredictable weather conditions
- Lack of early crop disease detection
- Unstable market price information
- Poor access to timely farming advice
- Difficulty making data-driven farming decisions

---

## 💡 Proposed Solution
SaruNena AI solves these problems using a **multi-agent AI system** that:

- Collects real-time weather data
- Detects crop-related risks
- Provides market price insights
- Evaluates farm risk levels
- Generates AI-powered recommendations
- Maintains memory of farmer interactions
- Provides location-based analysis

---

## 🧠 System Architecture

Farmer Input
   │
   ▼
Flask Web Application (UI Layer)
   │
   ▼
Agent Kernel Orchestrator
   │
   ├── Memory Agent
   ├── Location Agent
   ├── Weather Agent
   ├── Disease Agent
   ├── Market Agent
   ├── Risk Agent
   ├── Recommendation Agent
   └── Insight Agent
   │
   ▼
Final Farming Intelligence Output

---

## 🤖 AI Agents

### 1. Memory Agent
Stores previous farmer interactions and crop history.

### 2. Location Agent
Detects farmer location and maps it to coordinates.

### 3. Weather Agent
Fetches real-time weather data using Open-Meteo API.

### 4. Disease Agent
Provides crop disease risk analysis.

### 5. Market Agent
Returns crop market price insights.

### 6. Risk Agent
Calculates overall farm risk score based on weather and crop data.

### 7. Recommendation Agent
Generates farming advice based on risk levels.

### 8. Insight Agent
Provides AI-driven insights for better farming decisions.

---

## 🌐 Technology Stack

- Python
- Flask (Web Framework)
- Open-Meteo API
- JSON-based Memory Storage
- HTML/CSS Frontend
- Agent-based System Design

---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install flask requests