describe('Detalhes do Livro', () => {
  it('Livro válido', () => {
    cy.visit('/'); 
    cy.wait(2000);
  });

  it('Livro inválido', () => {
    cy.visit('/'); 
    cy.wait(2000);
  });
});
