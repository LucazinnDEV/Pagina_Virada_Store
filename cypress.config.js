const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://127.0.0.1:8000',
    supportFile: false,
    specPattern: 'cypress/e2e/**/*.cy.js',
    defaultCommandTimeout: 20000, 
    pageLoadTimeout: 120000,
    retries: {
      runMode: 2, 
      openMode: 0,
    },
    viewportWidth: 1280,
    viewportHeight: 720,
  },
  video: true,
  screenshotOnRunFailure: true,
  trashAssetsBeforeRuns: true, 
})
