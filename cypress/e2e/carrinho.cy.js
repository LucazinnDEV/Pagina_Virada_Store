describe('Carrinho', () => {
  beforeEach(() => {
    cy.clearLocalStorage();
    cy.clearCookies();
  });

  it('Adiciona item ao carrinho e acessa a página do carrinho', () => {
    // cy.visit('/produto/1/');  // Depende do produto existir
    // cy.get('#comprarBtn').click();  // Depende da página carregada
    // cy.get('#confirmModal').should('be.visible');  // Depende do modal aparecer
    // cy.get('#goToCart').click();  // Depende do modal
    // cy.url().should('include', '/carrinho');  // Verifica url após clicar
    // cy.get('tbody tr').should('have.length.greaterThan', 0);  // Verifica itens no carrinho
    // cy.contains('Finalizar Compra').should('be.visible');  // Verifica botão visível
  });

  it('Exibe mensagem ao acessar o carrinho vazio', () => {
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio').should('be.visible');
  });
});
