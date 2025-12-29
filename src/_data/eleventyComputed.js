module.exports = {
  // Get asset path based on page depth
  assetPath: (data) => {
    const url = data.page.url || '/';
    const depth = (url.match(/\//g) || []).length - 1;
    if (depth <= 0) return '';
    return '../'.repeat(depth);
  },
  
  // Get current year for footer copyright
  currentYear: () => new Date().getFullYear()
};

