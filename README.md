<div align="center">
Проект начала 2023 года, один из самых первых проектов не по учёбе. Базовый, в одном файле... Хочу видеть эволюцию, поэтому и залил сюда, ничего не меняя.

---
  
# UN3T

### A tiny social network inside Telegram

**An early 2023 experiment that turns a Telegram bot into a shared public chat with user profiles, communities, posts, and subscriptions.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-2.x-2CA5E0?logo=telegram&logoColor=white)](https://docs.aiogram.dev/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram&logoColor=white)](https://core.telegram.org/bots)
[![Status](https://img.shields.io/badge/status-archived%20experiment-6B7280)](#project-status)

</div>

> [!NOTE]
> UN3T is one of my first non-academic projects, written at the beginning of 2023. The original implementation is intentionally preserved in a single file so that the repository remains an honest snapshot of my early development experience.

## About

UN3T is a lightweight social-network prototype implemented as a Telegram bot. Users register a nickname and communicate in a common feed, while community owners can create public channels, publish posts, and gather subscribers.

The entire application runs through Telegram updates using asynchronous handlers from aiogram. All state is kept in memory, making the project compact and easy to study.

## Features

- **User registration** with unique Latin-letter and numeric nicknames
- **Global public feed** where messages are broadcast to every registered user
- **Nickname changes** with notifications for the community
- **Public communities** created and managed by users
- **Community subscriptions** by public name
- **Channel posts** delivered to every subscriber
- **Sticker broadcasting** in the global feed
- **Simple moderation rules** for reserved administrator names

## Bot commands

| Command | Description |
|---|---|
| `/start` or `/help` | Display the command reference |
| `/id <nickname>` | Register in UN3T |
| `/change <nickname>` | Change the current nickname |
| `/new_pub <name>` | Create a public community |
| `/meet_pub <name>` | Join an existing community |
| `/new_post <text>` | Publish a post to your community |
| `/exit` | Leave the global network |

Any ordinary text message is sent to all registered users.

## How it works

```text
Telegram user
     │
     ▼
Telegram Bot API
     │
     ▼
aiogram Dispatcher
     ├── registration handlers
     ├── global chat broadcast
     ├── public community management
     └── post and sticker delivery
     │
     ▼
In-memory Python lists
```

The bot stores:

- Telegram user IDs;
- registered nicknames;
- public community names;
- community administrators;
- subscriber lists.

## Running locally

### Requirements

- Python 3.9 or newer
- a Telegram bot token from [@BotFather](https://t.me/BotFather)
- aiogram 2.x

Clone the repository:

```bash
git clone https://github.com/alimak4v/un3t.git
cd un3t
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the compatible aiogram version:

```bash
pip install "aiogram>=2.20,<3.0"
```

Replace the placeholder in `main.py`:

```python
API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
```

Start the bot:

```bash
python main.py
```

> [!WARNING]
> Never commit a real Telegram token. For a maintained application, load secrets from environment variables instead.

## Current limitations

This repository represents an early prototype rather than a production service:

- all data disappears after a restart;
- there is no database or persistent configuration;
- one process holds the entire application state;
- communities support one administrator each;
- command input has minimal validation;
- there are no automated tests;
- the bot uses aiogram 2.x, whose API differs from aiogram 3.x;
- the original code contains a hard-coded administrator ID.

These limitations are documented rather than hidden because the purpose of the repository is to preserve the original project and show development progress over time.

## What a modern version would add

- persistent users, communities, and posts in PostgreSQL;
- environment-based configuration;
- aiogram 3.x routers and middleware;
- proper entities instead of parallel global lists;
- role-based community administration;
- structured logging and error handling;
- unit and integration tests;
- Docker packaging and automated deployment.

## Project status

**Archived as a historical project.** The original implementation is intentionally kept simple and unchanged.

---

<div align="center">

**A small bot, a first social network, and a visible starting point.**

</div>
