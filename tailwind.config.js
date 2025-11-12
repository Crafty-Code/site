module.exports = {
  darkMode: 'media',
  content: [
    './layouts/**/*.html',
    './themes/craftytheme/layouts/**/*.html',
    './layouts/partials/**/*.html',
    './content/**/*.md',
    './assets/**/*.js',
  ],
  safelist: [
    // Ensure all possible theme colors are included in the build
    // Primary colors
    {
      pattern: /(bg|text|border)-(blue|green|purple|red|yellow|indigo|pink|teal|gray|emerald|violet|rose|orange|cyan|sky|lime|fuchsia|slate|zinc|neutral|stone)-(50|100|200|300|400|500|600|700|800|900)/,
      variants: ['dark', 'hover', 'focus']
    },
    // Common theme color combinations
    'bg-gray-800', 'bg-gray-900', 'bg-white', 'bg-gray-50',
    'dark:bg-gray-900', 'dark:bg-gray-800', 'dark:bg-gray-700',
    'text-white', 'text-gray-100', 'text-gray-200', 'text-gray-300', 'text-gray-900',
    'dark:text-gray-100', 'dark:text-gray-200', 'dark:text-gray-300', 'dark:text-white',
    'border-gray-600', 'border-gray-700', 'border-gray-200', 'border-gray-300',
    'dark:border-gray-600', 'dark:border-gray-700',
    'hover:text-blue-400', 'dark:hover:text-blue-400',
    'hover:text-green-400', 'dark:hover:text-green-400',
    'hover:text-purple-400', 'dark:hover:text-purple-400',
    'hover:text-red-400', 'dark:hover:text-red-400',
    'hover:bg-blue-700', 'hover:bg-blue-600', 'dark:hover:bg-blue-600', 'dark:hover:bg-blue-700',
    // Button classes
    'bg-blue-600', 'bg-blue-700', 'dark:bg-blue-700', 'dark:bg-blue-600',
    'bg-green-600', 'bg-green-700', 'dark:bg-green-700', 'dark:bg-green-600',
    'bg-purple-600', 'bg-purple-700', 'dark:bg-purple-700', 'dark:bg-purple-600',
    // Form classes
    'focus:border-blue-500', 'focus:border-blue-400', 'dark:focus:border-blue-400', 'dark:focus:border-blue-500',
    // Code syntax colors
    'bg-gray-50', 'bg-gray-900', 'dark:bg-gray-900', 'dark:bg-gray-50'
  ],
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
