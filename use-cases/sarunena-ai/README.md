# 🌱 SaruNena AI – Smart Farming Assistant for Sri Lanka

<div align="center">

![SaruNena AI](/static/logo.png)

**A multi-agent AI-powered farming assistant built with Agent Kernel**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)](https://flask.palletsprojects.com/)

</div>

---

## 🎯 Problem Statement

Smallholder farmers in Sri Lanka face critical agricultural challenges:
- **Unpredictable Weather**: Sudden rainfall and climate shifts damage crops without timely alerts
- **Crop Disease**: Limited access to early disease detection and prevention guidance
- **Market Information Gap**: Lack of real-time pricing and market trend data makes selling decisions risky
- **Scattered Knowledge**: Agricultural recommendations come from fragmented sources
- **Language Barriers**: Technical farming advice often only available in English

**Result**: Reduced yields, crop losses, and economic hardship for rural farming families.

---

## ✨ Solution: Multi-Agent AI Assistant

**SaruNena AI** combines real-time weather, disease detection, market intelligence, and AI reasoning into a single **Agent Kernel-powered multi-agent system** that delivers actionable farming advice.

### Key Features
- ✅ **Real-Time Weather Analysis** – Open-Meteo API integration with caching
- ✅ **Crop Disease Detection** – AI-powered risk assessment
- ✅ **Market Price Insights** – Sri Lankan agricultural market data
- ✅ **Comprehensive Risk Scoring** – 0-100 risk index with weighted factors
- ✅ **Actionable Recommendations** – Farmer-friendly guidance
- ✅ **Session Memory** – Agent Kernel-backed context persistence
- ✅ **Modern Web Dashboard** – Interactive farming assistant interface
- ✅ **WhatsApp Integration** – Ready-to-use messaging integration

**Built with Real Agent Kernel** - Uses actual Agent Kernel primitives (Runtime, Session, AgentService, OpenAIModule, OpenAIToolBuilder) from the open-source repository, not custom abstractions.

---

## 🌍 UN Sustainable Development Goal Alignment

**SDG 2: Zero Hunger**
- Improves crop yields through early disease detection
- Reduces post-harvest losses with timely guidance
- Strengthens farmer resilience to climate variability

**SDG 13: Climate Action**
- Enables climate-adaptive agricultural practices
- Reduces input waste through precision farming
- Builds farmer capacity for climate response

---

## 🧠 System Architecture

### Multi-Agent Workflow

```
Farmer Input → SaruNena Triage Agent
                        ↓
                Agent Kernel Runtime
                        ↓
         Parallel Agent Specialists:
         ├─ Location Agent (geocoding)
         ├─ Weather Agent (real-time data)
         ├─ Disease Agent (risk analysis)
         ├─ Market Agent (price insights)
         ├─ Risk Agent (comprehensive scoring)
         ├─ Recommendation Agent (actionable advice)
         └─ Memory Agent (farmer context via Session)
                        ↓
         Aggregated Farming Report
                        ↓
    Dashboard Display & WhatsApp Response
```

### Key Agent Kernel Components

- **Runtime**: Orchestrates agent lifecycle and execution
- **Session**: Per-farmer context persistence (in-memory, Redis, DynamoDB)
- **Module**: OpenAIModule registers specialized agents
- **AgentService**: High-level interface for agent interaction
- **OpenAIToolBuilder**: Binds Python functions as callable tools for agents

---

## 🤖 AI Agents

### 1. Triage Agent
Routes farmer queries to appropriate specialists; synthesizes multi-agent responses into cohesive advice.

### 2. Location Agent
Extracts and resolves farmer location within Sri Lanka; provides geographic context for farming decisions.

### 3. Weather Agent
Fetches real-time weather data (temperature, rainfall, humidity) and translates conditions into farming implications.

### 4. Disease Agent
Analyzes crop disease risk based on reported symptoms and current weather patterns; recommends preventive actions.

### 5. Market Agent
Provides crop-specific pricing trends and demand forecasts for Sri Lankan agricultural markets.

### 6. Risk Agent
Aggregates weather, disease, and market signals into a comprehensive risk score (0-100) and action recommendations.

### 7. Recommendation Agent
Converts risk assessment into practical, farmer-friendly next steps (irrigation adjustments, spraying, harvesting timing, etc.).

### 8. Memory Agent
Stores and retrieves farmer context (location, previous crops, symptoms) using Agent Kernel's Session store for continuity.

---

## 🌐 Technology Stack

- **Multi-Agent Orchestration**: Agent Kernel Framework
- **Agent SDK**: OpenAI Agents SDK with OpenAIToolBuilder for tool binding
- **Session Management**: Agent Kernel Session store (in-memory, Redis, DynamoDB compatible)
- **Web Framework**: Flask with Jinja2 templating
- **External Data**: Open-Meteo API (weather) + comprehensive market/disease database
- **Runtime**: Python 3.12+

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- pip package manager
- (Optional) OpenAI API key for LLM-powered features

### Installation

```bash
cd agent-kernel/use-cases/sarunena-ai
./build.sh
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your configuration
```

### Run the Application

```bash
python app_kernel.py
```

Access the web interface at: http://localhost:5000

---

## 📖 Usage Guide

### Web Interface

1. **Enter your farming query** in the search box
   - Format: `[crop] in [location] with [symptoms]`
   - Example: "tomato in kandy with yellowing leaves"

2. **Click "Analyze"** to process through the multi-agent system

3. **Review the comprehensive dashboard** showing:
   - Weather conditions (real-time from Open-Meteo API)
   - Disease risk analysis (based on symptoms and weather)
   - Market price intelligence (Sri Lankan market data)
   - Comprehensive risk assessment (0-100 score)
   - Actionable recommendations
   - AI-powered insights

### API Usage

```bash
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"query": "rice in anuradhapura with blight symptoms"}'
```

For detailed usage instructions, see [USAGE_GUIDE.md](USAGE_GUIDE.md)

---

## 📁 Project Structure

```
sarunena-ai/
├── sarunena_kernel.py      # Core multi-agent orchestrator
├── tools.py                 # External API integrations
├── app_kernel.py           # Flask web application
├── whatsapp_integration.py  # WhatsApp handler
├── config.yaml             # Configuration
├── pyproject.toml          # Dependencies
├── .env.example            # Environment variables template
├── build.sh                # Setup script
├── templates/
│   └── index.html          # Web UI
├── static/
│   ├── style.css           # Styles
│   └── logo.png            # Logo
├── tests/                  # Test files
├── docs/                   # Documentation
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
└── README.md               # This file
```

---

## 🎨 Features

### Deterministic Mode (Default)
The system works perfectly without an OpenAI API key using:
- Real-time weather data from Open-Meteo API
- Comprehensive Sri Lankan crop disease databases
- Realistic market price data
- Sophisticated risk scoring algorithms

### Multi-Agent LLM Mode (Optional)
With an OpenAI API key, the system additionally provides:
- AI-powered agent orchestration
- Natural language query understanding
- Context-aware recommendations
- Multi-agent collaboration

### Risk Assessment Methodology

The system uses a weighted multi-factor risk model:
- **Weather Risk (40%)**: Temperature, rainfall, humidity, wind
- **Disease Risk (35%)**: Symptoms, weather conditions, crop susceptibility
- **Market Risk (25%)**: Price volatility, demand trends

**Risk Levels:**
- 0-29: LOW RISK (✓ FAVORABLE)
- 30-49: LOW-MEDIUM RISK (✓ MONITOR)
- 50-69: MEDIUM RISK (⚡ CAUTION)
- 70-100: HIGH RISK (⚠️ URGENT)

---

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=. tests/
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- **Weather Data**: Add more weather sources, improve caching
- **Disease Database**: Expand crop disease data for Sri Lanka
- **Market Data**: Add real-time market price integration
- **Mobile UI**: Improve mobile responsiveness
- **WhatsApp Integration**: Complete webhook implementation
- **Localization**: Add Sinhala/Tamil language support

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Agent Kernel Framework**: The core multi-agent orchestration system
- **Open-Meteo API**: Real-time weather data provider
- **OpenAI**: AI model provider for LLM-powered features
- **Sri Lankan Agricultural Community**: Inspiration and domain expertise

---

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the [USAGE_GUIDE.md](USAGE_GUIDE.md)
- Review [CONTRIBUTING.md](CONTRIBUTING.md)

---

<div align="center">

**Built with ❤️ for Sri Lankan Farmers**

[⬆ Back to Top](#-sarunena-ai--smart-farming-assistant-for-sri-lanka)

</div>