describe('Detalhes do Livro', () => {
  it('Livro válido', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();

    cy.contains('Ver Detalhes').first().click();

    cy.url().should('match', /\/\d+\/$/);

    cy.get('h1, h2, h3').should('exist');
  });

  it('Livro inválido', () => {
    cy.visit('/9999/', { failOnStatusCode: false });

    cy.contains('Page not found (404)').should('exist');

    cy.contains('Ops! O livro não foi encontrado.').should('exist');  
  });
});
