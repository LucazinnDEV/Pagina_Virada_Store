describe('Páginas básicas', () => {
  const paginas = ['/', '/categorias/', '/recomendados/', '/logout/'];
  
  paginas.forEach((pagina) => {
    it(`Acessa a página ${pagina}`, () => {
      cy.visit(pagina);
    });
  });
});
