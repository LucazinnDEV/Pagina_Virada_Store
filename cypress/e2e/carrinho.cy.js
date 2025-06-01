describe('Carrinho', () => {
  beforeEach(() => {
    cy.clearLocalStorage();
    cy.clearCookies();
  });

  it('Adiciona item ao carrinho e acessa a página do carrinho', () => {
    cy.visit('/livro/1/');  
    cy.get('#comprarBtn').should('be.visible').click();
    cy.get('#confirmModal', { timeout: 10000 }).should('be.visible');
    cy.get('#goToCart').click();
    cy.url().should('include', '/carrinho');
    cy.get('tbody tr').should('have.length.greaterThan', 0);
    cy.contains('Finalizar Compra').should('be.visible');
  });

  it('Exibe mensagem ao acessar o carrinho vazio', () => {
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio').should('be.visible');
  });
});
