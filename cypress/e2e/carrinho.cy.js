describe('Carrinho', () => {
  before(() => {
    cy.login('admin', 'admin123');        
    cy.visit('/admin/forum/livro/add/');    
    cy.get('#id_titulo').type('Livro Cypress');
    cy.get('#id_autor').type('Autor Teste');
    cy.get('#id_preco').clear().type('49.90');
    cy.get('input[name="_save"]').click(); 
    cy.contains('was added successfully', { timeout: 10000 }).should('exist');
    cy.logout(); 
  });

  it('Adiciona item ao carrinho e acessa a página', () => {
    cy.visit('/');
    cy.contains('Adicionar ao Carrinho', { timeout: 10000 }).first().click();
    cy.contains('Ver Carrinho', { timeout: 10000 }).click();

    cy.url().should('include', '/carrinho');
    cy.get('.carrinho-item', { timeout: 10000 }).should('have.length.greaterThan', 0);
  });
  
  it('Tenta acessar o carrinho sem itens', () => {
    cy.visit('/logout');         
    cy.visit('/carrinho');
    cy.contains('Seu carrinho está vazio', { timeout: 10000 }).should('be.visible');
  });
});
