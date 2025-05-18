# 🤝 Contribuindo com o Projeto Página Virada Store

Seja bem-vindo(a) e obrigado(a) por considerar contribuir com o **Página Virada Store**, nosso e-commerce colaborativo focado em livros. Este documento tem como objetivo guiá-lo em como montar o ambiente, entender a proposta do projeto e colaborar de forma produtiva.

---

## 🚀 Sobre o Projeto

O Página Virada Store é um e-commerce de livros construído com Django, com foco em acessibilidade, organização e experiência do usuário.

---

## 🧰 Requisitos do Ambiente

### 1. Instale o Visual Studio Code

Baixe o VS Code:  
👉 https://code.visualstudio.com/download

### 2. Instale o Python 3.7+

Verifique se o Python está instalado:

```bash
python --version
```

Se necessário, baixe:  
👉 https://www.python.org/downloads/

### 3. Clone o Repositório

```bash
git clone https://github.com/Rafaellc-DEV/Pagina_Virada_Store
cd Pagina_Virada_Store
```

### 4. Crie e Ative um Ambiente Virtual

```bash
python -m venv venv
```

Ativação:

- **Windows:** `venv\Scripts\activate`
- **Linux/Mac:** `source venv/bin/activate`

### 5. Instale as Dependências

```bash
pip install -r requirements.txt
```

Caso o arquivo `requirements.txt` não esteja atualizado:

```bash
pip install django python-dotenv
```

### 6. Configure o Banco de Dados (SQLite)

No arquivo `settings.py`, confirme que o `DATABASES` está configurado para SQLite (default do Django).

### 7. Migre as Tabelas

```bash
python manage.py migrate
```

### 8. Rode o Projeto

```bash
python manage.py runserver
```

> Acesse: http://127.0.0.1:8000

---

## 🧪 Prototipação e Design

### Figma

Use o Figma para protótipos de baixa fidelidade:

👉 https://www.figma.com/design/aDKjwqFzzYOgslpmmFgf3w/Untitled?node-id=0-1&p=f&t=pAFx2G5DQYwb5ehp-0

Dicas:

- Crie protótipos simples com foco em **funcionalidade**, não em design visual.
- Especifique os **componentes** e **funções** esperadas de cada parte da tela.

---

## 📋 Planejamento SCRUM

Utilizamos o Jira com metodologia ágil. Veja o board aqui:  
👉 https://paginaviradastore.atlassian.net/jira/software/projects/SCRUM/summary

Etapas padrão das tarefas:

1. To-Do  
2. Prototipação Lo-Fi  
3. Prototipada  
4. Implementação  
5. Implementada  
6. Concluída

Formato das histórias de usuário:

```text
Como [tipo de usuário]
Quero [realizar algo]
Para [atingir objetivo]

Cenário:
Dado que...
Quando...
Então...
```

---

## 🧑‍💻 Como Contribuir

1. Faça um **fork** do repositório
2. Clone o repositório para sua máquina
3. Crie um branch:

```bash
git checkout -b minha-feature
```

4. Faça suas alterações seguindo as convenções de código
5. Teste localmente para garantir que tudo funciona
6. Faça commit e push para o seu fork:

```bash
git add .
git commit -m "feat: minha contribuição"
git push origin minha-feature
```

7. Crie um **Pull Request** no GitHub
8. Aguarde o feedback da equipe de revisão

---

## ✅ Boas Práticas

- Documente bem seu código
- Nomeie commits de forma clara e objetiva
- Evite enviar código quebrado ou inacabado
- Comunique-se via Discord ou WhatsApp do projeto
- Respeite todos os colaboradores com empatia e profissionalismo

---

## 🙌 Agradecimento

Obrigado por fazer parte da **Página Virada Store**!  
Sua contribuição é essencial para construirmos uma plataforma acessível, útil e eficiente para leitores e editoras.

Para dúvidas ou ajuda, entre em contato com a equipe mantenedora ou abra uma issue.

**Juntos, escrevemos novas páginas. Boas contribuições!** 📚🚀
