/**
 * Trippovention Thailand - Internal Website Search Engine
 * Native In-Header Search Bar, Dropdown Suggestions & Results Page Controller
 */

(function () {
  'use strict';

  // --- Configuration & Constants ---
  const POPULAR_SEARCHES = [
    'Bangkok Pattaya Package',
    'Phuket',
    'Safari World',
    'Coral Island',
    'Phi Phi Island',
    'Dinner Cruise Bangkok',
    'Airport Transfer',
    'Krabi Sightseeing',
    'Chiang Mai'
  ];

  const TYPO_MAP = {
    'pukhet': 'phuket',
    'phukit': 'phuket',
    'phukett': 'phuket',
    'fuket': 'phuket',
    'bangkock': 'bangkok',
    'bangkog': 'bangkok',
    'bkkk': 'bangkok',
    'pataya': 'pattaya',
    'pattayah': 'pattaya',
    'patayya': 'pattaya',
    'kraby': 'krabi',
    'crabby': 'krabi',
    'chiangmai': 'chiang mai',
    'chaing mai': 'chiang mai',
    'chiangrai': 'chiang rai',
    'chaing rai': 'chiang rai',
    'samui': 'koh samui',
    'kosamui': 'koh samui',
    'kohsamui': 'koh samui',
    'kohlarn': 'koh larn',
    'phiphi': 'phi phi',
    'safariworld': 'safari world',
    'dinercruise': 'dinner cruise',
    'dinercruis': 'dinner cruise',
    'sightseing': 'sightseeing',
    'transfr': 'transfer',
    'transfar': 'transfer'
  };

  const SYNONYM_EXPANSIONS = {
    'bkk': ['bangkok', 'airport', 'suvarnabhumi'],
    'dmk': ['bangkok', 'airport', 'don mueang'],
    'hkt': ['phuket', 'airport'],
    'cnx': ['chiang mai', 'airport'],
    'cei': ['chiang rai', 'airport'],
    'kbv': ['krabi', 'airport'],
    'utp': ['pattaya', 'airport', 'utapao'],
    'usm': ['koh samui', 'airport'],
    'pickup': ['transfer', 'taxi', 'car'],
    'drop': ['transfer', 'taxi', 'car'],
    'cab': ['transfer', 'taxi', 'car'],
    'taxi': ['transfer', 'car', 'shuttle'],
    'shuttle': ['transfer', 'transport'],
    'transport': ['transfer'],
    'transportation': ['transfer'],
    'car': ['transfer'],
    'van': ['transfer', 'minivan'],
    'minivan': ['transfer'],
    'things to do': ['sightseeing', 'activities', 'tours'],
    'activities': ['sightseeing', 'tours', 'tickets'],
    'activity': ['sightseeing', 'tour'],
    'attractions': ['sightseeing', 'theme park', 'tickets'],
    'attraction': ['sightseeing', 'tickets'],
    'tickets': ['sightseeing', 'tour'],
    'island hopping': ['island', 'speedboat', 'tour', 'excursion'],
    'family trip': ['family', 'package', 'holiday'],
    'family holiday': ['family', 'package']
  };

  // --- Helper: Determine Root Relative Prefix ---
  function getRootPrefix() {
    // 1. Check current script src tag
    const scripts = document.querySelectorAll('script[src*="search.js"]');
    for (let s of scripts) {
      const src = s.getAttribute('src');
      const idx = src.indexOf('assets/');
      if (idx !== -1) {
        return src.substring(0, idx);
      }
    }

    // 2. Fallback based on pathname depth relative to root
    const path = window.location.pathname.replace(/^\/+/, '');
    const segments = path.split('/').filter(Boolean);
    if (segments.length <= 1) return '';
    return '../'.repeat(segments.length - 1);
  }

  const ROOT_PREFIX = getRootPrefix();

  // Ensure search.css is loaded
  function ensureSearchCSS() {
    if (!document.querySelector('link[href*="search.css"]')) {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = ROOT_PREFIX + 'assets/search.css';
      document.head.appendChild(link);
    }
  }

  // --- Search Engine State ---
  let searchData = null;
  let isLoadingData = false;
  let activeCategory = 'all';
  let activeSelectedIndex = -1;
  let searchDebounceTimer = null;

  // --- Load Search Data ---
  function loadSearchData(callback) {
    if (searchData && searchData.length) {
      if (callback) callback(searchData);
      return;
    }

    // Check if globally loaded via search-data.js
    if (window.TRIPPOVENTION_SEARCH_DATA && Array.isArray(window.TRIPPOVENTION_SEARCH_DATA)) {
      searchData = window.TRIPPOVENTION_SEARCH_DATA;
      if (callback) callback(searchData);
      return;
    }

    if (isLoadingData) {
      setTimeout(() => loadSearchData(callback), 80);
      return;
    }

    isLoadingData = true;

    // Try fetching JSON first
    const jsonPath = ROOT_PREFIX + 'assets/search-index.json';
    fetch(jsonPath)
      .then(res => {
        if (!res.ok) throw new Error('Network response not ok: ' + res.status);
        return res.json();
      })
      .then(data => {
        searchData = data;
        isLoadingData = false;
        if (callback) callback(searchData);
      })
      .catch(() => {
        // Fallback: dynamically load search-data.js
        const script = document.createElement('script');
        script.src = ROOT_PREFIX + 'assets/search-data.js';
        script.onload = () => {
          isLoadingData = false;
          if (window.TRIPPOVENTION_SEARCH_DATA) {
            searchData = window.TRIPPOVENTION_SEARCH_DATA;
          } else {
            searchData = [];
          }
          if (callback) callback(searchData);
        };
        script.onerror = () => {
          isLoadingData = false;
          searchData = [];
          if (callback) callback(searchData);
        };
        document.head.appendChild(script);
      });
  }

  // --- Intelligent Keyword Matching Engine ---
  function cleanString(str) {
    return (str || '')
      .toLowerCase()
      .replace(/[^\w\s-]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function getTokens(query) {
    const cleaned = cleanString(query);
    const rawTokens = cleaned.split(' ').filter(Boolean);
    const tokens = [];

    rawTokens.forEach(t => {
      // Correct typo if present
      const corrected = TYPO_MAP[t] || t;
      tokens.push(corrected);

      // Add synonyms
      if (SYNONYM_EXPANSIONS[corrected]) {
        SYNONYM_EXPANSIONS[corrected].forEach(syn => {
          if (!tokens.includes(syn)) tokens.push(syn);
        });
      }
    });

    // Check multi-word phrase replacements
    for (let phrase in SYNONYM_EXPANSIONS) {
      if (phrase.includes(' ') && cleaned.includes(phrase)) {
        SYNONYM_EXPANSIONS[phrase].forEach(syn => {
          if (!tokens.includes(syn)) tokens.push(syn);
        });
      }
    }

    return { rawTokens, allTokens: Array.from(new Set(tokens)) };
  }

  function scoreItem(item, rawQuery, tokens) {
    const raw = cleanString(rawQuery);
    if (!raw) return 0;

    const titleLower = (item.title || '').toLowerCase();
    const destLower = (item.destination || '').toLowerCase();
    const catLower = (item.category || '').toLowerCase();
    const descLower = (item.description || '').toLowerCase();
    const keywords = Array.isArray(item.keywords) ? item.keywords.map(k => String(k).toLowerCase()) : [];

    let score = 0;

    // Category Filter check
    if (activeCategory && activeCategory !== 'all') {
      const itemCat = (item.category || '').toLowerCase();
      const targetCat = activeCategory.toLowerCase();
      if (!itemCat.includes(targetCat)) {
        return 0; // Filter out if not in selected tab
      }
    }

    // 1. Exact / Full Phrase Matches
    if (titleLower === raw) {
      score += 150;
    } else if (titleLower.startsWith(raw)) {
      score += 90;
    } else if (titleLower.includes(raw)) {
      score += 65;
    }

    if (destLower === raw) {
      score += 70;
    }

    // 2. Token Matching
    let matchedTokenCount = 0;
    const { rawTokens, allTokens } = tokens;

    allTokens.forEach(tok => {
      let tokenFound = false;

      // Title matches
      if (titleLower.includes(tok)) {
        score += 30;
        tokenFound = true;
      }
      // Destination matches
      if (destLower.includes(tok)) {
        score += 25;
        tokenFound = true;
      }
      // Category / Badge matches
      if (catLower.includes(tok) || (item.badge && item.badge.toLowerCase().includes(tok))) {
        score += 20;
        tokenFound = true;
      }
      // Keyword matches
      if (keywords.some(k => k.includes(tok))) {
        score += 18;
        tokenFound = true;
      }
      // Description matches
      if (descLower.includes(tok)) {
        score += 10;
        tokenFound = true;
      }

      if (tokenFound) matchedTokenCount++;
    });

    // 3. Multi-token completeness bonus
    // If every raw token typed by customer matches something in the item:
    const allRawMatched = rawTokens.every(tok => {
      const corrected = TYPO_MAP[tok] || tok;
      return (
        titleLower.includes(corrected) ||
        destLower.includes(corrected) ||
        descLower.includes(corrected) ||
        keywords.some(k => k.includes(corrected)) ||
        (SYNONYM_EXPANSIONS[corrected] && SYNONYM_EXPANSIONS[corrected].some(syn => 
          titleLower.includes(syn) || destLower.includes(syn) || descLower.includes(syn) || keywords.some(k => k.includes(syn))
        ))
      );
    });

    if (allRawMatched && rawTokens.length > 1) {
      score += 45 * rawTokens.length;
    }

    // Transfer route specific boost: "bkk to pattaya", "bangkok to pattaya", "phuket airport to krabi"
    if (raw.includes(' to ') || (rawTokens.includes('airport') && rawTokens.includes('transfer'))) {
      if (item.category === 'Transfer') score += 40;
    }

    // Island hopping boost
    if (raw.includes('island hopping') || raw.includes('island hop')) {
      if (titleLower.includes('island') || descLower.includes('island')) score += 35;
    }

    // Dinner cruise boost
    if (raw.includes('dinner cruise') || raw.includes('cruise')) {
      if (titleLower.includes('cruise') || descLower.includes('cruise')) score += 40;
    }

    return score;
  }

  function executeSearch(query, category) {
    if (!searchData || !searchData.length) return [];
    const trimmed = (query || '').trim();
    if (!trimmed) return [];

    activeCategory = category || activeCategory || 'all';
    const tokens = getTokens(trimmed);

    const scoredItems = [];
    for (let i = 0; i < searchData.length; i++) {
      const item = searchData[i];
      const score = scoreItem(item, trimmed, tokens);
      if (score > 12) {
        scoredItems.push({ item, score });
      }
    }

    // Sort descending by score
    scoredItems.sort((a, b) => b.score - a.score);
    return scoredItems.map(s => s.item);
  }

  // --- Highlight Matching Terms in Text ---
  function highlightMatches(text, query) {
    if (!text || !query) return escapeHtml(text || '');
    const tokens = cleanString(query).split(' ').filter(t => t.length > 1);
    if (!tokens.length) return escapeHtml(text);

    // Escape regex chars
    const pattern = tokens.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|');
    const regex = new RegExp(`(${pattern})`, 'gi');

    const escaped = escapeHtml(text);
    return escaped.replace(regex, '<mark>$1</mark>');
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // --- Dynamic Mounting into Website Header ---
  function mountHeaderSearch() {
    const navRight = document.querySelector('.nav .container .nav-right');
    if (!navRight) return;

    if (document.getElementById('headerSearchWrap')) return; // Already mounted

    // 1. Create .header-search-wrap
    const wrap = document.createElement('div');
    wrap.className = 'header-search-wrap';
    wrap.id = 'headerSearchWrap';

    wrap.innerHTML = `
      <div class="header-search-bar" id="headerSearchBar" role="search">
        <div class="header-search-input-box">
          <svg class="header-search-icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" class="header-search-input" id="headerSearchInput" placeholder="Search destinations, packages, transfers..." autocomplete="off" spellcheck="false" aria-label="Search website content" aria-expanded="false" aria-haspopup="listbox" role="combobox" />
          <span class="header-search-kbd">⌘K</span>
          <button type="button" class="header-search-clear" id="headerSearchClear" aria-label="Clear search input">✕</button>
        </div>
      </div>
      <button type="button" class="header-search-toggle" id="headerSearchToggle" aria-label="Open search" title="Search Trippovention">
        <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
      </button>
    `;

    // Insert right before .actions
    const actions = navRight.querySelector('.actions');
    if (actions) {
      navRight.insertBefore(wrap, actions);
    } else {
      navRight.prepend(wrap);
    }

    // 2. Create Modal Overlay and Dropdown Container
    let overlay = document.getElementById('searchOverlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'header-search-dropdown-overlay';
      overlay.id = 'searchOverlay';
      overlay.setAttribute('aria-hidden', 'true');

      overlay.innerHTML = `
        <div class="header-search-backdrop" id="searchBackdrop"></div>
        <div class="header-search-dropdown" id="searchDropdown" role="dialog" aria-modal="true" aria-label="Search Trippovention">
          <div class="header-search-mobile-bar">
            <div class="header-search-input-box">
              <svg class="header-search-icon" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              <input type="text" class="header-search-input" id="mobileSearchInput" placeholder="Search destinations, packages, transfers..." autocomplete="off" spellcheck="false" />
              <button type="button" class="header-search-clear" id="mobileSearchClear" aria-label="Clear">✕</button>
            </div>
            <button type="button" class="header-search-mobile-close" id="mobileSearchClose">Cancel</button>
          </div>

          <div class="header-search-filters" id="searchDropdownFilters" role="tablist">
            <button type="button" class="search-filter-tab active" data-category="all" role="tab" aria-selected="true">All</button>
            <button type="button" class="search-filter-tab" data-category="Package" role="tab" aria-selected="false">Packages</button>
            <button type="button" class="search-filter-tab" data-category="Sightseeing" role="tab" aria-selected="false">Sightseeing</button>
            <button type="button" class="search-filter-tab" data-category="Transfer" role="tab" aria-selected="false">Transfers</button>
            <button type="button" class="search-filter-tab" data-category="Day Trip" role="tab" aria-selected="false">Day Trips</button>
            <button type="button" class="search-filter-tab" data-category="Destination" role="tab" aria-selected="false">Destinations</button>
          </div>

          <div class="header-search-body" id="searchResultsBody"></div>

          <div class="header-search-footer" id="searchFooter">
            <a href="#" class="search-view-all-link" id="searchViewAll">View all results →</a>
            <span class="search-footer-hint">Press Esc to close • ↑↓ to navigate</span>
          </div>
        </div>
      `;

      document.body.appendChild(overlay);
    }

    bindSearchEvents();
  }

  // --- Bind Event Listeners ---
  function bindSearchEvents() {
    const desktopInput = document.getElementById('headerSearchInput');
    const mobileInput = document.getElementById('mobileSearchInput');
    const desktopClear = document.getElementById('headerSearchClear');
    const mobileClear = document.getElementById('mobileSearchClear');
    const mobileToggle = document.getElementById('headerSearchToggle');
    const mobileClose = document.getElementById('mobileSearchClose');
    const backdrop = document.getElementById('searchBackdrop');
    const overlay = document.getElementById('searchOverlay');
    const viewAllLink = document.getElementById('searchViewAll');
    const filterTabs = document.querySelectorAll('#searchDropdownFilters .search-filter-tab');

    // Preload data on initial interaction / idle
    const triggerDataLoad = () => loadSearchData();
    if ('requestIdleCallback' in window) {
      window.requestIdleCallback(triggerDataLoad);
    } else {
      setTimeout(triggerDataLoad, 500);
    }

    function openSearch(fromMobile = false) {
      overlay.classList.add('active');
      overlay.setAttribute('aria-hidden', 'false');
      document.body.classList.add('search-open');
      if (fromMobile || window.innerWidth < 992) {
        document.body.style.overflow = 'hidden';
      }

      // Load search data immediately
      loadSearchData();

      if (fromMobile || window.innerWidth < 992) {
        if (mobileInput) {
          mobileInput.value = desktopInput ? desktopInput.value : '';
          mobileInput.focus();
        }
      } else {
        if (desktopInput) {
          desktopInput.focus();
          desktopInput.setAttribute('aria-expanded', 'true');
        }
      }

      renderDropdownContent(getCurrentQuery());
    }

    function closeSearch() {
      overlay.classList.remove('active');
      overlay.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('search-open');
      document.body.style.overflow = '';
      if (desktopInput) desktopInput.setAttribute('aria-expanded', 'false');
      activeSelectedIndex = -1;
    }

    function getCurrentQuery() {
      const isMobileVisible = window.innerWidth < 992;
      if (isMobileVisible && mobileInput) return mobileInput.value.trim();
      return desktopInput ? desktopInput.value.trim() : '';
    }

    function syncInputValues(val) {
      if (desktopInput && desktopInput.value !== val) desktopInput.value = val;
      if (mobileInput && mobileInput.value !== val) mobileInput.value = val;
      toggleClearButtons(val);
    }

    function toggleClearButtons(val) {
      const show = !!val;
      if (desktopClear) desktopClear.style.display = show ? 'inline-block' : 'none';
      if (mobileClear) mobileClear.style.display = show ? 'inline-block' : 'none';
    }

    // Handle Input Typing with Debounce
    function handleQueryInput(val) {
      syncInputValues(val);
      clearTimeout(searchDebounceTimer);
      searchDebounceTimer = setTimeout(() => {
        renderDropdownContent(val);
      }, 150);
    }

    if (desktopInput) {
      desktopInput.addEventListener('focus', () => openSearch(false));
      desktopInput.addEventListener('input', (e) => handleQueryInput(e.target.value));
      desktopInput.addEventListener('keydown', handleKeyNavigation);
    }

    if (mobileInput) {
      mobileInput.addEventListener('input', (e) => handleQueryInput(e.target.value));
      mobileInput.addEventListener('keydown', handleKeyNavigation);
    }

    if (mobileToggle) {
      mobileToggle.addEventListener('click', (e) => {
        e.preventDefault();
        openSearch(true);
      });
    }

    if (mobileClose) {
      mobileClose.addEventListener('click', closeSearch);
    }

    if (backdrop) {
      backdrop.addEventListener('click', closeSearch);
    }

    if (desktopClear) {
      desktopClear.addEventListener('click', () => {
        syncInputValues('');
        if (desktopInput) desktopInput.focus();
        renderDropdownContent('');
      });
    }

    if (mobileClear) {
      mobileClear.addEventListener('click', () => {
        syncInputValues('');
        if (mobileInput) mobileInput.focus();
        renderDropdownContent('');
      });
    }

    // Category Filter tabs in dropdown
    filterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        filterTabs.forEach(t => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');
        activeCategory = tab.dataset.category || 'all';
        renderDropdownContent(getCurrentQuery());
      });
    });

    // View All Results Link
    if (viewAllLink) {
      viewAllLink.addEventListener('click', (e) => {
        e.preventDefault();
        const q = getCurrentQuery();
        if (q) {
          window.location.href = ROOT_PREFIX + `search.html?q=${encodeURIComponent(q)}&category=${encodeURIComponent(activeCategory)}`;
        } else {
          window.location.href = ROOT_PREFIX + 'search.html';
        }
      });
    }

    // Global Hotkeys: Command+K / Ctrl+K and Escape
    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        openSearch(false);
      } else if (e.key === 'Escape' && overlay.classList.contains('active')) {
        e.preventDefault();
        closeSearch();
      }
    });

    // Close on navigation click inside results
    const resultsBody = document.getElementById('searchResultsBody');
    if (resultsBody) {
      resultsBody.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (link) {
          closeSearch();
        }
      });
    }
  }

  // --- Keyboard Navigation in Results ---
  function handleKeyNavigation(e) {
    const resultsContainer = document.getElementById('searchResultsBody');
    if (!resultsContainer) return;

    const items = resultsContainer.querySelectorAll('.search-result-item');
    if (!items.length) {
      if (e.key === 'Enter') {
        e.preventDefault();
        const q = e.target.value.trim();
        if (q) {
          window.location.href = ROOT_PREFIX + `search.html?q=${encodeURIComponent(q)}&category=${encodeURIComponent(activeCategory)}`;
        }
      }
      return;
    }

    if (e.key === 'ArrowDown') {
      e.preventDefault();
      activeSelectedIndex = (activeSelectedIndex + 1) % items.length;
      updateSelectedResultItem(items);
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      activeSelectedIndex = (activeSelectedIndex - 1 + items.length) % items.length;
      updateSelectedResultItem(items);
    } else if (e.key === 'Enter') {
      e.preventDefault();
      if (activeSelectedIndex >= 0 && items[activeSelectedIndex]) {
        items[activeSelectedIndex].click();
      } else {
        const q = e.target.value.trim();
        if (q) {
          window.location.href = ROOT_PREFIX + `search.html?q=${encodeURIComponent(q)}&category=${encodeURIComponent(activeCategory)}`;
        }
      }
    }
  }

  function updateSelectedResultItem(items) {
    items.forEach((item, idx) => {
      if (idx === activeSelectedIndex) {
        item.classList.add('selected');
        item.scrollIntoView({ block: 'nearest' });
      } else {
        item.classList.remove('selected');
      }
    });
  }

  // --- Render Dropdown Content ---
  function renderDropdownContent(query) {
    const body = document.getElementById('searchResultsBody');
    const footer = document.getElementById('searchFooter');
    const viewAllLink = document.getElementById('searchViewAll');
    if (!body) return;

    activeSelectedIndex = -1;
    const trimmed = (query || '').trim();

    // 1. Empty State: Show Popular Searches
    if (!trimmed) {
      body.innerHTML = `
        <div class="search-suggestions-section">
          <div class="search-suggestions-title">Popular Searches</div>
          <div class="search-tags-grid">
            ${POPULAR_SEARCHES.map(tag => `
              <button type="button" class="search-tag-chip" data-search="${escapeHtml(tag)}">
                <span>🔍</span> ${escapeHtml(tag)}
              </button>
            `).join('')}
          </div>
        </div>
      `;

      if (footer) footer.style.display = 'none';

      // Bind popular tag chips
      body.querySelectorAll('.search-tag-chip').forEach(btn => {
        btn.addEventListener('click', () => {
          const text = btn.dataset.search;
          const desktopInput = document.getElementById('headerSearchInput');
          const mobileInput = document.getElementById('mobileSearchInput');
          if (desktopInput) desktopInput.value = text;
          if (mobileInput) mobileInput.value = text;
          const desktopClear = document.getElementById('headerSearchClear');
          const mobileClear = document.getElementById('mobileSearchClear');
          if (desktopClear) desktopClear.style.display = 'inline-block';
          if (mobileClear) mobileClear.style.display = 'inline-block';
          renderDropdownContent(text);
        });
      });
      return;
    }

    // 2. Perform Search
    loadSearchData(data => {
      const results = executeSearch(trimmed, activeCategory);

      if (!results.length) {
        body.innerHTML = `
          <div class="header-search-no-results">
            <div class="no-res-icon">🔍</div>
            <h4>No matches found for "${escapeHtml(trimmed)}"</h4>
            <p>Try checking spelling, using fewer keywords, or searching by destination (e.g. "Phuket", "Bangkok", "Krabi").</p>
          </div>
        `;
        if (footer) footer.style.display = 'none';
        return;
      }

      // Display top 8 results in dropdown
      const displayResults = results.slice(0, 8);

      body.innerHTML = `
        <div class="header-search-results" role="listbox">
          ${displayResults.map(item => renderDropdownItemHTML(item, trimmed)).join('')}
        </div>
      `;

      if (footer) {
        footer.style.display = 'flex';
        if (viewAllLink) {
          viewAllLink.textContent = `View all ${results.length} results →`;
          viewAllLink.href = ROOT_PREFIX + `search.html?q=${encodeURIComponent(trimmed)}&category=${encodeURIComponent(activeCategory)}`;
        }
      }
    });
  }

  function renderDropdownItemHTML(item, query) {
    const itemUrl = ROOT_PREFIX + item.url;
    const itemImg = item.image ? ROOT_PREFIX + item.image : ROOT_PREFIX + 'assets/images/logo.webp';
    const highlightedTitle = highlightMatches(item.title, query);
    const highlightedDesc = highlightMatches(item.description, query);
    const badge = item.badge || item.category || 'Travel';
    const dest = item.destination || '';
    const priceText = item.price ? (item.price.includes('Contact') ? 'Contact For Rates' : item.price) : '';

    return `
      <a href="${itemUrl}" class="search-result-item" role="option">
        <img src="${itemImg}" alt="${escapeHtml(item.title)}" class="search-item-thumb" loading="lazy" onerror="this.onerror=null;this.src='${ROOT_PREFIX}assets/images/logo.webp';this.style.objectFit='contain';" />
        <div class="search-item-info">
          <div class="search-item-header">
            <span class="search-item-badge">${escapeHtml(badge)}</span>
            ${dest ? `<span class="search-item-dest">• ${escapeHtml(dest)}</span>` : ''}
          </div>
          <div class="search-item-title">${highlightedTitle}</div>
          <div class="search-item-desc">${highlightedDesc}</div>
        </div>
        ${priceText ? `<div class="search-item-price">${escapeHtml(priceText)}</div>` : ''}
      </a>
    `;
  }

  // --- Search Results Page Controller (search.html) ---
  function initSearchResultsPage() {
    const pageContainer = document.getElementById('searchResultsPage');
    if (!pageContainer) return;

    const urlParams = new URLSearchParams(window.location.search);
    const initialQuery = urlParams.get('q') || '';
    const initialCat = urlParams.get('category') || 'all';

    const heroInput = document.getElementById('searchPageHeroInput');
    const heroBtn = document.getElementById('searchPageHeroBtn');
    const resultsCountEl = document.getElementById('searchPageResultsCount');
    const resultsGrid = document.getElementById('searchPageGrid');
    const loadMoreBtn = document.getElementById('searchPageLoadMore');
    const sortSelect = document.getElementById('searchPageSort');
    const pills = document.querySelectorAll('.search-page-pills .search-page-pill');

    let pageCurrentQuery = initialQuery;
    let pageCurrentCategory = initialCat;
    let pageCurrentSort = 'relevance';
    let visibleCount = 12;
    let fullResults = [];

    if (heroInput) heroInput.value = initialQuery;

    // Set active category pill
    pills.forEach(pill => {
      if (pill.dataset.category.toLowerCase() === initialCat.toLowerCase()) {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
      }
      pill.addEventListener('click', () => {
        pills.forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        pageCurrentCategory = pill.dataset.category || 'all';
        visibleCount = 12;
        updateSearchResults();
      });
    });

    if (sortSelect) {
      sortSelect.addEventListener('change', () => {
        pageCurrentSort = sortSelect.value;
        visibleCount = 12;
        updateSearchResults();
      });
    }

    if (heroBtn && heroInput) {
      heroBtn.addEventListener('click', () => {
        executePageSearch(heroInput.value.trim());
      });
      heroInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          executePageSearch(heroInput.value.trim());
        }
      });
    }

    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', () => {
        visibleCount += 12;
        renderPageResults();
      });
    }

    function executePageSearch(query) {
      pageCurrentQuery = query;
      visibleCount = 12;
      const newUrl = new URL(window.location.href);
      if (query) {
        newUrl.searchParams.set('q', query);
      } else {
        newUrl.searchParams.delete('q');
      }
      if (pageCurrentCategory && pageCurrentCategory !== 'all') {
        newUrl.searchParams.set('category', pageCurrentCategory);
      } else {
        newUrl.searchParams.delete('category');
      }
      window.history.pushState({}, '', newUrl);
      updateSearchResults();
    }

    function updateSearchResults() {
      loadSearchData(() => {
        if (!pageCurrentQuery) {
          // If no query, show all products in active category
          let items = searchData.slice();
          if (pageCurrentCategory !== 'all') {
            const targetCat = pageCurrentCategory.toLowerCase();
            items = items.filter(it => (it.category || '').toLowerCase().includes(targetCat));
          }
          fullResults = items;
        } else {
          fullResults = executeSearch(pageCurrentQuery, pageCurrentCategory);
        }

        // Apply Sorting
        if (pageCurrentSort === 'title-asc') {
          fullResults.sort((a, b) => (a.title || '').localeCompare(b.title || ''));
        } else if (pageCurrentSort === 'title-desc') {
          fullResults.sort((a, b) => (b.title || '').localeCompare(a.title || ''));
        }

        renderPageResults();
      });
    }

    function renderPageResults() {
      if (resultsCountEl) {
        if (pageCurrentQuery) {
          resultsCountEl.innerHTML = `Showing <strong>${fullResults.length}</strong> results for "<strong>${escapeHtml(pageCurrentQuery)}</strong>"`;
        } else {
          resultsCountEl.innerHTML = `Showing <strong>${fullResults.length}</strong> available travel options`;
        }
      }

      if (!resultsGrid) return;

      if (!fullResults.length) {
        resultsGrid.innerHTML = `
          <div class="search-page-no-results">
            <div class="no-res-icon">🔍</div>
            <h3>No results found</h3>
            <p>We couldn't find anything matching "<strong>${escapeHtml(pageCurrentQuery)}</strong>".</p>
            <div class="no-res-suggestions">
              <p>Try searching for popular destinations or categories:</p>
              <div class="search-tags-grid" style="justify-content:center; margin-top:12px;">
                ${POPULAR_SEARCHES.map(s => `<button type="button" class="search-tag-chip search-page-quick-tag" data-q="${escapeHtml(s)}">${escapeHtml(s)}</button>`).join('')}
              </div>
            </div>
          </div>
        `;

        resultsGrid.querySelectorAll('.search-page-quick-tag').forEach(tagBtn => {
          tagBtn.addEventListener('click', () => {
            const val = tagBtn.dataset.q;
            if (heroInput) heroInput.value = val;
            executePageSearch(val);
          });
        });

        if (loadMoreBtn) loadMoreBtn.style.display = 'none';
        return;
      }

      const visibleItems = fullResults.slice(0, visibleCount);
      resultsGrid.innerHTML = visibleItems.map(item => renderPageCardHTML(item, pageCurrentQuery)).join('');

      if (loadMoreBtn) {
        loadMoreBtn.style.display = fullResults.length > visibleCount ? 'inline-block' : 'none';
      }
    }

    function renderPageCardHTML(item, query) {
      const itemUrl = ROOT_PREFIX + item.url;
      const itemImg = item.image ? ROOT_PREFIX + item.image : ROOT_PREFIX + 'assets/images/logo.webp';
      const highlightedTitle = highlightMatches(item.title, query);
      const highlightedDesc = highlightMatches(item.description, query);
      const badge = item.badge || item.category || 'Travel';
      const dest = item.destination || 'Thailand';
      const priceText = item.price || 'Best Rate Guaranteed';

      return `
        <div class="card search-product-card">
          <div class="img-wrap">
            <img src="${itemImg}" alt="${escapeHtml(item.title)}" loading="lazy" onerror="this.onerror=null;this.src='${ROOT_PREFIX}assets/images/logo.webp';this.style.objectFit='contain';" />
            <span class="badge" style="position: absolute; top: 12px; left: 12px; z-index: 2; box-shadow: 0 2px 6px rgba(0,0,0,0.2);">${escapeHtml(badge)}</span>
          </div>
          <div class="body">
            <div class="font-weight-600" style="font-size: 13px; color: var(--orange); text-transform: uppercase; margin-bottom: 4px;">📍 ${escapeHtml(dest)}</div>
            <h3><a href="${itemUrl}" style="color: inherit; text-decoration: none;">${highlightedTitle}</a></h3>
            <p>${highlightedDesc}</p>
            <div class="price-row" style="margin-top: auto; padding-top: 10px; display: flex; align-items: baseline; justify-content: space-between;">
              <span class="price font-weight-700" style="color: var(--emerald, #10b981); font-size: 15px;">${escapeHtml(priceText)}</span>
            </div>
            <a href="${itemUrl}" class="btn" style="margin-top: 12px;">View Details →</a>
          </div>
        </div>
      `;
    }

    // Initial Trigger
    updateSearchResults();
  }

  // --- Auto-Initialization ---
  function init() {
    ensureSearchCSS();
    mountHeaderSearch();
    initSearchResultsPage();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
