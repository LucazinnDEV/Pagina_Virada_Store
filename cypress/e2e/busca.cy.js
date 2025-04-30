describe('Busca de Livros', () => {
  it('Busca existente', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();

    // Verifica que algum resultado com "pai" aparece
    cy.contains('pai', { matchCase: false }).should('exist');
  });

  it('Busca inexistente', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('asdjklqwe123');
    cy.get('form').first().submit();

    // Verifica a mensagem exibida quando não há resultados
    cy.contains('Desculpe, não encontramos resultados para sua pesquisa.').should('exist');
  });
});
