describe('Finalizar Compra', () => {
  it('Compra com dados válidos', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();
    cy.contains('Ver Detalhes').first().click();
    cy.contains('COMPRAR AGORA').click();

    cy.contains('Finalizar Compra').click();
    cy.url().should('include', '/confirmar-finalizacao/');
    cy.contains('Sim, Finalizar Compra').click();
    cy.url().should('include', '/checkout/');

    // Preenche todos os campos corretamente
    cy.get('input[name="nome"]').type('João');
    cy.get('input[name="sobrenome"]').type('Cliente');
    cy.get('input[name="cep"]').type('50720000');
    cy.get('input[name="endereco"]').type('Rua das Letras, 123');

    cy.contains('Confirmar Compra').click();

    // Verifica se a compra foi finalizada com sucesso
    cy.url().should('include', '/checkout/');
    cy.contains('Obrigado pela sua compra').should('exist');
  });

  it('Tenta finalizar deixando um campo vazio', () => {
    cy.visit('/');
    cy.get('input[name="q"]').clear().type('pai');
    cy.get('form').first().submit();
    cy.contains('Ver Detalhes').first().click();
    cy.contains('COMPRAR AGORA').click();

    cy.contains('Finalizar Compra').click();
    cy.url().should('include', '/confirmar-finalizacao/');
    cy.contains('Sim, Finalizar Compra').click();
    cy.url().should('include', '/checkout/');

    // Preenche todos os campos exceto "nome"
    // cy.get('input[name="nome"]').type('João'); ← esse fica em branco
    cy.get('input[name="sobrenome"]').type('Cliente');
    cy.get('input[name="cep"]').type('50720000');
    cy.get('input[name="endereco"]').type('Rua das Letras, 123');

    cy.contains('Confirmar Compra').click();

    // Verifica que o formulário não foi enviado (continua na mesma página)
    cy.url().should('include', '/checkout/');
  });
});
