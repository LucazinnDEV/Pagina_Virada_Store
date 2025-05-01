describe('Testes de cadastro: cenário bom e ruim', () => {
  it('Cenário bom: cadastro completo e login', () => {
    const timestamp = Date.now();
    const usuario = `usuario_${timestamp}`;
    const senha = 'SenhaForte@2024';
    const email = `teste_${timestamp}@exemplo.com`;
    const cpf = `${timestamp}`.slice(0, 11);
    const telefone = `11999${timestamp}`.slice(0, 11);
    const cep = `${timestamp}`.slice(0, 8);

    cy.visit('/');

    cy.get('a[href="/login/"], a[href="/logout/"]').first().click();
    cy.location('pathname').then((path) => {
      if (path !== '/login/') {
        cy.get('a[href="/login/"] i.bi-person-circle').parent().click();
      }
    });

    cy.url().should('include', '/login');
    cy.contains('Cadastre-se').click();

    cy.get('input[name="username"]').type(usuario);
    cy.get('input[name="email"]').type(email);
    cy.get('input[name="password1"]').type(senha);
    cy.get('input[name="password2"]').type(senha);
    cy.get('select[name="tipo_pessoa"]').select('Física');
    cy.get('input[name="nome"]').type(`João_${timestamp}`);
    cy.get('input[name="sobrenome"]').type(`Silva_${timestamp}`);
    cy.get('input[name="data_nascimento"]').type('2000-01-01');
    cy.get('input[name="cpf"]').type(cpf);
    cy.get('input[name="cep"]').type(cep);
    cy.get('input[name="endereco"]').type(`Rua Exemplo ${timestamp}`);
    cy.get('input[name="telefone"]').type(telefone);

    cy.get('form').last().within(() => {
      cy.contains('Cadastre-se').click();
    });

    cy.url({ timeout: 10000 }).should('include', '/login');

    cy.get('input[name="username"]').type(usuario);
    cy.get('input[name="password"]').type(senha);
    cy.contains('Entrar').click();

    cy.url().should('eq', 'http://127.0.0.1:8000/');
  });

  it('Cenário ruim: cadastro com campo obrigatório em branco (nome)', () => {
    const timestamp = Date.now();
    const usuario = `usuario_fail_${timestamp}`;
    const senha = 'SenhaForte@2024';
    const email = `fail_${timestamp}@exemplo.com`;
    const cpf = `${timestamp}`.slice(0, 11);
    const telefone = `11999${timestamp}`.slice(0, 11);
    const cep = `${timestamp}`.slice(0, 8);

    cy.visit('/');

    cy.get('a[href="/login/"]').first().click();
    cy.contains('Cadastre-se').click();

    cy.get('input[name="username"]').type(usuario);
    cy.get('input[name="email"]').type(email);
    cy.get('input[name="password1"]').type(senha);
    cy.get('input[name="password2"]').type(senha);
    cy.get('select[name="tipo_pessoa"]').select('Física');
    cy.get('input[name="sobrenome"]').type(`Silva_${timestamp}`);
    cy.get('input[name="data_nascimento"]').type('2000-01-01');
    cy.get('input[name="cpf"]').type(cpf);
    cy.get('input[name="cep"]').type(cep);
    cy.get('input[name="endereco"]').type(`Rua Exemplo ${timestamp}`);
    cy.get('input[name="telefone"]').type(telefone);

    cy.get('form').last().within(() => {
      cy.contains('Cadastre-se').click();
    });

    cy.get('input[name="nome"]').should('have[aria-invalid="true"]');  

    cy.url().should('include', '/registrar');
  });
});
