# Organizador de arquivos pelo tipo da extensão

Esse projeto é um script em Python que organiza automaticamente os arquivos de uma pasta selecionada, separando-os em subpastas de acordo com o tipo de arquivo (por extensão). A interface para seleção de pasta é feita com a biblioteca `Tkinter`.

## Funcionamento

1. O usuário escolhe uma pasta por meio da interface gráfica.
2. O script verifica todos os arquivos existentes na pasta.
3. Com base na extensão do arquivo, ele é movido para uma subpasta correspondente:
   - `imagens/` → `.png`, `.jpg`, `.jpeg`
   - `planilhas/` → `.xlsx`, `.xlsm`
   - `pdfs/` → `.pdf`
   - `csv/` → `.csv`
4. Se a subpasta não existir, ela será criada automaticamente.
5. O arquivo é movido para a subpasta correspondente.

