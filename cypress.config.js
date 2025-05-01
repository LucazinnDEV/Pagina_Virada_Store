const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://127.0.0.1:8000',
    supportFile: false,
    specPattern: 'cypress/e2e/**/*.cy.js',
    defaultCommandTimeout: 10000,
    pageLoadTimeout: 60000,
  },
  video: true,
  screenshotOnRunFailure: true,
})
