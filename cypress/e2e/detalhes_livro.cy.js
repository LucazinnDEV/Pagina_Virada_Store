describe('Detalhes do Livro', () => {
  it('Livro válido', () => {
    cy.visit('/livro/1'); 

    cy.wait(2000);

    cy.contains('Ver Detalhes', { timeout: 20000 }).should('be.visible');
  });

  it('Livro inválido', () => {
    cy.visit('/livro/999'); 

    cy.wait(2000);

    cy.contains('Ops! O livro não foi encontrado.', { timeout: 20000 }).should('be.visible');
  });
});
