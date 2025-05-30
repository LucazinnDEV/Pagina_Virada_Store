describe('Login Admin', () => {
  it('Login com credenciais corretas', () => {
    cy.visit('/admin/');
    cy.get('#id_username').type('joao');
    cy.get('#id_password').type('270406');
    cy.get('form').submit();
    cy.url().should('include', '/admin/');
    cy.get('#site-name', { timeout: 10000 }).should(($el) => {
      const text = $el.text();
      expect(text).to.satisfy(t => t.includes('Administração') || t.includes('Site administration'));
    });
  });

  it('Login com credenciais erradas', () => {
    cy.visit('/admin/');
    cy.get('#id_username').type('joao');
    cy.get('#id_password').type('senhaerrada');
    cy.get('form').submit();
    cy.get('.errornote', { timeout: 20000 }).should('be.visible');
    cy.get('.errornote').should(($el) => {
      const text = $el.text();
      expect(text).to.satisfy(t =>
        t.includes('Por favor, insira um usuário e senha corretos') ||
        t.includes('Please enter the correct username and password')
      );
    });
  });
});
