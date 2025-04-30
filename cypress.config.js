const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    baseUrl: 'http://127.0.0.1:8000',
    supportFile: false,
    defaultCommandTimeout: 10000
  }
})
