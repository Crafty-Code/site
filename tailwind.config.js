module.exports = {
  darkMode: 'class',
  content: [
    './layouts/**/*.html',
    './themes/craftytheme/layouts/**/*.html',
    './layouts/partials/**/*.html',
    './content/**/*.md',
    './assets/**/*.js',
  ],
  safelist: [
    'dark:bg-gray-900',
    'dark:text-gray-100',
    'dark:border-gray-600',
    'dark:bg-gray-800',
    'dark:text-white',
    'dark:bg-black',
    'dark:text-gray-300',
    'dark:border-blue-900',
    'dark:text-blue-300',
    'dark:hover:text-blue-400',
    'dark:bg-blue-900',
    'dark:border-gray-700',
    'dark:prose-invert',
  ],
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
