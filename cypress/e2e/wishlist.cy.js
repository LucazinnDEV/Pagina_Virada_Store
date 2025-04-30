// cypress/e2e/wishlist.cy.js

describe('Lista de Desejos', () => {
  it('Adiciona e remove da lista de desejos com usuário logado', () => {
    // Vai para a home
    cy.visit('/');

    // Clica no botão de login (ícone do usuário)
    cy.get('a[href="/login/"] i.bi-person-circle').click();

    // Confirma que está na página de login
    cy.url().should('include', '/login');
    cy.contains('Faça login');

    // Preenche o login
    cy.get('input[name="username"]').type('joao');
    cy.get('input[name="password"]').type('270406');

    // Clica no botão "Entrar"
    cy.contains('Entrar').click();

    // Confirma que voltou para a home
    cy.url().should('eq', 'http://127.0.0.1:8000/');

    // Faz uma busca
    cy.get('input[name="q"]').type('pai');
    cy.get('form').first().submit();

    // Verifica que está na busca
    cy.url().should('include', '/buscar');

    // Clica em "Ver Detalhes"
    cy.contains('Ver Detalhes').click();

    // Verifica que está na página do livro
    cy.url().should('match', /\/\d+\/$/); // ex: /10/

    // Clica para adicionar à wishlist
    cy.contains('Adicionar à Lista de Desejos').click();

    // Verifica que o botão mudou para "Remover da Lista de Desejos"
    cy.contains('Remover da Lista de Desejos').should('exist');

    // Remove da wishlist
    cy.contains('Remover da Lista de Desejos').click();

    // Verifica que voltou para "Adicionar à Lista de Desejos"
    cy.contains('Adicionar à Lista de Desejos').should('exist');
  });

  it('Redireciona para login ao tentar acessar página de wishlist sem login', () => {
    // Vai para a home
    cy.visit('/');

    // Faz uma busca por "pai"
    cy.get('input[name="q"]').type('pai');
    cy.get('form').first().submit();

    // Verifica que está na página de busca
    cy.url().should('include', '/buscar');

    // Clica em "Ver Detalhes" do primeiro livro
    cy.contains('Ver Detalhes').click();

    // Verifica que está na página do livro
    cy.url().should('match', /\/\d+\/$/);

    // Tenta visitar wishlist diretamente
    cy.visit('/wishlist/');

    // Deve ser redirecionado para login
    cy.url().should('include', '/login');
    cy.contains('Faça login').should('exist');
  });
});
