describe('Carrinho', () => {
  beforeEach(() => {
    cy.clearLocalStorage();
    cy.clearCookies();
  });

  it('Exibe mensagem ao acessar o carrinho vazio', () => {
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio').should('be.visible');
  });
});
