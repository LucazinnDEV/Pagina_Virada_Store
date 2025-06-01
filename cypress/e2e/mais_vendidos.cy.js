describe('Livros mais vendidos', () => {
  it('Carrega a página de livros mais vendidos e verifica a lista', () => {
    cy.visit('/mais-vendidos'); 
    cy.contains('Mais Vendidos').should('be.visible');
    cy.get('.livro-item').its('length').should('be.gte', 1); 
  });
});
