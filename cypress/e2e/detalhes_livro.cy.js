describe('Detalhes do Livro', () => {
  it('Livro válido', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();

    // Clica em "Ver Detalhes"
    cy.contains('Ver Detalhes').first().click();

    // Verifica que a URL tem formato /<id>/
    cy.url().should('match', /\/\d+\/$/);

    // Verifica que o título ou conteúdo do livro aparece
    cy.get('h1, h2, h3').should('exist');
  });

  it('Livro inválido', () => {
    // Acessa um ID de livro que não existe
    cy.visit('/9999/', { failOnStatusCode: false });

    // Verifica a mensagem padrão de erro do Django em modo DEBUG
    cy.contains('Page not found (404)').should('exist');
  });
});
