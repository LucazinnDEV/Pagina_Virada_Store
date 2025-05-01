describe('Lista de Desejos', () => {
  beforeEach(() => {
    cy.login('joao', '270406'); 
  });

  it('Adiciona e remove da lista de desejos com usuário logado', () => {
    cy.visit('/wishlist/');
    cy.contains('Adicionar à lista de desejos').click();
    cy.contains('Remover da lista de desejos').click();
  });

  it('Redireciona para login ao tentar acessar página de wishlist sem login', () => {
    cy.logout(); 
    cy.visit('/wishlist/');
    cy.url().should('include', '/login/');
  });
});
