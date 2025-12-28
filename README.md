# Henk Laukka Personal Website

A personal portfolio website built with **Hugo** and hosted at [henkkalaukka.fi](http://henkkalaukka.fi).

## Overview

This repository contains the complete source code for a customized Hugo-based personal website featuring a blog, poetry gallery, and an interactive book tracker. The site is automatically built and deployed to Hetzner via CI/CD pipeline whenever changes are pushed to the main branch.

## Tech Stack

- **Static Site Generator**: [Hugo](https://github.com/gohugoio/hugo/) (Extended version)
- **Base Theme**: [Nightfall](https://github.com/lordmathis/hugo-theme-nightfall) (heavily customized)
- **Styling**: Dart Sass for SCSS compilation
- **Deployment**: GitHub Actions → FTP to Hetzner
- **Book Management**: Python Flask application

## Features

### 📝 Blog
A custom blog section with personalized layout and styling for articles and posts.

### 🖼️ Poems Gallery
An interactive poetry gallery featuring:
- Responsive modal layout
- Mobile-optimized viewing experience
- Clean presentation of poems

### 📚 Book Tracker Gallery
A custom-built book tracking system displaying your reading history:
- Sleek gallery layout showcasing book covers
- Dynamically fetches book metadata from `/data/books.json`
- Ground-up custom implementation with custom styling and functionality

### 🎨 Custom Theme Modifications
The base Nightfall theme has been extensively modified with custom layouts, components, and styling to match the personal branding and feature requirements.

## Project Structure
├── .github/workflows # github actions deployment
├── archetypes/ # Page archetypes for hugo
├── content/ # Markdown source files for all pages
├── data/ # books.json file for book tracker data
├── layouts/ # Custom Hugo templates
├── static/ # Static assets
│ └── blogi/ # Blog images
│ └── books/ # Book cover images
│ └── lyhkarit/ # Book "review" images
│ └── screenshots/ # Blog screenshot images
├── themes/ # Hugo themes (Nightfall base)
└── book-manager/ # Python book management application

## Book Manager

A Python-based management tool for maintaining your book collection:

### Features
- Add new books to your collection
- Manage all book metadata and properties
- Web-based interface running on `localhost:5555`
- Automatically updates `/data/books.json`

### Getting Started

1. Install Python onto your machine (instructions elsewhere)
2. Run the app with pythin app.py
3. Access the interface at http://localhost:5555
4. Use the UI to add and manage books
5. Manual step: Add corresponding book cover images to /static/books/ directory
