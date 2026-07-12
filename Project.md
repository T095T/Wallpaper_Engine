# Project Specification: AuraWall

## Overview

AuraWall is an AI-powered wallpaper generation platform that creates beautiful, personalized wallpapers based on a user's mood, aesthetic preferences, colors, and optional quotes.

The goal is to provide a premium user experience where users don't need to write complicated prompts. Instead, they make a few simple selections, and the backend intelligently generates an optimized prompt for the AI image model.

This project is intended to be built as a production-ready SaaS MVP.

---

# Tech Stack

## Frontend
- Next.js (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui
- TanStack Query
- React Hook Form
- Zod

## Backend
- Django
- Django REST Framework
- PostgreSQL
- Django Simple JWT
- Celery
- Redis

## Storage
- AWS S3 (or Cloudinary initially)

## Deployment
- Docker
- Docker Compose
- Nginx
- GitHub Actions (later)

---

# Product Vision

Users should never need to understand prompt engineering.

Instead of typing long prompts, they simply choose:

- Mood
- Style
- Color Palette
- Device
- Optional Quote

The backend constructs an optimized prompt and generates a wallpaper.

The product should feel like a design tool rather than an AI chatbot.

---

# Core User Flow

Landing Page

↓

Login / Continue as Guest

↓

Generate Wallpaper

↓

Choose Mood

↓

Choose Style

↓

Choose Color Palette

↓

Choose Device

↓

(Optional) Enter Quote

↓

Generate Wallpaper

↓

Preview

↓

Download

↓

Save to Gallery

---

# MVP Features

## Authentication

- Register
- Login
- JWT Authentication
- Logout
- Guest Mode (later)

---

## Wallpaper Generator

User selects:

- Mood
- Style
- Color Palette
- Device Resolution
- Optional Quote

Backend creates an optimized prompt.

Calls image generation model.

Returns wallpaper.

Stores wallpaper metadata.

---

## Gallery

User can:

- View generated wallpapers
- Download wallpapers
- Delete wallpapers
- View generation history

---

## Prompt Builder

This is the heart of the application.

Users never interact with prompts directly.

Backend converts user selections into a professional AI prompt.

Example

Input

Mood:
Coding

Style:
Minimal

Color:
Blue

Quote:
Discipline beats motivation.

Backend Prompt

"A premium minimalist coding workspace wallpaper with deep navy blue gradients, cinematic lighting, subtle neon accents, clean typography placed in safe lock-screen areas, highly readable quote, modern UI inspired composition, ultra detailed digital artwork, 4K wallpaper."

Prompt generation should be modular and easily extendable.

---

# Device Support

Initial

- Mobile Portrait
- Desktop Landscape

Later

- Tablet
- Ultrawide
- Dual Monitor

---

# Mood Options

- Motivated
- Calm
- Focused
- Gaming
- Coding
- Study
- Nature
- Dark
- Minimal

---

# Style Options

- Minimal
- Cyberpunk
- Anime Inspired
- Nature
- Abstract
- Retro
- Futuristic
- Synthwave
- Watercolor

Do NOT use copyrighted names like:

- Goku
- Naruto
- Spider-Man

Instead use generic descriptions.

---

# Color Palettes

Users can

- Pick custom color
or

Choose presets

Examples

- Ocean Blue
- Midnight Black
- Sunset Orange
- Forest Green
- Lavender
- Monochrome
- Neon Purple

---

# Quote

Optional.

If empty

Backend may generate a quote using an LLM.

Future

Categories

- Motivation
- Coding
- Stoicism
- Business
- Gym
- Philosophy
- Productivity

---

# Database Design

## User

- id
- email
- password
- created_at

---

## Wallpaper

- id
- user
- image_url
- mood
- style
- palette
- quote
- prompt
- prompt_version
- device
- created_at
- download_count

---

# Django Apps

accounts/

Authentication

wallpapers/

Wallpaper CRUD

generator/

Prompt Builder

AI Integration

gallery/

Saved Wallpapers

common/

Utilities

---

# REST API

Authentication

POST /api/auth/register

POST /api/auth/login

POST /api/auth/refresh

---

Generation

POST /api/generate

GET /api/generate/{id}

---

Gallery

GET /api/gallery

GET /api/gallery/{id}

DELETE /api/gallery/{id}

---

User

GET /api/profile

---

# Backend Architecture

Frontend

↓

DRF API

↓

Generator Service

↓

Prompt Builder

↓

Image Generation Provider

↓

Store Image

↓

Save Metadata

↓

Return Response

Business logic should remain inside services.

Views should stay thin.

---

# Suggested Project Structure

backend/

config/

accounts/

wallpapers/

generator/

gallery/

common/

media/

requirements/

frontend/

app/

components/

hooks/

lib/

types/

docker/

docker-compose.yml

README.md

---

# Phase 1

Project Setup

- Docker
- PostgreSQL
- Django
- DRF
- JWT
- Next.js
- Tailwind

Deliverable

Working frontend connected to backend.

---

# Phase 2

Authentication

Deliverable

User registration and login complete.

---

# Phase 3

Wallpaper Generator

Deliverable

Generate first wallpaper.

---

# Phase 4

Prompt Builder

Deliverable

Professional prompts generated automatically.

---

# Phase 5

Gallery

Deliverable

Users can save and download wallpapers.

---

# Phase 6

Polish

- Responsive UI
- Loading states
- Error handling
- Empty states

---

# Phase 7

Production

- Docker
- Celery
- Redis
- Async generation

---

# Version 1.1

- AI Quote Generation
- Favorite Wallpapers
- Prompt Presets
- Better Prompt Builder

---

# Version 1.2

- Daily Wallpaper
- Share Wallpaper
- Collections
- Analytics

---

# Version 2

- AI remembers user preferences
- Daily personalized wallpaper
- Premium Subscription
- Scheduled wallpaper generation
- Multiple AI providers

---

# Coding Standards

Backend

- Follow Django Best Practices
- Service Layer Architecture
- Fat Services, Thin Views
- Type hints where possible
- DRF ViewSets only where appropriate
- Reusable serializers
- Environment variables for secrets

Frontend

- Reusable components
- Server Components where appropriate
- Client Components only when required
- Keep business logic outside UI components

---

# Design Principles

The application should feel premium.

Prioritize:

- Clean UI
- Fast generation
- Beautiful typography
- Consistent spacing
- Excellent mobile experience
- Minimal user input
- Intelligent defaults

The user experience should feel closer to Canva than to ChatGPT.

---

# Primary Goal

Build a production-quality AI SaaS MVP that demonstrates:

- Backend Engineering
- Django REST Framework
- AI Integration
- Prompt Engineering
- Docker
- Authentication
- Modern Frontend
- Production Architecture

The codebase should be modular, scalable, and easy to extend with future AI capabilities.