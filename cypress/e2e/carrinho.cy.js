describe('Carrinho', () => {
  it('Adiciona item ao carrinho e acessa a página', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();
    cy.contains('Ver Detalhes', { timeout: 10000 }).first().click();
    cy.contains('COMPRAR AGORA', { matchCase: false }).click();
    cy.url().should('include', '/carrinho/');
  });

  it('Tenta acessar o carrinho sem itens', () => {
    cy.visit('/carrinho/');
    cy.contains('Seu carrinho está vazio').should('exist');
  });
});
