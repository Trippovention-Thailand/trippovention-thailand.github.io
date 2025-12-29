/**
 * Trippovention Thailand - Centralized Structured Data Manager
 *
 * This module generates and injects schema.org structured data dynamically
 * to reduce code duplication and improve maintainability.
 *
 * Usage: Call StructuredData.init(config) with page-specific parameters
 */

const StructuredData = (() => {
  // Master configuration - single source of truth for Thailand site
  const COMPANY_INFO = {
    name: "Trippovention Thailand",
    url: "https://trippovention.co.th",
    logo: "https://trippovention.co.th/assets/images/logo.webp",
    image: "https://trippovention.co.th/assets/images/logo.webp",
    telephone: "+66-94-931-9572",
    email: "info@trippovention.co.th",
    address: {
      "@type": "PostalAddress",
      streetAddress: "Bangkok Office",
      addressLocality: "Bangkok",
      addressRegion: "Bangkok",
      postalCode: "10XXX",
      addressCountry: "TH",
    },
    geo: {
      "@type": "GeoCoordinates",
      latitude: "13.7563",
      longitude: "100.5018",
    },
    openingHours: "Mo-Sa 09:00-18:00",
    priceRange: "฿฿-฿฿฿",
    socialMedia: [
      "https://facebook.com/trippovention",
      "https://instagram.com/trippovention",
      "https://twitter.com/trippovention",
    ],
    // Global coverage with Thailand focus
    areaServed: [
      "TH",
      "SG",
      "MY",
      "VN",
      "ID",
      "PH",
      "KH",
      "MM",
      "LA",
      "IN",
      "AE",
      "JP",
      "KR",
      "CN",
      "HK",
      "AU",
      "NZ",
      "GB",
      "FR",
      "ES",
      "IT",
      "CH",
      "AT",
      "NL",
      "GR",
      "TR",
      "DE",
      "US",
      "CA",
    ],
  };

  // Contact point template (reusable)
  const getContactPoint = (areaServed = COMPANY_INFO.areaServed) => ({
    "@type": "ContactPoint",
    telephone: COMPANY_INFO.telephone,
    contactType: "Customer Service",
    areaServed: areaServed,
    availableLanguage: ["English", "Thai"],
    hoursAvailable: {
      "@type": "OpeningHoursSpecification",
      dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      opens: "09:00",
      closes: "18:00",
    },
  });

  // Full TravelAgency provider template
  const getTravelAgencyProvider = () => ({
    "@type": "TravelAgency",
    name: COMPANY_INFO.name,
    url: COMPANY_INFO.url,
    logo: COMPANY_INFO.logo,
    image: COMPANY_INFO.image,
    telephone: COMPANY_INFO.telephone,
    email: COMPANY_INFO.email,
    address: COMPANY_INFO.address,
    geo: COMPANY_INFO.geo,
    openingHours: COMPANY_INFO.openingHours,
    sameAs: COMPANY_INFO.socialMedia,
    contactPoint: getContactPoint(),
  });

  // Schema generators
  const schemas = {
    // 1. TravelAgency Schema (Homepage, Worldwide)
    travelAgency: (config) => ({
      "@context": "https://schema.org",
      "@type": "TravelAgency",
      name: COMPANY_INFO.name,
      description: config.description,
      url: config.url,
      logo: COMPANY_INFO.logo,
      image: COMPANY_INFO.image,
      telephone: COMPANY_INFO.telephone,
      email: COMPANY_INFO.email,
      address: COMPANY_INFO.address,
      geo: COMPANY_INFO.geo,
      openingHours: COMPANY_INFO.openingHours,
      priceRange: COMPANY_INFO.priceRange,
      sameAs: COMPANY_INFO.socialMedia,
      ...(config.aggregateRating && {
        aggregateRating: {
          "@type": "AggregateRating",
          ratingValue: config.aggregateRating.value,
          reviewCount: config.aggregateRating.count,
          bestRating: "5",
          worstRating: "1",
        },
      }),
      contactPoint: getContactPoint(),
    }),

    // 2. Organization Schema (Knowledge Graph)
    organization: () => ({
      "@context": "https://schema.org",
      "@type": "Organization",
      name: COMPANY_INFO.name,
      alternateName: "Trippovention Thailand Travel Agency",
      url: COMPANY_INFO.url,
      logo: COMPANY_INFO.logo,
      description:
        "Leading travel agency in Thailand specializing in Thailand & worldwide tours with 15+ years of experience",
      foundingDate: "2021",
      slogan: "Your Trusted Travel Partner in Thailand",
      address: COMPANY_INFO.address,
      contactPoint: {
        "@type": "ContactPoint",
        telephone: COMPANY_INFO.telephone,
        contactType: "Customer Service",
        email: COMPANY_INFO.email,
      },
      sameAs: COMPANY_INFO.socialMedia,
    }),

    // 3. WebSite with SearchAction (Sitelinks Search Box)
    website: (config) => ({
      "@context": "https://schema.org",
      "@type": "WebSite",
      name: COMPANY_INFO.name,
      url: COMPANY_INFO.url,
      potentialAction: {
        "@type": "SearchAction",
        target: `${COMPANY_INFO.url}/${config.searchPath || "search.html"}?q={search_term_string}`,
        "query-input": "required name=search_term_string",
      },
    }),

    // 4. Service Schema (Services, Visa)
    service: (config) => ({
      "@context": "https://schema.org",
      "@type": "Service",
      serviceType: config.serviceType,
      ...(config.name && {
        name: config.name,
      }),
      ...(config.description && {
        description: config.description,
      }),
      provider: getTravelAgencyProvider(),
      areaServed: COMPANY_INFO.areaServed,
      ...(config.aggregateRating && {
        aggregateRating: {
          "@type": "AggregateRating",
          ratingValue: config.aggregateRating.value,
          reviewCount: config.aggregateRating.count,
          bestRating: "5",
        },
      }),
      ...(config.offers && {
        offers: config.offers,
      }),
      ...(config.serviceOutput && {
        serviceOutput: config.serviceOutput,
      }),
      ...(config.hasOfferCatalog && {
        hasOfferCatalog: config.hasOfferCatalog,
      }),
    }),

    // 5. TouristTrip Schema (Package pages)
    touristTrip: (config) => ({
      "@context": "https://schema.org",
      "@type": config.schemaType || "TouristTrip",
      name: config.name,
      description: config.description,
      url: config.url,
      provider: getTravelAgencyProvider(),
      ...(config.aggregateRating && {
        aggregateRating: {
          "@type": "AggregateRating",
          ratingValue: config.aggregateRating.value,
          reviewCount: config.aggregateRating.count,
          bestRating: "5",
        },
      }),
      ...(config.duration && {
        duration: config.duration,
      }),
      touristType: config.touristType || ["Family", "Couples", "Solo Travelers", "Groups"],
      ...(config.itinerary && {
        itinerary: config.itinerary,
      }),
      ...(config.offers && {
        offers: config.offers,
      }),
    }),

    // 6. ContactPage Schema
    contactPage: (config) => ({
      "@context": "https://schema.org",
      "@type": "ContactPage",
      mainEntity: {
        "@type": "TravelAgency",
        name: COMPANY_INFO.name,
        url: COMPANY_INFO.url,
        logo: COMPANY_INFO.logo,
        telephone: config.multiplePhones || [COMPANY_INFO.telephone],
        email: COMPANY_INFO.email,
        address: COMPANY_INFO.address,
        geo: COMPANY_INFO.geo,
        openingHoursSpecification: {
          "@type": "OpeningHoursSpecification",
          dayOfWeek: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          opens: "09:00",
          closes: "18:00",
        },
        contactPoint: config.contactPoints || [
          {
            "@type": "ContactPoint",
            telephone: COMPANY_INFO.telephone,
            contactType: "Customer Service",
            areaServed: COMPANY_INFO.areaServed,
            availableLanguage: ["English", "Thai"],
          },
        ],
        sameAs: COMPANY_INFO.socialMedia,
      },
    }),

    // 7. BreadcrumbList Schema
    breadcrumb: (items) => ({
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      itemListElement: items.map((item, index) => ({
        "@type": "ListItem",
        position: index + 1,
        name: item.name,
        item: item.url,
      })),
    }),
  };

  // Inject schema into page
  const injectSchema = (schema, comment = null) => {
    const script = document.createElement("script");
    script.type = "application/ld+json";
    script.textContent = JSON.stringify(schema);

    // Add comment before script if provided
    if (comment) {
      const commentNode = document.createComment(` ${comment} `);
      document.body.appendChild(commentNode);
    }

    document.body.appendChild(script);
  };

  // Main initialization function
  const init = (config) => {
    // Always add breadcrumb if provided
    if (config.breadcrumb) {
      injectSchema(schemas.breadcrumb(config.breadcrumb), "Structured Data: BreadcrumbList");
    }

    // Add page-specific schemas
    switch (config.pageType) {
      case "homepage":
        injectSchema(
          schemas.travelAgency({
            description:
              config.description ||
              "Your trusted travel partner for unforgettable journeys across Thailand and the world",
            url: COMPANY_INFO.url,
            aggregateRating: {
              value: "4.8",
              count: "500",
            },
          }),
          "Structured Data: TravelAgency (Primary Business Entity)"
        );

        injectSchema(schemas.organization(), "Structured Data: Organization (Knowledge Graph)");
        injectSchema(schemas.website({}), "Structured Data: WebSite (Sitelinks Search Box)");
        break;

      case "worldwide":
        injectSchema(
          schemas.travelAgency({
            description:
              config.description ||
              "International travel packages for Thailand, Singapore, Malaysia, UAE, Vietnam, Europe and more",
            url: config.url,
          }),
          "Structured Data: TravelAgency"
        );
        break;

      case "services":
        injectSchema(
          schemas.service({
            serviceType: "Travel Services",
            aggregateRating: {
              value: "4.8",
              count: "500",
            },
            hasOfferCatalog: config.offerCatalog,
          }),
          "Structured Data: Service with OfferCatalog"
        );
        break;

      case "visa":
        injectSchema(
          schemas.service({
            serviceType: "Visa Assistance Services",
            name: "Visa Services by Trippovention Thailand",
            description: config.description,
            offers: config.offers,
            serviceOutput: config.serviceOutput,
          }),
          "Structured Data: Service (Visa Assistance)"
        );
        break;

      case "contact":
        injectSchema(
          schemas.contactPage({
            multiplePhones: config.phones,
            contactPoints: config.contactPoints,
          }),
          "Structured Data: ContactPage"
        );
        break;

      case "package":
        injectSchema(
          schemas.touristTrip({
            schemaType: config.schemaType || "TouristTrip",
            name: config.name,
            description: config.description,
            url: config.url,
            aggregateRating: config.aggregateRating,
            duration: config.duration,
            touristType: config.touristType,
            itinerary: config.itinerary,
            offers: config.offers,
          }),
          `Structured Data: ${config.schemaType || "TouristTrip"}`
        );
        break;

      default:
        // Only warn in development
        if (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1") {
          console.warn("StructuredData: Unknown page type:", config.pageType);
        }
    }
  };

  // Public API
  return {
    init,
    COMPANY_INFO, // Export for reference
    schemas, // Export for advanced usage
  };
})();

// Auto-initialize if config exists in window
if (typeof window !== "undefined" && window.structuredDataConfig) {
  document.addEventListener("DOMContentLoaded", () => {
    StructuredData.init(window.structuredDataConfig);
  });
}
