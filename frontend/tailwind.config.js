/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Geist', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['"Geist Mono"', 'JetBrains Mono', 'monospace'],
      },
      colors: {
        police: {
          50: '#F0F5FA',
          100: '#E2EBF5',
          200: '#C5D7EB',
          300: '#99BCE0',
          400: '#649BD0',
          500: '#3D7CBD',
          600: '#2A619F',
          700: '#224D80',
          800: '#1B3F68',
          900: '#0F233A',
          950: '#081321'
        },
        accent: {
          DEFAULT: '#2563EB',
          hover: '#1D4ED8',
          muted: '#3B82F6',
          subtle: 'rgba(37, 99, 235, 0.08)'
        }
      },
      boxShadow: {
        'glass': 'inset 0 1px 0 rgba(255, 255, 255, 0.08), 0 4px 20px -2px rgba(0, 0, 0, 0.3)',
        'glass-hover': 'inset 0 1px 0 rgba(255, 255, 255, 0.15), 0 8px 30px -4px rgba(0, 0, 0, 0.4)',
      }
    },
  },
  plugins: [],
};
