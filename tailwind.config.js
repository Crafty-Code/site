module.exports = {
  darkMode: 'class',
  content: [
    './layouts/**/*.html',
    './themes/craftytheme/layouts/**/*.html',
    './content/**/*.md',
    './assets/**/*.js',
  ],
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
