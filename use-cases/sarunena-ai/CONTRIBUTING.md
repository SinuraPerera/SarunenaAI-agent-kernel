# Contributing to SaruNena AI

Thank you for your interest in contributing to SaruNena AI! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Git
- Basic understanding of Flask, Agent Kernel, and agricultural concepts

### Setup Development Environment

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/agent-kernel.git
   cd agent-kernel/use-cases/sarunena-ai
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   ./build.sh
   # Or manually:
   pip install -r ../requirements.txt
   pip install -e .
   ```

5. Copy environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Development Workflow

### Branch Naming

- Use descriptive branch names: `feature/weather-improvements`, `fix/location-parsing`, `docs/update-readme`
- Prefix with:
  - `feature/` for new features
  - `fix/` for bug fixes
  - `docs/` for documentation changes
  - `refactor/` for code refactoring

### Making Changes

1. Create a new branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the coding standards below

3. Test your changes thoroughly

4. Commit your changes:
   ```bash
   git add .
   git commit -m "feat: add weather caching mechanism"
   ```

### Commit Message Format

Follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Test additions or changes
- `chore:` Maintenance tasks

Example:
```
feat(weather): add caching for Open-Meteo API responses

- Implement 5-minute cache for weather data
- Add cache invalidation on error
- Reduce API calls by 60%
```

## Coding Standards

### Python Code

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Keep functions focused and small (< 50 lines)
- Use meaningful variable and function names

Example:
```python
def get_weather_data(latitude: float, longitude: float) -> dict:
    """
    Fetch real-time weather data from Open-Meteo API.
    
    Args:
        latitude: Location latitude coordinate
        longitude: Location longitude coordinate
        
    Returns:
        Dictionary containing temperature, rainfall, and weather conditions
        
    Raises:
        ConnectionError: If API request fails after retries
    """
    # Implementation
```

### HTML/CSS/JavaScript

- Use semantic HTML5 elements
- Follow BEM naming convention for CSS classes
- Keep JavaScript modular and reusable
- Ensure responsive design for mobile devices

### Testing

- Write tests for new features
- Maintain test coverage above 80%
- Use descriptive test names
- Test edge cases and error conditions

Example:
```python
def test_weather_data_caching():
    """Test that weather data is cached correctly."""
    # Arrange
    lat, lon = 6.9271, 79.8612  # Colombo
    
    # Act
    result1 = get_weather_data(lat, lon)
    result2 = get_weather_data(lat, lon)
    
    # Assert
    assert result1 == result2
    assert cache_hits == 1
```

## Project Structure

```
sarunena-ai/
├── sarunena_kernel.py      # Core multi-agent orchestrator
├── tools.py                 # External API integrations
├── app_kernel.py           # Flask web application
├── whatsapp_integration.py  # WhatsApp handler
├── config.yaml             # Configuration
├── pyproject.toml          # Dependencies
├── templates/
│   └── index.html          # Web UI
├── static/
│   ├── style.css           # Styles
│   └── logo.png            # Logo
└── tests/                  # Test files
```

## Areas for Contribution

### High Priority

- **Weather Data**: Add more weather sources, improve caching
- **Disease Database**: Expand crop disease data for Sri Lanka
- **Market Data**: Add real-time market price integration
- **Mobile UI**: Improve mobile responsiveness
- **WhatsApp Integration**: Complete webhook implementation

### Medium Priority

- **Testing**: Add comprehensive test coverage
- **Documentation**: Improve code comments and API docs
- **Performance**: Optimize agent orchestration
- **Localization**: Add Sinhala/Tamil language support

### Low Priority

- **Analytics**: Add usage analytics
- **Notifications**: Push notification system
- **Export**: PDF report generation
- **Maps**: Interactive farm location maps

## Pull Request Process

1. Update documentation if needed
2. Add tests for your changes
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a Pull Request on GitHub with:
   - Clear title and description
   - Reference related issues
   - Screenshots for UI changes
   - Test results

## Review Process

- Maintainers will review your PR within 48 hours
- Address review feedback promptly
- Keep discussion focused and constructive
- Squash commits if requested before merge

## Questions?

- Open an issue for questions or suggestions
- Join our Discord community
- Check existing issues before creating new ones

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to SaruNena AI! 🌾
