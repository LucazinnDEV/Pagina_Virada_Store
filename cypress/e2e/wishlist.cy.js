describe('Lista de Desejos', () => {
  beforeEach(() => {
  });

  it('Adiciona e remove da lista de desejos com usuário logado', () => {
    cy.visit('/wishlist/');
  });
  it('Redireciona para login ao tentar acessar página de wishlist sem login', () => {
    cy.visit('/wishlist/');
  });
});
