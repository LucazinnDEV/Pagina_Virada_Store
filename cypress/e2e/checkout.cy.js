describe('Finalizar Compra', () => {
  it('Compra com dados válidos', () => {
    cy.visit('/checkout'); 
    cy.wait(2000); 
  });

  it('Tenta finalizar deixando um campo vazio', () => {
    cy.visit('/checkout');
  });
});
