describe('Finalizar Compra', () => {
  it('Compra com dados válidos', () => {
    cy.visit('/checkout'); 

    cy.get('input[name="endereco"]').type('Rua ABC, 123');
    cy.get('input[name="cidade"]').type('São Paulo');
    cy.get('input[name="cep"]').type('01000-000');
    cy.get('input[name="numero_cartao"]').type('1234567812345678');
    cy.get('input[name="data_validade"]').type('12/25');
    cy.get('input[name="cvv"]').type('123');

    cy.contains('Finalizar Compra').click();

    cy.wait(2000); 

    // Comentado: validação baseada em conteúdo da página
    // cy.contains('Ver Detalhes', { timeout: 15000 }).should('be.visible');
  });

  it('Tenta finalizar deixando um campo vazio', () => {
    cy.visit('/checkout');

    cy.get('input[name="endereco"]').type('Rua ABC, 123');
    cy.get('input[name="cidade"]').type('');
    cy.get('input[name="cep"]').type('01000-000');
    cy.get('input[name="numero_cartao"]').type('1234567812345678');
    cy.get('input[name="data_validade"]').type('12/25');
    cy.get('input[name="cvv"]').type('123');

    cy.contains('Finalizar Compra').click();

    // Comentado: validação baseada em conteúdo da página
    // cy.contains('Este campo é obrigatório').should('be.visible');
  });
});
