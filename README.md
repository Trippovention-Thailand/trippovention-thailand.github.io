# Trippovention Thailand Website

A static website for **Trippovention Thailand** (trippovention.co.th) - Your trusted travel partner for Thailand & worldwide tours.

## Overview

This is a simple static website copied from the main Trippovention site (trippovention.com) and customized for the Thailand market with:

- **Thailand as Primary Contact**: Thailand office and phone number (+66 94 931 9572) highlighted first
- **Updated Domain**: All URLs point to trippovention.co.th
- **Thai Email**: query@trippovention.co.th
- **Multilingual Support**: Google Translate integration for English/Thai

## Project Structure

```
trippovention-thailand.github.io/
├── docs/                         # Website files (GitHub Pages serves from here)
│   ├── assets/                   # CSS, JS, images
│   │   ├── images/               # All website images
│   │   ├── styles.css            # Main stylesheet
│   │   ├── app.js                # Main JavaScript
│   │   ├── structured-data.js    # SEO structured data
│   │   └── contact-form.js       # Contact form functionality
│   ├── packages/                 # Tour package pages
│   │   ├── india/                # India packages
│   │   ├── singapore/            # Singapore packages
│   │   └── thailand/             # Thailand packages
│   ├── visa/                     # Visa services
│   ├── index.html                # Homepage
│   ├── contact.html              # Contact page
│   ├── destinations.html         # Destinations by country
│   ├── destinations-themes.html  # Destinations by theme
│   ├── destinations-travelers.html # Destinations by traveler type
│   ├── services.html             # Our services
│   ├── privacy-policy.html       # Privacy policy
│   ├── refund-policy.html        # Refund policy
│   ├── terms-and-conditions.html # Terms & conditions
│   ├── thank-you.html            # Form submission thank you
│   ├── 404.html                  # Error page
│   ├── offline.html              # Offline page
│   ├── CNAME                     # Custom domain
│   ├── robots.txt                # Search engine directives
│   ├── sitemap.xml               # SEO sitemap
│   └── image-sitemap.xml         # Image sitemap
├── .github/                      # GitHub workflows (if any)
├── .gitignore
└── README.md
```

## Pages (22 Total)

### Root Level (12 pages)
- `index.html` - Homepage
- `contact.html` - Contact with office locations
- `destinations.html` - Destinations by country
- `destinations-themes.html` - Destinations by theme
- `destinations-travelers.html` - Destinations by traveler type
- `services.html` - Services overview
- `privacy-policy.html` - Privacy policy
- `refund-policy.html` - Refund policy
- `terms-and-conditions.html` - Terms & conditions
- `thank-you.html` - Thank you page
- `404.html` - Error page
- `offline.html` - Offline page

### Visa (1 page)
- `visa/index.html` - Visa services

### Packages (9 pages)
- `packages/india/index.html` - India packages
- `packages/singapore/index.html` - Singapore packages
- `packages/singapore/family-5days.html` - Singapore family package
- `packages/thailand/index.html` - Thailand packages
- `packages/thailand/pattaya_bangkok.html` - Pattaya Bangkok package
- `packages/thailand/krabi_phuket.html` - Krabi Phuket package
- `packages/thailand/koh_samui_bangkok.html` - Koh Samui Bangkok package
- `packages/thailand/koh_samet_pattaya_bangkok.html` - Koh Samet package
- `packages/thailand/chiang_mai_chiang_rai_bangkok.html` - Chiang Mai package

## Contact Information

### Thailand Office (Primary)
- **Address**: 23/13 M, 12 Nong Pure Subdistrict, Bang Lamung District, Chonburi Province - 20150, Thailand
- **Phone**: +66 94 931 9572
- **WhatsApp**: +66 94 931 9572
- **Email**: query@trippovention.co.th

### India Office (Secondary)
- **Address**: Unit No. 337 A, 3rd Floor, Spaze IT Park, Tower A, Sector 49, Sohna Road, Gurgaon, Haryana - 122018
- **Phone**: +91 73030 10446
- **Landline**: +91 124 418 2575

## Deployment

### GitHub Pages

1. Push changes to the repository
2. Go to Repository Settings → Pages
3. Set Source to "Deploy from a branch"
4. Select `main` branch and `/docs` folder
5. Save and wait for deployment

The site will be available at:
- `https://trippovention-thailand.github.io/`
- `https://trippovention.co.th` (custom domain)

### Custom Domain Setup

The `CNAME` file in `/docs` contains `trippovention.co.th`. Configure your DNS:

| Type  | Name | Value                              |
|-------|------|------------------------------------|
| CNAME | www  | trippovention-thailand.github.io   |
| A     | @    | 185.199.108.153                    |
| A     | @    | 185.199.109.153                    |
| A     | @    | 185.199.110.153                    |
| A     | @    | 185.199.111.153                    |

## Making Changes

Since this is a simple static site, just edit the HTML files directly in the `docs/` folder:

### Update Contact Information
Edit the footer section in each HTML file, or use find-replace across all files.

### Update Phone Numbers
Search and replace phone patterns across all HTML files.

### Add New Pages
1. Copy an existing HTML file as a template
2. Update the content, title, and meta tags
3. Add the page to `sitemap.xml`
4. Update navigation links if needed

### Update Styles
Edit `docs/assets/styles.css`

### Update JavaScript
Edit `docs/assets/app.js` or other JS files in `docs/assets/`

## SEO Configuration

### robots.txt
Located at `docs/robots.txt` - controls search engine crawling.

### Sitemaps
- `docs/sitemap.xml` - Main sitemap with all pages
- `docs/image-sitemap.xml` - Image sitemap for image search

### Structured Data
`docs/assets/structured-data.js` contains Schema.org markup for:
- TravelAgency
- Organization
- ContactPage
- TouristTrip (for package pages)

## Multilingual Support

Google Translate is integrated into the navigation bar:
- English (default)
- Thai (ภาษาไทย)

The widget is styled to match the site design.

## License

Copyright © 2025 Trippovention Thailand. All rights reserved.
