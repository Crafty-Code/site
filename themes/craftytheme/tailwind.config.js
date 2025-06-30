module.exports = {
  darkMode: 'class',
  content: [
    './layouts/**/*.html',
    './themes/craftytheme/layouts/**/*.html',
    './layouts/partials/**/*.html',
    './content/**/*.md',
    './assets/**/*.js',
    './themes/craftytheme/layouts/**/*.html',
    './themes/craftytheme/layouts/partials/**/*.html',
    './themes/craftytheme/content/**/*.md',
    './themes/craftytheme/assets/**/*.js',
  ],
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
