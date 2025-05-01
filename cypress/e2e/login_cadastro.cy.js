describe('Testes de cadastro: cenário bom e ruim', () => {
  it('Cenário bom: cadastro completo e login', () => {
    cy.visit('/cadastro/');

    cy.get('#id_nome').type('João da Silva');
    cy.get('#id_email').type('joao@exemplo.com');
    cy.get('#id_senha').type('senha123');
    cy.get('#id_confirmar_senha').type('senha123');
    cy.get('form').submit();

    cy.contains('Bem-vindo, João!', { timeout: 10000 }).should('be.visible');
  });

  it('Cenário ruim: cadastro com campo obrigatório em branco (nome)', () => {
    cy.visit('/cadastro/');

    cy.get('#id_nome').clear();
    cy.get('#id_email').type('joao@exemplo.com');
    cy.get('#id_senha').type('senha123');
    cy.get('#id_confirmar_senha').type('senha123');
    cy.get('form').submit();

    cy.get('#id_nome').should('have.attr', 'aria-invalid', 'true');

    cy.contains('Este campo é obrigatório', { timeout: 10000 }).should('be.visible');
  });
});
