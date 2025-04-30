describe('Páginas básicas', () => {
  const paginas = ['/', '/categorias/', '/recomendados/', '/logout/'];
  paginas.forEach(pagina => {
    it(`Acessa ${pagina}`, () => {
      cy.visit(pagina);
      cy.contains('Página Virada').should('exist');
    });
  });
});