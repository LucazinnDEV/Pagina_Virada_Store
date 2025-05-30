describe('Carrinho', () => {
  it('Adiciona item ao carrinho e acessa a página', () => {
    cy.visit('/');
    cy.get('.produto, .livro, .item', { timeout: 10000 }).first().should('be.visible');
    cy.contains('Adicionar ao Carrinho', { timeout: 10000 }).first().click();
    cy.contains('Ver Carrinho', { timeout: 10000 }).click();
    cy.url().should('include', '/carrinho');
    cy.get('.carrinho-item, .item-carrinho', { timeout: 10000 }).should('have.length.greaterThan', 0);
  });

  it('Tenta acessar o carrinho sem itens', () => {
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio', { timeout: 10000 }).should('be.visible');
  });
});
