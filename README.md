# 🕵️ Image Analyser — OSINT Edition / LeitorMetadados

> 🚧 **Em Desenvolvimento** · Este projeto está em estágio inicial de desenvolvimento. Funcionalidades podem mudar, e bugs são esperados.
>
> 🚧 **Under Development** · This project is in early development. Features may change and bugs are expected.

---

## PT-BR 🇧🇷

### 📋 Descrição

**LeitorMetadados** é uma ferramenta **OSINT** de linha de comando que extrai e exibe metadados de imagens. Ela lê arquivos de imagem e mostra informações como dados EXIF, coordenadas GPS (com link para o Google Maps), metadados de chunks PNG e informações básicas do arquivo — tudo em uma interface estilizada com cores ANSI no terminal.

O projeto foi criado com foco em **inteligência de fonte aberta (OSINT)** e **perícia forense digital**, permitindo analisar metadados que muitas vezes contêm informações valiosas como localização, modelo de câmera, data/hora e software utilizado.

### ✨ Funcionalidades Atuais

- **Informações básicas** do arquivo (nome, formato, dimensões, modo de cor, tamanho)
- **Extração de dados EXIF** (câmera, flash, data/hora, software, etc.)
- **Coordenadas GPS** com link clicável para o Google Maps
- **Metadados de chunks PNG** (para arquivos PNG)
- **Detecção de metadados removidos** (ex.: imagens do WhatsApp)
- **Interface terminal estilizada** com cores ANSI e formatação em caixa
- **Aviso automático** quando o WhatsApp remove metadados da imagem

### 📦 Requisitos

| Dependência | Versão | Obrigatório |
|-------------|--------|-------------|
| Python      | 3.13+  | Sim         |
| Pillow      | 12.2.0 | Sim         |
| asarPy      | 1.0.1  | Não (futuro)|

### 🔧 Instalação

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd LeitorMetadados

# Crie e ative um ambiente virtual (recomendado)
python3 -m venv .venv
source .venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 🚀 Uso

```bash
python image.py
```

> ⚠️ **Atenção:** Atualmente o caminho da imagem está **hardcoded** na linha 73 do arquivo `image.py`:
> ```python
> CAMINHO = "Imagens/image.jpg"
> ```
> Você precisa **alterar essa variável** para apontar para a imagem desejada, ou colocar sua imagem em `Imagens/image.jpg`.

### 📁 Estrutura do Projeto

```
LeitorMetadados/
├── image.py           # Código principal da ferramenta
├── requirements.txt   # Dependências do projeto
├── Imagens/
│   └── image.png      # Imagem de exemplo para testes
├── .venv/             # Ambiente virtual Python
└── .git/              # Controle de versão Git
```

### 🐛 Problemas Conhecidos

- **Caminho hardcoded:** A variável `CAMINHO` em `image.py` aponta para `Imagens/image.jpg`, mas o arquivo de exemplo fornecido é `Imagens/image.png`. Será necessário renomear o arquivo ou alterar o código.
- **asarPy não utilizado:** A dependência `asarPy==1.0.1` está listada no `requirements.txt`, mas ainda não é usada no código. Foi adicionada para suporte futuro a arquivos ASAR (Electron).
- **Sem argumentos CLI:** Não é possível especificar o caminho da imagem via linha de comando. O caminho é fixo no código-fonte.
- **Sem testes automatizados:** O projeto ainda não possui testes unitários ou de integração.
- **Apenas um formato de imagem de exemplo:** O projeto precisa de mais imagens de teste em diferentes formatos (JPEG, TIFF, etc.).

### 🗺️ Roadmap

- [ ] **Argumentos CLI** — Adicionar `--image <caminho>`, `--help`, `--version`
- [ ] **Suporte a ASAR** — Extrair metadados de imagens dentro de arquivos ASAR (Electron)
- [ ] **Mais formatos** — Suporte expandido para TIFF, BMP, WebP e outros
- [ ] **Exportação** — Salvar metadados em JSON/CSV
- [ ] **Testes automatizados** — Suite de testes com pytest ou unittest
- [ ] **CI/CD** — Integração contínua com GitHub Actions
- [ ] **Empacotamento** — Publicar no PyPI ou oferecer binário standalone

---

## EN 🇬🇧

### 📋 Description

**LeitorMetadados** (Metadata Reader) is a **OSINT** command-line tool that extracts and displays metadata from image files. It reads image files and shows information such as EXIF data, GPS coordinates (with a Google Maps link), PNG chunk metadata, and basic file information — all in a styled ANSI-colored terminal interface.

The project was created with a focus on **Open Source Intelligence (OSINT)** and **digital forensics**, allowing analysts to inspect metadata that often contains valuable information such as geolocation, camera model, timestamps, and software used.

### ✨ Current Features

- **Basic file info** (name, format, dimensions, color mode, file size)
- **EXIF data extraction** (camera, flash, date/time, software, etc.)
- **GPS coordinates** with clickable Google Maps link
- **PNG chunk metadata** (for PNG files)
- **Stripped metadata detection** (e.g., WhatsApp images)
- **Styled terminal UI** with ANSI colors and box formatting
- **WhatsApp metadata removal warning**

### 📦 Requirements

| Dependency | Version | Required |
|------------|---------|----------|
| Python     | 3.13+   | Yes      |
| Pillow     | 12.2.0  | Yes      |
| asarPy     | 1.0.1   | No (future)|

### 🔧 Installation

```bash
# Clone the repository
git clone <repo-url>
cd LeitorMetadados

# Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 🚀 Usage

```bash
python image.py
```

> ⚠️ **Note:** The image path is currently **hardcoded** on line 73 of `image.py`:
> ```python
> CAMINHO = "Imagens/image.jpg"
> ```
> You need to **change this variable** to point to your desired image, or place your image at `Imagens/image.jpg`.

### 📁 Project Structure

```
LeitorMetadados/
├── image.py           # Main application code
├── requirements.txt   # Project dependencies
├── Imagens/
│   └── image.png      # Sample image for testing
├── .venv/             # Python virtual environment
└── .git/              # Git version control
```

### 🐛 Known Issues

- **Hardcoded path:** The `CAMINHO` variable in `image.py` points to `Imagens/image.jpg`, but the sample file provided is `Imagens/image.png`. You must rename the file or change the code.
- **asarPy unused:** The `asarPy==1.0.1` dependency is listed in `requirements.txt` but is not yet used in the code. It was added for future ASAR (Electron) archive support.
- **No CLI arguments:** You cannot specify the image path via command line. The path is hardcoded in the source code.
- **No automated tests:** The project currently has no unit or integration tests.
- **Single sample image:** More test images in different formats (JPEG, TIFF, etc.) are needed.

### 🗺️ Roadmap

- [ ] **CLI arguments** — Add `--image <path>`, `--help`, `--version`
- [ ] **ASAR support** — Extract metadata from images inside Electron ASAR archives
- [ ] **More formats** — Expanded support for TIFF, BMP, WebP, and others
- [ ] **Export** — Save metadata to JSON/CSV
- [ ] **Automated tests** — Test suite with pytest or unittest
- [ ] **CI/CD** — Continuous integration with GitHub Actions
- [ ] **Packaging** — Publish to PyPI or provide a standalone binary

---

## 📄 Licença / License

MIT © [KauaRios](kauarios49@gmail.com)

Este projeto está licenciado sob a licença MIT — veja o arquivo [LICENSE](LICENSE) para detalhes (se aplicável).

This project is licensed under the MIT license — see the [LICENSE](LICENSE) file for details (if applicable).

---

<div align="center">
  <sub>Feito com 💜 por KauaRios · Construído com Python e Pillow</sub>
  <br>
  <sub>Made with 💜 by KauaRios · Built with Python and Pillow</sub>
</div>
