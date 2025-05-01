describe('Carrinho', () => {
  it('Adiciona item ao carrinho e acessa a página', () => {
    cy.visit('/');

    cy.contains('Adicionar ao Carrinho').click();

    cy.wait(2000);

    cy.contains('Ver Carrinho').click();

    cy.url().should('include', '/carrinho');
    cy.contains('Ver Detalhes', { timeout: 15000 }).should('be.visible'); 

    cy.get('.carrinho-item').should('have.length.greaterThan', 0); 
  });

  it('Tenta acessar o carrinho sem itens', () => {
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio').should('be.visible');
  });
});
