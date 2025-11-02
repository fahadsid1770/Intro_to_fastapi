# 🚀 Production-Grade FastAPI Implementation

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)

A comprehensive, production-ready FastAPI implementation showcasing modern best practices, security patterns, and scalable architecture for building robust web APIs.

## ✨ Features

### 🔐 **Security & Authentication**
- **JWT Token-based Authentication** with OAuth2PasswordBearer
- **Secure password hashing** using bcrypt via Passlib
- **Token expiration** and refresh mechanisms
- **Protected routes** with dependency injection

### ⚡ **Performance Optimization**
- **Async/await patterns** for I/O-bound operations
- **Connection pooling** for database efficiency
- **CPU-bound task handling** with thread pool execution
- **HTTP middleware** for request/response optimization

### 🛠 **Production Configuration**
- **Environment-based settings** with Pydantic Settings
- **Environment variables** management
- **Host validation** and security middleware
- **Debug mode** control for different environments

### 📊 **API Development Features**
- **Request/Response models** with Pydantic
- **Query parameters** and pagination
- **Path parameters** with type validation
- **Enum usage** for constrained choices
- **Form data handling** with multipart support

## 📁 Project Structure

```
intro-to-fastapi/
├── 📄 README.md                           # This comprehensive guide
├── 📄 pyproject.toml                      # Project configuration & dependencies
├── 📄 main.py                            # Core FastAPI examples & patterns
├── 📄 .env                               # Environment variables template
├── 📄 .gitignore                         # Git ignore rules
├── 📄 uv.lock                            # UV package manager lock file
│
├── 📁 fastapi_in_production/              # Production-grade implementations
│   ├── 📁 async_await_usage/             # Async patterns for I/O operations
│   │   └── 📄 use_async_functions_for_IO_bound_operations.py
│   │
│   ├── 📁 database\ connection\ pooling/  # Database optimization patterns
│   │
│   ├── 📁 environment\ variables\ and\ settings/  # Configuration management
│   │   ├── 📄 using_env_variables.py
│   │   └── 📄 production_ready_using_env_variables.py
│   │
│   ├── 📁 JWT\ authentication/            # Authentication implementation
│   │   └── 📄 jwt-auth.py
│   │
│   ├── 📄 .env                           # Environment configuration
│   └── 📄 source-medium-link.txt         # Reference article
│
└── 📁 Additional Examples/               # Learning & reference files
    ├── 📄 basic_hello.py
    ├── 📄 create_and_read_session_cookie.py
    ├── 📄 dynamic_url.py
    ├── 📄 header.py
    ├── 📄 multipart_form_data.py
    ├── 📄 post_data.py
    ├── 📄 query_params.py
    └── 📄 use_of_enumclass.py
```

## 🚀 Quick Start

### Prerequisites
- Python 3.12 or higher
- UV package manager (recommended) or pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/intro-to-fastapi.git
   cd intro-to-fastapi
   ```

2. **Install dependencies**
   ```bash
   # Using UV (recommended)
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Set up environment variables**
   ```bash
   cp fastapi_in_production/.env .env
   # Edit .env with your configurations
   ```

4. **Run the application**
   ```bash
   # Development mode
   uvicorn main:app --reload
   
   # Production mode
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

5. **Access the API**
   - Interactive documentation: http://localhost:8000/docs
   - Alternative documentation: http://localhost:8000/redoc

## 📚 Usage Examples

### Basic FastAPI Application
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
```

### JWT Authentication
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Token validation logic here
    return user

@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}"}
```

### Async I/O Operations
```python
import httpx

@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.example.com/data")
    return response.json()
```

### Environment Configuration
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    database_url: str
    secret_key: str
    debug: bool = False

    class Config:
        env_file = ".env"
```

## 🛠 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```bash
# Application Settings
APP_NAME="Production FastAPI App"
DEBUG=false
ADMIN_EMAIL="admin@example.com"

# Database
DATABASE_URL="postgresql://user:password@localhost/dbname"

# Security
SECRET_KEY="your-super-secret-key-here"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS & Security
ALLOWED_HOSTS=["localhost:3000", "yourdomain.com"]
```

### Production Settings
- Set `DEBUG=false` for production environments
- Use strong `SECRET_KEY` for JWT token signing
- Configure proper `ALLOWED_HOSTS` for security
- Set up proper `DATABASE_URL` for your database

## 🔧 Production Best Practices Covered

### 1. **Security Implementation**
- JWT-based authentication with proper token validation
- Password hashing with bcrypt
- Host validation middleware
- CORS configuration for web applications

### 2. **Performance Optimization**
- Async/await patterns for non-blocking I/O
- Database connection pooling
- Thread pool execution for CPU-intensive tasks
- Proper middleware usage

### 3. **Configuration Management**
- Environment-based configuration
- Type-safe settings with Pydantic
- Development vs production environment handling
- Secure secret management

### 4. **API Design Patterns**
- RESTful endpoint design
- Request/response validation
- Error handling and status codes
- Pagination and filtering patterns

### 5. **Development Workflow**
- Hot reload for development
- Structured project organization
- Dependency management with UV
- Code formatting with Black

## 🧪 Testing the Implementation

### Run Individual Examples
```bash
# JWT Authentication
python fastapi_in_production/JWT\ authentication/jwt-auth.py

# Environment Settings
python fastapi_in_production/environment\ variables\ and\ settings/production_ready_using_env_variables.py

# Async Operations
python fastapi_in_production/async_await_usage/use_async_functions_for_IO_bound_operations.py
```

### API Endpoints Available
- `GET /` - Basic health check
- `GET /items/` - Item listing with pagination
- `POST /items/` - Create new items
- `GET /models/{model_name}` - Enum validation example
- `POST /token` - JWT token generation
- `GET /protected` - Protected route example
- `GET /external-data` - Async external API call
- `GET /info` - Application information

## 🚀 Deployment

### Using Docker
```dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY . .
RUN pip install -e .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Using Gunicorn
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### Environment-Specific Deployments
- **Development**: Use `uvicorn --reload` for hot reloading
- **Staging**: Enable detailed logging and moderate security
- **Production**: Use Gunicorn with multiple workers and strict security

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add type hints to all functions
- Include docstrings for public methods
- Write comprehensive tests for new features
- Update documentation as needed

## 📖 Learning Resources

This implementation is based on best practices from:
- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI for Production Guide](https://medium.com/@ramanbazhanau/preparing-fastapi-for-production-a-comprehensive-guide-d167e693aa2b)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the inline code comments and docstrings
- **Issues**: Open an issue on GitHub for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas

---

**Built with ❤️ using FastAPI and modern Python practices**

*This project demonstrates production-ready FastAPI implementation patterns suitable for real-world applications.*