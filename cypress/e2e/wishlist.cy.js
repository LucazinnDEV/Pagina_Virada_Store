describe('Lista de Desejos', () => {
  
  const login = (username, password) => {
    cy.get('a[href="/login/"] i.bi-person-circle').click();
    cy.url().should('include', '/login');
    cy.contains('Faça login');

    cy.get('input[name="username"]').type(username);
    cy.get('input[name="password"]').type(password);
    cy.contains('Entrar').click();
    cy.url().should('eq', 'http://127.0.0.1:8000/');
  };

  it('Adiciona e remove da lista de desejos com usuário logado', () => {
    cy.visit('/');
    login('joao', '270406');

    cy.get('input[name="q"]').type('pai');
    cy.get('form').first().submit();
    cy.url().should('include', '/buscar');

    cy.contains('Ver Detalhes').click();
    cy.url().should('match', /\/\d+\/$/);

    cy.contains('Adicionar à Lista de Desejos').click();
    cy.contains('Remover da Lista de Desejos').should('exist');

    cy.contains('Remover da Lista de Desejos').click();
    cy.contains('Adicionar à Lista de Desejos').should('exist');
  });

  it('Redireciona para login ao tentar acessar página de wishlist sem login', () => {
    cy.visit('/');
    cy.get('input[name="q"]').type('pai');
    cy.get('form').first().submit();
    cy.url().should('include', '/buscar');

    cy.contains('Ver Detalhes').click();
    cy.url().should('match', /\/\d+\/$/);

    cy.visit('/wishlist/');
    cy.url().should('include', '/login');
    cy.contains('Faça login').should('exist');
  });
});
