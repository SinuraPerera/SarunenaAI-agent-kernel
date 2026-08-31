# SaruNena AI - Usage Guide

## Quick Start

### 1. Setup (5 minutes)

```bash
cd agent-kernel/use-cases/sarunena-ai
./build.sh
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your OpenAI API key (optional for deterministic mode)
```

### 3. Run the Application

```bash
python app_kernel.py
```

Access at: http://localhost:5000

---

## How to Use

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

Response:
```json
{
  "success": true,
  "analysis": {
    "location": "Anuradhapura",
    "crop": "Rice",
    "temp": 28.5,
    "rain": 2.3,
    "risk_score": 62,
    "risk_level": "Medium Risk",
    "recommendation": "Rice in Anuradhapura needs field inspection...",
    "insight": "Based on moderate rainfall and reported symptoms..."
  }
}
```

---

## Supported Crops

- Tomato
- Rice
- Chili
- Carrot
- Potato
- Onion
- Cabbage
- Banana
- Coconut
- Tea

## Supported Locations (Sri Lanka)

- Kandy
- Colombo
- Galle
- Jaffna
- Anuradhapura
- Nuwara Eliya
- Badulla
- Kurunegala
- Ratnapura
- Matara
- Batticaloa
- Trincomalee
- Ampara
- Vavuniya
- Dambulla

---

## Multi-Agent Architecture

### Agent Workflow

```
User Query → Triage Agent → Parallel Specialists → Aggregated Response
                    ↓
         ├─ Location Agent (geocoding)
         ├─ Weather Agent (Open-Meteo API)
         ├─ Disease Agent (risk analysis)
         ├─ Market Agent (price intelligence)
         ├─ Risk Agent (comprehensive scoring)
         └─ Recommendation Agent (actionable advice)
```

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

## Advanced Features

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

Enable by setting `OPENAI_API_KEY` in `.env`

### WhatsApp Integration

Configure WhatsApp Business API credentials in `.env`:

```bash
WHATSAPP_PHONE_NUMBER_ID=your_id
WHATSAPP_ACCESS_TOKEN=your_token
WHATSAPP_VERIFY_TOKEN=your_verify_token
```

Webhook endpoint: `https://your-domain.com/webhook/whatsapp`

---

## Troubleshooting

### Weather Data Not Loading

- Check internet connection
- Verify Open-Meteo API accessibility
- The system has built-in retry logic (3 attempts with exponential backoff)

### Location Not Recognized

- The system defaults to Colombo for unknown locations
- Try using major district names
- Check spelling of Sri Lankan cities

### High Memory Usage

- Weather data is cached for 5 minutes
- Market data is cached for 1 hour
- Clear cache by restarting the application

### Agent Kernel Module Unavailable

- This is normal if OpenAI agents module is not installed
- The system automatically falls back to deterministic mode
- All core features work perfectly without LLM integration

---

## Performance Tips

1. **Batch Processing**: Process multiple queries sequentially for efficiency
2. **Caching**: Weather and market data are automatically cached
3. **Location Accuracy**: Use specific Sri Lankan district names for better results
4. **Symptom Detail**: Include specific symptoms for more accurate disease assessment

---

## Development

### Project Structure

```
sarunena-ai/
├── sarunena_kernel.py      # Core multi-agent orchestrator
├── tools.py                 # External API integrations
├── app_kernel.py           # Flask web application
├── whatsapp_integration.py  # WhatsApp handler
├── config.yaml             # Configuration
├── pyproject.toml          # Dependencies
├── templates/index.html    # Web UI
├── static/style.css        # Styling
└── agents/                 # Legacy agents (deprecated)
```

### Adding New Crops

Edit `tools.py` - add to `price_data` and `disease_database` dictionaries:

```python
# Market data
"new_crop": {
    "price_range": "Rs. X-Y/kg",
    "trend": "Stable",
    "demand": "High",
    "reason": "Market driver"
}

# Disease data
"new_crop": {
    "diseases": ["Disease 1", "Disease 2"],
    "high_risk_conditions": ["condition1", "condition2"],
    "prevention": "Prevention strategy",
    "optimal_conditions": "Growing conditions"
}
```

### Adding New Locations

Edit `tools.py` - add to `sri_lanka_locations` dictionary:

```python
"new_location": ("New Location, Province, Sri Lanka", (latitude, longitude))
```

---

## Production Deployment

### Environment Variables

```bash
OPENAI_API_KEY=sk-...                    # Optional
WHATSAPP_PHONE_NUMBER_ID=...             # Optional
WHATSAPP_ACCESS_TOKEN=...                 # Optional
WHATSAPP_VERIFY_TOKEN=...                # Optional
AK_SESSION_STORE_TYPE=redis              # Recommended for production
LOG_LEVEL=INFO
```

### Recommended Setup

1. Use Gunicorn or uWSGI for production WSGI server
2. Configure Redis for session storage
3. Set up proper logging and monitoring
4. Use environment-specific configuration files
5. Enable HTTPS for WhatsApp webhooks

### Docker Deployment

```dockerfile
FROM python:3.12
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app_kernel:app", "--bind", "0.0.0.0:5000"]
```

---

## Support

For issues or questions:
1. Check this usage guide
2. Review the main README.md
3. Consult Agent Kernel documentation
4. Open an issue on GitHub

---

## License

This is a use case demonstration of Agent Kernel. See main repository for licensing information.
