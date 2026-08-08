/**
 * WebMCP - AI Agent Integration for Trippovention Thailand (trippovention.co.th)
 * Standard: WebMCP API (https://webmachinelearning.github.io/webmcp/)
 */

(function () {
  'use strict';

  const LLMS_URL = 'https://trippovention.co.th/llms.txt';
  const SITE_URL = 'https://trippovention.co.th';

  const webMcpTools = [
    {
      name: 'search_travel_packages',
      description: 'Search Trippovention Thailand and international travel packages by destination or keyword',
      inputSchema: {
        type: 'object',
        properties: {
          query: {
            type: 'string',
            description: 'Destination name, activity, or keyword (e.g., "Bangkok", "Phuket", "Krabi", "Pattaya", "Buddha circuit")'
          },
          category: {
            type: 'string',
            enum: ['thailand', 'international', 'india'],
            description: 'Optional package category filter'
          }
        },
        required: ['query']
      },
      execute: async function (args) {
        const searchTerm = (args.query || '').toLowerCase();
        const results = [];

        const popularPackages = [
          { name: 'Bangkok Essentials Escape', destination: 'Bangkok', duration: '4 Days / 3 Nights', url: '/packages/thailand/bangkok/bangkok_essentials_escape.html' },
          { name: 'Phuket Beach Escape', destination: 'Phuket', duration: '5 Days / 4 Nights', url: '/packages/thailand/phuket/phuket_beach_escape.html' },
          { name: 'Krabi Family Adventure', destination: 'Krabi', duration: '5 Days / 4 Nights', url: '/packages/thailand/krabi/krabi_family_adventure.html' },
          { name: 'Pattaya Beach Escape', destination: 'Pattaya', duration: '4 Days / 3 Nights', url: '/packages/thailand/pattaya/pattaya_beach_escape.html' },
          { name: 'Ultimate Thailand Explorer', destination: 'Thailand', duration: 'Multi-city', url: '/packages/thailand/phuket/ultimate_thailand_explorer.html' },
          { name: 'Buddha Circuit Spiritual Adventure', destination: 'India', duration: '7 Days / 6 Nights', url: '/packages/india/buddha/buddha_circuit_spiritual_adventure.html' },
          { name: 'Golden Buddha Circuit Retreat', destination: 'India', duration: '7 Days / 6 Nights', url: '/packages/india/buddha/golden_buddha_circuit_retreat.html' }
        ];

        popularPackages.forEach(function (pkg) {
          if (pkg.name.toLowerCase().includes(searchTerm) || pkg.destination.toLowerCase().includes(searchTerm)) {
            results.push(pkg);
          }
        });

        if (results.length === 0) {
          return {
            status: 'success',
            message: 'For detailed listings of all travel packages matching "' + args.query + '", please consult ' + LLMS_URL,
            matches: popularPackages.slice(0, 3)
          };
        }

        return {
          status: 'success',
          count: results.length,
          packages: results
        };
      }
    },
    {
      name: 'get_package_details',
      description: 'Retrieve full itinerary details, inclusions, and overview for a specific Trippovention travel package',
      inputSchema: {
        type: 'object',
        properties: {
          packageName: {
            type: 'string',
            description: 'Name of the travel package or destination (e.g. "Bangkok", "Phuket", "Krabi")'
          }
        },
        required: ['packageName']
      },
      execute: async function (args) {
        return {
          status: 'success',
          packageName: args.packageName,
          provider: 'Trippovention Thailand',
          experience: '15+ Years Ground Operations Experience',
          contact: {
            phone: '+66-90-917-7601',
            email: 'query@trippovention.co.th',
            website: SITE_URL
          },
          documentation: 'Full package details and summaries available at ' + LLMS_URL
        };
      }
    },
    {
      name: 'get_visa_requirements',
      description: 'General visa and entry guidance; contact the team for document support',
      inputSchema: {
        type: 'object',
        properties: {
          country: {
            type: 'string',
            description: 'Destination country name (e.g., "Thailand", "Singapore", "Vietnam", "UK", "USA")'
          }
        },
        required: ['country']
      },
      execute: async function (args) {
        return {
          status: 'success',
          country: args.country,
          note: 'Visa assistance is handled via human consultation. See ' + LLMS_URL + ' and contact query@trippovention.co.th or +66-90-917-7601.',
          contactUrl: SITE_URL + '/contact.html'
        };
      }
    },
    {
      name: 'submit_travel_inquiry',
      description: 'Submit a custom travel inquiry or request expert callback for tailored holiday package planning',
      inputSchema: {
        type: 'object',
        properties: {
          name: { type: 'string', description: 'Traveler full name' },
          email: { type: 'string', description: 'Contact email address' },
          phone: { type: 'string', description: 'Contact phone / WhatsApp number' },
          destination: { type: 'string', description: 'Target destination or holiday preference' },
          travelers: { type: 'number', description: 'Number of travelers' },
          message: { type: 'string', description: 'Special requirements or travel dates' }
        },
        required: ['name', 'phone', 'destination']
      },
      execute: async function (args) {
        const nameInput = document.querySelector('input[name="name"], #name');
        const phoneInput = document.querySelector('input[name="phone"], input[name="tel"], #phone');
        const emailInput = document.querySelector('input[name="email"], #email');
        const msgInput = document.querySelector('textarea[name="message"], #message');

        if (nameInput) nameInput.value = args.name || '';
        if (phoneInput) phoneInput.value = args.phone || '';
        if (emailInput) emailInput.value = args.email || '';
        if (msgInput) msgInput.value = (args.destination ? 'Destination: ' + args.destination + '. ' : '') + (args.message || '');

        return {
          status: 'success',
          message: 'Inquiry details recorded. Complete submission at ' + SITE_URL + '/contact.html or call +66-90-917-7601.',
          inquiry: args
        };
      }
    }
  ];

  function registerWebMcp() {
    if (typeof navigator !== 'undefined' && navigator.modelContext && typeof navigator.modelContext.provideContext === 'function') {
      try {
        navigator.modelContext.provideContext({
          tools: webMcpTools
        });
        console.log('[WebMCP] Registered Trippovention Thailand WebMCP context provider.');
      } catch (err) {
        console.warn('[WebMCP] provideContext call error:', err);
      }
    }

    if (typeof window !== 'undefined') {
      window.webMCP = window.webMCP || {
        version: '1.0.0',
        tools: webMcpTools
      };
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', registerWebMcp);
  } else {
    registerWebMcp();
  }
})();
