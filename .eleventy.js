module.exports = function(eleventyConfig) {
  // Copy assets folder as-is
  eleventyConfig.addPassthroughCopy("src/assets");
  
  // Copy other static files
  eleventyConfig.addPassthroughCopy("src/robots.txt");
  eleventyConfig.addPassthroughCopy("src/site.webmanifest");
  eleventyConfig.addPassthroughCopy("src/sitemap.xml");
  eleventyConfig.addPassthroughCopy("src/image-sitemap.xml");
  eleventyConfig.addPassthroughCopy("src/sw.js");
  eleventyConfig.addPassthroughCopy("src/CNAME");
  eleventyConfig.addPassthroughCopy("src/_headers");
  
  // Copy package HTML files as-is (they contain structured data that shouldn't be processed)
  eleventyConfig.addPassthroughCopy("src/packages/singapore/*.html");
  eleventyConfig.addPassthroughCopy("src/packages/india/*.html");
  eleventyConfig.addPassthroughCopy("src/packages/thailand/*.html");
  
  // Watch for changes in assets
  eleventyConfig.addWatchTarget("src/assets/");
  
  // Add date filter for templates
  eleventyConfig.addFilter("dateFormat", function(date) {
    return new Date(date).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });
  });
  
  // Add a filter to get asset path based on depth
  eleventyConfig.addFilter("assetPath", function(depth) {
    if (depth === 0) return "";
    return "../".repeat(depth);
  });

  // Set input/output directories
  return {
    dir: {
      input: "src",
      output: "docs",
      includes: "_includes",
      data: "_data"
    },
    templateFormats: ["njk", "html", "md"],
    htmlTemplateEngine: "njk",
    markdownTemplateEngine: "njk"
  };
};

