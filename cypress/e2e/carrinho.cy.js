describe('Carrinho', () => {
  it('Adiciona item ao carrinho e acessa a página', () => {
    cy.visit('/');
    cy.wait(2000); 
  });

  it('Tenta acessar o carrinho sem itens', () => {
    cy.visit('/carrinho');
  });
});
