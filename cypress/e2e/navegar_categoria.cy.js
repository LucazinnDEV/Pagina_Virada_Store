describe('Navegar por Categoria', () => {
  it('Acessa página de categorias', () => {
    cy.visit('/categorias');
    cy.url().should('include', '/categorias');
  });
});
