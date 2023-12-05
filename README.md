# Chat Application using Django Channels

This repository contains a simple chat application built with Django Channels. Django Channels extends Django to handle WebSockets, allowing real-time communication between clients and the server.

## Features

- Real-time chat using WebSockets
- User authentication and authorization
- Multiple chat rooms
- Message history

## Requirements

- Python 3.x
- Django
- Channels
- Redis (for handling WebSocket connections)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chat-application.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chat-application
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Make migrations and apply them:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000` to access the chat application.

## Configuration

### WebSocket Configuration

Django Channels requires a channel layer to handle WebSocket connections. By default, this application is configured to use Redis as the channel layer. Make sure you have Redis installed and running.

Configure the channel layer in your Django settings:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    'channels',
]

# Use channels layer as the default backend for Django
ASGI_APPLICATION = 'your_project.routing.application'

# Use Redis as the channel layer
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

### Routing Configuration

Create a `routing.py` file in your project directory:

```python
# routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter(
    {
        'websocket': AuthMiddlewareStack(
            URLRouter(
                # your routing configuration here
            )
        ),
    }
)
```

Replace the comment in `routing.py` with the actual routing configuration for your chat application.

## Usage

1. Create a user account or log in.
2. Join an existing chat room or create a new one.
3. Start chatting in real-time!

Feel free to explore the codebase and customize the application to fit your specific requirements. If you have any questions or issues, please open an [issue](https://github.com/yourusername/chat-application/issues).

Happy chatting!
