describe('Logout do usuário', () => {
    it('Realiza login e depois logout com sucesso (cenário bom)', () => {
      cy.visit('/');
  
      cy.get('a[href="/login/"] i.bi-person-circle').click();
  
      cy.get('input[name="username"]').type('joao');
      cy.get('input[name="password"]').type('270406');
  
      cy.contains('Entrar').click();
  
      cy.url().should('eq', 'http://127.0.0.1:8000/');
  
      cy.get('a[href="/logout/"] i.bi-box-arrow-right').click();
  
      cy.url().should('eq', 'http://127.0.0.1:8000/');
      cy.get('a[href="/login/"] i.bi-person-circle').should('exist');
    });
  
    it('Tenta acessar /logout/ sem estar logado (cenário ruim)', () => {
      cy.visit('/logout/');
  
      // Verifica que foi redirecionado para o login ou voltou pra home
      cy.url().should('satisfy', (url) => {
        return (
          url === 'http://127.0.0.1:8000/login/' ||
          url === 'http://127.0.0.1:8000/'
        );
      });
  
      // Verifica se existe o botão de login
      cy.get('a[href="/login/"] i.bi-person-circle').should('exist');
    });
  });
  