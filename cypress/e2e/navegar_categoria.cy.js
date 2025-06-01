describe('Navegar por Categoria', () => {
  it('Acessa página de categorias e navega para uma categoria específica', () => {
    cy.visit('/categorias'); 
    cy.get('.categoria-item').first().click(); 
    cy.url().should('include', '/categoria/');
    cy.get('.livro-item').its('length').should('be.gte', 1);
  });
});