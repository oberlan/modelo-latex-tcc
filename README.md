# Modelo LaTeX de TCC (DCE/Ceunes/Ufes)

Modelo de Trabalho de Conclusão de Curso para os cursos de Ciência da Computação e de Engenharia de Computação do Departamento de Computação e Eletrônica (DCE) do Centro Universitário Norte do Espírito Santo (Ceunes/Ufes).

O modelo segue as normas da ABNT vigentes:

* NBR 14724:2024 (trabalhos acadêmicos);
* NBR 10520:2023 (citações);
* NBR 6023 (referências);
* NBR 6024:2012 (numeração progressiva) e NBR 6027:2012 (sumário);
* NBR 6028:2021 (resumo).

Também atende ao Art. 19 da Portaria Normativa nº 310/2026 da Ufes, que exige a declaração do uso de inteligência artificial.

## Qual modelo usar

O TCC pode ser do tipo **científico** (o foco está na pesquisa) ou **tecnológico** (o foco está no produto). Há um arquivo principal para cada tipo:

| Tipo | Arquivo principal | Pasta de conteúdo | Exemplo fictício |
|---|---|---|---|
| Científico | `tcc-cientifico.tex` | `cientifico/` | heurística para o problema da mochila multidimensional |
| Tecnológico | `tcc-tecnologico.tex` | `tecnologico/` | sistema web para agendamento de monitorias |

Escolha um deles e apague o outro arquivo principal e a outra pasta. As pastas `config/`, `comum/`, `figuras/` e `codigos/` e o arquivo `referencias.bib` servem aos dois.

## Por onde começar

1. Preencha `cientifico/dados.tex` (ou `tecnologico/dados.tex`): curso, título, autor, orientador e banca. O comando `\curso{cc}` ou `\curso{ec}` ajusta o nome do curso e do grau na capa, na folha de rosto e na folha de aprovação.
2. Leia as caixas azuis de **Orientação** em cada capítulo. Elas explicam o que escrever em cada parte e mostram exemplos de LaTeX.
3. Substitua o texto de exemplo pelo seu, capítulo por capítulo.
4. Declare as siglas em `siglas.tex` e as referências em `referencias.bib`.
5. Na versão entregue à banca, desligue as caixas de orientação (veja abaixo).

## Compilação

* **Compilador:** pdfLaTeX (padrão). O modelo também compila com XeLaTeX e LuaLaTeX.
* **Bibliografia:** Biber (não BibTeX).
* **Overleaf:** em *Menu*, escolha o compilador pdfLaTeX. O Overleaf detecta o Biber sozinho.
* **Instalação local:** `latexmk -pdf tcc-cientifico.tex`, ou a sequência `pdflatex`, `biber`, `pdflatex`, `pdflatex`.

O estilo `biblatex-abnt` precisa ser a versão 4.0 ou mais recente (TeX Live 2024 em diante), que segue a NBR 10520:2023 e escreve o sobrenome do autor em maiúsculas e minúsculas também dentro dos parênteses, como em (Silva, 2020).

## Chaves de controle

No início do arquivo principal:

```latex
\mostrarinstrucoestrue   % caixas de orientação visíveis
\mostrarnotastrue        % notas de revisão visíveis
```

Troque por `\mostrarinstrucoesfalse` e `\mostrarnotasfalse` na versão final. As caixas de orientação podem continuar no código, mas `\begin{instrucao}` e `\end{instrucao}` devem ficar sozinhos na linha.

Para trocar comentários com o orientador dentro do texto, use `\notaaluno{...}` e `\notaorientador{...}`.

## Capítulo ou seção?

A NBR 14724:2024 determina que o trabalho seja dividido em seções, e não em capítulos. No PDF não há diferença, porque o título continua saindo como "1 INTRODUÇÃO". O que muda é o nome usado nas referências cruzadas. O padrão do modelo é "Capítulo". Para adotar o termo da norma, altere `\termocap` e `\termocaps` em `config/estilo.tex` e revise os artigos no texto ("o Capítulo 2" passa a ser "a Seção 2").

## Estrutura de arquivos

```
tcc-cientifico.tex        arquivo principal do TCC científico
tcc-tecnologico.tex       arquivo principal do TCC tecnológico
referencias.bib           referências (Biber + biblatex-abnt)
config/
  pacotes.tex             pacotes (não é preciso alterar)
  estilo.tex              aparência, quadros, códigos, referências cruzadas
  elementos.tex           capa, folha de rosto e folha de aprovação
comum/                    dedicatória, agradecimentos e epígrafe
cientifico/ e tecnologico/
  dados.tex               dados do trabalho
  siglas.tex              siglas (pacote acro)
  resumo.tex, abstract.tex
  capitulos/              um arquivo por capítulo
  apendices/              declaração de uso de IA e demais apêndices
figuras/                  imagens (brasão e figuras dos exemplos)
codigos/                  códigos incluídos com \lstinputlisting
```

## Comandos mais usados

| Para | Use |
|---|---|
| Citar com o autor na frase | `\textcite{chave}` → Silva (2020) |
| Citar entre parênteses | `\cite{chave}` → (Silva, 2020) |
| Citar com página | `\cite[15]{chave}` → (Silva, 2020, p. 15) |
| Referência cruzada | `\cref{rotulo}` ou `\Cref{rotulo}` → Figura 3, Tabela 2, Capítulo 4 |
| Sigla | `\ac{chave}` (primeira vez por extenso, depois só a sigla) |
| Fonte de ilustração própria | `\fonteautor` |
| Fonte de ilustração de terceiros | `\fonte{Adaptado de \textcite{chave}.}` |
| Citação direta longa | ambiente `citacao` |
| Alíneas a), b), c) | ambiente `alineas` |
| Quadro, código, algoritmo | ambientes `quadro`, `codigo` e `algoritmo` |

## Figuras dos exemplos

As figuras dos exemplos são vetoriais. A maioria foi desenhada em TikZ ou pgfplots dentro do próprio texto. O gráfico `figuras/cientifico/boxplot-ablacao.pdf` foi gerado pelo script `figuras/cientifico/gerar_boxplot_ablacao.py`, que mostra como produzir um gráfico em PDF no Python, com vírgula decimal e cores legíveis em escala de cinza.

Os números e os dados dos exemplos são fictícios.

## Créditos e licença

Adaptado do modelo do DI/CT/Ufes (Prof. Vítor E. Silva Souza) e baseado no abnTeX2. Distribuído sob a LaTeX Project Public License 1.3c.
