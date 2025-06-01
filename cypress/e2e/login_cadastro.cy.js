describe('Testes de cadastro: cenário bom e ruim', () => {
  it('Cenário bom: cadastro completo e login', () => {
    cy.visit('/'); 
    cy.wait(2000); 
  });

  it('Cenário ruim: cadastro com campo obrigatório em branco (nome)', () => {
    cy.visit('/'); 
    cy.wait(2000); 
  });
});
