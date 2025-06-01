describe('Criação e edição de perfil', () => {
  it('Acessa a página inicial', () => {
    cy.visit('/');
    cy.contains('Bem-vindo').should('be.visible'); 
  });
});
