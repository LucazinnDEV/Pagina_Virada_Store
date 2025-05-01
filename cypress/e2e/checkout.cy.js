describe('Finalizar Compra', () => {
  it('Compra com dados válidos', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();

    cy.contains('Ver Detalhes', { timeout: 10000 }).first().click();
    cy.contains('COMPRAR AGORA', { timeout: 10000 }).click();

    cy.contains('Finalizar Compra', { timeout: 10000 }).click();
    cy.url().should('include', '/confirmar-finalizacao/');
    cy.contains('Sim, Finalizar Compra', { timeout: 10000 }).click();
    cy.url().should('include', '/checkout/');

    cy.get('input[name="nome"]').clear().type('João');
    cy.get('input[name="sobrenome"]').clear().type('Cliente');
    cy.get('input[name="cep"]').clear().type('50720000');
    cy.get('input[name="endereco"]').clear().type('Rua das Letras, 123');

    cy.contains('Confirmar Compra', { timeout: 10000 }).click();

    cy.url().should('include', '/checkout/');
    cy.contains('Obrigado pela sua compra', { timeout: 10000 }).should('exist');
  });

  it('Tenta finalizar deixando um campo vazio', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();

    cy.contains('Ver Detalhes', { timeout: 10000 }).first().click();
    cy.contains('COMPRAR AGORA', { timeout: 10000 }).click();

    cy.contains('Finalizar Compra', { timeout: 10000 }).click();
    cy.url().should('include', '/confirmar-finalizacao/');
    cy.contains('Sim, Finalizar Compra', { timeout: 10000 }).click();
    cy.url().should('include', '/checkout/');

    cy.get('input[name="sobrenome"]').clear().type('Cliente');
    cy.get('input[name="cep"]').clear().type('50720000');
    cy.get('input[name="endereco"]').clear().type('Rua das Letras, 123');

    cy.contains('Confirmar Compra', { timeout: 10000 }).click();

    cy.url().should('include', '/checkout/');
    cy.contains('Campo obrigatório', { timeout: 10000 }).should('exist'); 
  });
});
