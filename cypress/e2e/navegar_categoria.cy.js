describe('Navegar por Categoria', () => {
  it('Acessa página de categorias', () => {
    cy.visit('/categorias');
    cy.url().should('include', '/categorias');
    cy.get('.livro-item').its('length').should('be.gte', 1);
  });
});
