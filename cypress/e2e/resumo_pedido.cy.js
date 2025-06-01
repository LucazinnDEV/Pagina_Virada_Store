describe('Resumo do Pedido e Rastreamento', () => {
  it('Acessa a página de resumo do pedido e verifica elementos básicos', () => {
    cy.visit('/pedido/resumo'); 
    cy.contains('Resumo do Pedido').should('be.visible');
    cy.contains('Status do Pedido').should('be.visible');
    cy.get('#rastreamento').should('exist');
  });
});