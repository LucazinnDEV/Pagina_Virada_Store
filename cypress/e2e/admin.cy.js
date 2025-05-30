describe('Login Admin', () => {
  it('Login com credenciais corretas', () => {
    cy.visit('/admin/');
    cy.get('#id_username').type('joao');
    cy.get('#id_password').type('270406');
    cy.get('form').submit();
    cy.url().should('include', '/admin/');
    cy.get('#site-name', { timeout: 10000 }).should('contain.text', 'Site administration');
  });

  it('Login com credenciais erradas', () => {
    cy.visit('/admin/');
    cy.get('#id_username').type('joao');
    cy.get('#id_password').type('senhaerrada');
    cy.get('form').submit();
    cy.get('.errornote', { timeout: 10000 }).should('be.visible');
    cy.get('.errornote').should('contain.text', 'Please enter the correct username and password');
  });
});
