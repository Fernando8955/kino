# Kino del Sur — como colocar no ar de graça

Você tem dois arquivos:

- `index.html` — o site inteiro
- `resultados.json` — a lista de resultados

O site lê o `resultados.json`. Para lançar um resultado novo, você só edita esse
arquivo. Não precisa mexer no `index.html` nunca mais.

---

## Parte 1 — colocar no ar (uma vez só, ~10 minutos)

### 1. Criar conta no GitHub
Acesse **github.com** → *Sign up*. É grátis. Guarde o usuário e a senha.

### 2. Criar o repositório
- Clique no **+** no canto superior direito → *New repository*
- Nome: `kino-del-sur`
- Marque **Public**
- *Create repository*

### 3. Subir os dois arquivos
- Na tela do repositório, clique em **uploading an existing file**
- Arraste o `index.html` e o `resultados.json`
- Clique em **Commit changes**

### 4. Publicar no Cloudflare Pages
- Acesse **pages.cloudflare.com** → crie a conta (grátis, não pede cartão)
- *Create a project* → *Connect to Git* → autorize o GitHub
- Escolha o repositório `kino-del-sur`
- Em *Framework preset* deixe **None**; os campos de build ficam **vazios**
- *Save and Deploy*

Em cerca de 1 minuto seu site está no ar em algo como:

    https://kino-del-sur.pages.dev

Pronto. Custo: zero, para sempre.

> **Alternativa mais rápida ainda:** entre em **netlify.com/drop** e arraste a
> pasta inteira. O site sobe na hora, sem conta. Mas aí, para atualizar o
> resultado, você precisa arrastar a pasta de novo todo dia — por isso o
> caminho do GitHub compensa.

---

## Parte 2 — lançar o resultado (todo dia, ~2 minutos)

### 1. Abrir o painel
No seu site, clique em **Panel** (canto superior direito) e digite o PIN.

> O PIN da demo é **2580**. Troque antes de divulgar o site: no `index.html`,
> procure a linha `var PIN_DEMO = '2580';` e mude o número.

### 2. Digitar o resultado
- Confira o **número do sorteo** e a **data**
- Toque nos **14 números** no teclado da tela (ele trava sozinho ao chegar em 14)
- Multiplicador e comodín são opcionais
- Clique em **Generar resultado**

O resultado já aparece na tela e uma **barra vermelha** avisa: *"Falta publicar"*.
Isso quer dizer que só você está vendo.

### 3. Copiar e colar no GitHub
- No painel, clique em **Copiar todo**
- Abra o GitHub → seu repositório → arquivo **resultados.json**
- Clique no **lápis** (editar)
- Apague tudo que estiver lá e **cole** o que você copiou
- Clique em **Commit changes**

Em cerca de 1 minuto o Cloudflare atualiza o site sozinho e todo mundo vê o
resultado novo.

### 4. Fechar o ciclo
Volte no painel e clique em **Ya lo pegué en el sitio**. A barra vermelha some.

Tudo isso funciona pelo celular, inclusive a edição no GitHub.

---

## Perguntas rápidas

**Perdi o resultado que digitei?**
Não. Ele fica guardado no seu navegador até você colar no GitHub. Se fechar o
site e voltar, a barra vermelha continua lá te lembrando.

**Errei um número.**
No painel, clique em **Borrar último** e digite de novo. Se já tinha colado no
GitHub, corrija direto no arquivo e faça um novo *Commit*.

**Quero um domínio próprio (kinodelsur.com).**
Aí sim custa: uns R$ 50 por ano no registro.com.br ou no Cloudflare. Depois é só
apontar nas configurações do Pages. A hospedagem continua grátis.

**Quero que o painel publique sozinho, sem esse copia-e-cola.**
Dá pra fazer com Supabase, também de graça. É só pedir.
