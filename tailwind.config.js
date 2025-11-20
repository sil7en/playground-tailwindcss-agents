/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.html",
    "./assets/js/**/*.js"
  ],
  theme: {
    extend: {
      colors: {
        'neo-white': '#FFFFFF',
        'neo-black': '#000000',
        'neo-yellow': '#FFDE00', // Bright yellow
        'neo-pink': '#FF66CC',   // Hot pink
        'neo-blue': '#3366FF',   // Bright blue
        'neo-green': '#00FF66',  // Neon green
        'neo-purple': '#CC33FF', // Bright purple
        'neo-bg': '#F0F0F0',     // Light gray for background
      },
      boxShadow: {
        'neo': '4px 4px 0px 0px rgba(0,0,0,1)',
        'neo-sm': '2px 2px 0px 0px rgba(0,0,0,1)',
        'neo-lg': '8px 8px 0px 0px rgba(0,0,0,1)',
      },
      borderWidth: {
        '3': '3px',
      },
      borderRadius: {
        'none': '0px',
        'sm': '2px',
        'DEFAULT': '4px',
      }
    },
  },
  plugins: [],
}
