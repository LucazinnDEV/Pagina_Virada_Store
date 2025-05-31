describe('Finalizar Compra', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.contains('Adicionar ao Carrinho').first().click();
    cy.contains('Ver Carrinho').click();
    cy.contains('Finalizar Compra').click(); 
  });

  it('Compra com dados válidos', () => {
    cy.get('input[name="nome"]').clear().type('João');
    cy.get('input[name="sobrenome"]').clear().type('Silva');
    cy.get('input[name="cep"]').clear().type('01000-000');
    cy.get('input[name="endereco"]').clear().type('Rua Exemplo, 123');
    cy.get('select[name="forma_pagamento"]').select('Cartão de Crédito');
    cy.contains('Confirmar Compra').click();
    cy.contains('Obrigado pela sua compra').should('be.visible');
  });

  it('Tenta finalizar deixando um campo vazio', () => {
    cy.get('input[name="nome"]').clear().type('João');
    cy.get('input[name="sobrenome"]').clear().type('Silva');
    cy.get('input[name="cep"]').clear().type('01000-000');
    cy.get('input[name="endereco"]').clear(); 
    cy.get('select[name="forma_pagamento"]').select('Pix');
    cy.contains('Confirmar Compra').click();
    cy.url().should('include', '/checkout');
    cy.get('form').should('exist'); 
  });
});
