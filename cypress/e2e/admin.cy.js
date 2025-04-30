describe('Login Admin', () => {
  it('Login com credenciais corretas', () => {
    cy.visit('/admin/');
    cy.get('#id_username').type('joao');
    cy.get('#id_password').type('270406');
    cy.get('form').submit();

    // Verifica se o painel do admin foi carregado
    cy.url().should('include', '/admin/');
    cy.get('.module').should('exist');
  });

  it('Login com credenciais erradas', () => {
    cy.visit('/admin/');
    cy.get('#id_username').type('joao');
    cy.get('#id_password').type('senhaerrada');
    cy.get('form').submit();

    // Verifica se o alerta de erro apareceu
    cy.get('.errornote').should('contain', 'usuário e senha corretos');
  });
});
