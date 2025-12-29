# Trippovention Thailand Website

A static website for Trippovention Thailand (trippovention.co.th) built with [11ty (Eleventy)](https://www.11ty.dev/).

## Features

- **Data-Driven Templates**: Content is separated into JSON data files for easy management
- **Reusable Components**: Nunjucks partials for header, footer, navigation, etc.
- **Multilingual Support**: Google Translate integration for English/Thai
- **Responsive Design**: Mobile-first approach inherited from the original design
- **Performance Optimized**: Static HTML output with optimized assets
- **GitHub Pages Ready**: Builds to `docs/` folder for easy deployment

## Project Structure

```
trippovention-thailand.github.io/
├── src/                          # Source files
│   ├── _data/                    # Global data files (JSON)
│   │   ├── site.json             # Site configuration
│   │   ├── navigation.json       # Navigation structure
│   │   ├── homepage.json         # Homepage content
│   │   ├── visa.json             # Visa services data
│   │   └── packages/             # Package data by country
│   ├── _includes/                # Reusable template partials
│   │   ├── layouts/
│   │   │   └── base.njk          # Base HTML layout
│   │   └── partials/
│   │       ├── head.njk          # <head> section
│   │       ├── nav.njk           # Navigation bar
│   │       ├── footer.njk        # Footer
│   │       └── scripts.njk       # Footer scripts
│   ├── assets/                   # Static assets (CSS, JS, images)
│   ├── packages/                 # Package pages
│   ├── visa/                     # Visa pages
│   └── *.njk                     # Page templates
├── docs/                         # Build output (GitHub Pages serves from here)
├── .eleventy.js                  # 11ty configuration
├── package.json                  # Node dependencies
└── README.md
```

## Development

### Prerequisites

- Node.js 18+
- npm or yarn

### Installation

```bash
npm install
```

### Commands

```bash
# Build to docs/ folder
npm run build

# Development server with hot reload
npm run serve

# Debug mode
npm run debug
```

### Local Development

1. Run `npm run serve` to start the development server
2. Open `http://localhost:8080` in your browser
3. Edit files in `src/` - changes will auto-reload

## Deployment

### GitHub Pages

1. Push changes to the repository
2. Go to Repository Settings → Pages
3. Set Source to "Deploy from a branch"
4. Select `main` branch and `/docs` folder
5. Save and wait for deployment

The site will be available at `https://trippovention-thailand.github.io/` 
or your custom domain if configured (trippovention.co.th).

## Configuration

### Site Settings

Edit `src/_data/site.json` to update:
- Contact information
- Phone numbers
- Email addresses
- Social media links
- Analytics IDs

### Adding New Pages

1. Create a new `.njk` file in `src/`
2. Add front matter with layout, title, description
3. Run build to generate HTML

Example:
```njk
---
layout: layouts/base.njk
title: Page Title
description: Page description
activePage: nav-item-id
---

<section class="section">
  <div class="container">
    <!-- Your content here -->
  </div>
</section>
```

### Adding New Packages

1. Add package data to `src/_data/packages/[country].json`
2. Create template in `src/packages/[country]/index.njk`
3. Reference data using `{% set country = packages.country %}`

## Multilingual Support

Google Translate is integrated into the navigation bar, allowing users to switch between:
- English (default)
- Thai (ภาษาไทย)

The widget is styled to match the site design and can be customized in `src/_includes/partials/head.njk`.

## License

Copyright © 2025 Trippovention Thailand. All rights reserved.
