describe('Carrinho', () => {
  beforeEach(() => {
    cy.clearLocalStorage();
    cy.clearCookies();
  });

  it('Adiciona item ao carrinho e acessa a página', () => {
    cy.visit('/');
    cy.wait(2000); 
  });

  it('Exibe mensagem ao acessar o carrinho vazio', () => {
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio').should('be.visible');
  });
});