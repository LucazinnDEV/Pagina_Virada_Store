describe('Criação e edição de perfil', () => {
  it('Registra novo usuário', () => {
    cy.visit('/registro'); 
    cy.get('#id_username').type('usuario_teste');
    cy.get('#id_email').type('teste@exemplo.com');
    cy.get('#id_password1').type('SenhaSegura123!');
    cy.get('#id_password2').type('SenhaSegura123!');
    cy.get('form').submit();
    cy.url().should('not.include', '/registro');
  });

  it('Edita o perfil do usuário logado', () => {
    cy.visit('/login');
    cy.get('#id_username').type('usuario_teste');
    cy.get('#id_password').type('SenhaSegura123!');
    cy.get('form').submit();
    cy.url().should('not.include', '/login');

    cy.visit('/perfil/editar');
    cy.get('#id_first_name').clear().type('NomeTeste');
    cy.get('#id_last_name').clear().type('SobrenomeTeste');
    cy.get('form').submit();

    cy.contains('Perfil atualizado com sucesso').should('be.visible');
  });
});