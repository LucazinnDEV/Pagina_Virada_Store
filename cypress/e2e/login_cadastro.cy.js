describe('Testes de cadastro: cenário bom e ruim', () => {

  const usuario = {
    nome: 'João da Silva',
    email: 'joao@example.com',
    senha: 'senha123'
  };

  it('Cenário bom: cadastro completo e login', () => {
    cy.visit('/registrar/'); 
    cy.get('#id_nome').type(usuario.nome);
    cy.get('#id_email').type(usuario.email);
    cy.get('#id_senha').type(usuario.senha);
    cy.get('#id_confirmar_senha').type(usuario.senha);
    cy.get('form').submit();
    cy.contains('Cadastro realizado com sucesso').should('be.visible');
    cy.visit('/login/');
    cy.get('input[name="username"]').type(usuario.email);
    cy.get('input[name="password"]').type(usuario.senha);
    cy.get('button[type="submit"]').click();

    cy.contains('Bem-vindo').should('be.visible'); 
  });

  it('Cenário ruim: cadastro com campo obrigatório em branco (nome)', () => {
    cy.visit('/registrar/'); 
    cy.get('#id_email').type('teste@example.com');
    cy.get('#id_senha').type('senha123');
    cy.get('#id_confirmar_senha').type('senha123');
    cy.get('form').submit();
    cy.contains('Este campo é obrigatório').should('be.visible');
  });

});
