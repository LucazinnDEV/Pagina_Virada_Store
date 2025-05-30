describe('Busca de Livros', () => {
  it('Busca existente', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();
    cy.contains(/pai/i, { timeout: 10000 }).should('exist');
  });

  it('Busca inexistente', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('asdjklqwe123');
    cy.get('form').first().submit();
    cy.contains('Desculpe, não encontramos resultados para sua pesquisa.', { timeout: 10000 }).should('exist');
  });
});
