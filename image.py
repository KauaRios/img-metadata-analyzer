from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import os
import sys

# ── Paleta ANSI ──────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"

PURPLE  = "\033[38;5;135m"   # roxo principal
MAGENTA = "\033[38;5;201m"   # magenta brilhante
CYAN    = "\033[38;5;117m"   # ciano suave
WHITE   = "\033[38;5;255m"   # branco
GRAY    = "\033[38;5;240m"   # cinza escuro
RED     = "\033[38;5;196m"   # vermelho erro
YELLOW  = "\033[38;5;220m"   # amarelo aviso
GREEN   = "\033[38;5;114m"   # verde ok

# ── Helpers visuais ──────────────────────────────────────────
W = 54  # largura do box

def banner():
    linhas = [
        f"{MAGENTA}{'▀' * W}{RESET}",
        f"{MAGENTA}█{RESET}{' ' * (W - 2)}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{'  ' + PURPLE + BOLD}██╗███╗   ███╗ █████╗  ██████╗{RESET}{' ' * 5}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{'  ' + PURPLE + BOLD}██║████╗ ████║██╔══██╗██╔════╝{RESET}{' ' * 5}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{'  ' + PURPLE + BOLD}██║██╔████╔██║███████║██║  ███╗{RESET}{' ' * 4}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{'  ' + PURPLE + BOLD}██║██║╚██╔╝██║██╔══██║██║   ██║{RESET}{' ' * 4}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{'  ' + PURPLE + BOLD}██║██║ ╚═╝ ██║██║  ██║╚██████╔╝{RESET}{' ' * 4}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{'  ' + PURPLE + BOLD}╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ {RESET}{' ' * 4}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{' ' * (W - 2)}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{CYAN}{BOLD}{'  Image Analyser  ·  OSINT Edition':^{W-2}}{RESET}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{GRAY}{'  v1.0  ·  by KauaRios':^{W-2}}{RESET}{MAGENTA}█{RESET}",
        f"{MAGENTA}█{RESET}{' ' * (W - 2)}{MAGENTA}█{RESET}",
        f"{MAGENTA}{'▄' * W}{RESET}",
    ]
    print()
    for l in linhas:
        print(l)
    print()

def secao(titulo):
    bar = f"{PURPLE}┌{'─' * (W - 2)}┐{RESET}"
    tit = f"{PURPLE}│{RESET} {MAGENTA}{BOLD}{titulo}{RESET}"
    pad = W - 2 - len(titulo) - 1
    tit += " " * pad + f"{PURPLE}│{RESET}"
    sep = f"{PURPLE}├{'─' * (W - 2)}┤{RESET}"
    print(bar)
    print(tit)
    print(sep)

def linha(chave, valor, cor_val=WHITE):
    chave_fmt = f"{CYAN}{chave:<20}{RESET}"
    valor_fmt = f"{cor_val}{valor}{RESET}"
    conteudo = f" {chave_fmt} {valor_fmt}"
    print(f"{PURPLE}│{RESET}{conteudo}")

def rodape():
    print(f"{PURPLE}└{'─' * (W - 2)}┘{RESET}\n")

def aviso(msg):
    print(f"\n{YELLOW}  ⚠  {msg}{RESET}\n")

def erro(msg):
    print(f"\n{RED}  ✖  {msg}{RESET}\n")

def ok(msg):
    print(f"{GREEN}  ✔  {msg}{RESET}")

# ── Lógica principal ─────────────────────────────────────────
CAMINHO = "Imagens/image.jpg"


def informacoes_basicas(imagem):
    secao(" INFORMAÇÕES BÁSICAS")
    linha("Arquivo",   os.path.basename(imagem.filename))
    linha("Formato",   imagem.format or "Desconhecido")
    linha("Dimensões", f"{imagem.size[0]} x {imagem.size[1]} px")
    linha("Modo",      imagem.mode)

    tam = os.path.getsize(imagem.filename)
    if tam >= 1_048_576:
        linha("Tamanho", f"{tam / 1_048_576:.2f} MB")
    else:
        linha("Tamanho", f"{tam / 1024:.1f} KB")
    rodape()


def extrair_exif(imagem):
    exif = imagem.getexif()
    if not exif:
        return False

    secao(" DADOS EXIF")
    for tag_id, valor in exif.items():
        tag_nome = TAGS.get(tag_id, f"Tag_{tag_id}")

        if tag_nome == "GPSInfo" and isinstance(valor, dict):
            linha("GPSInfo", "→ ver seção GPS abaixo", YELLOW)
        else:
            val_str = str(valor)
            if len(val_str) > 45:
                val_str = val_str[:45] + "…"
            linha(tag_nome, val_str)
    rodape()

    # GPS separado
    for tag_id, valor in exif.items():
        if TAGS.get(tag_id) == "GPSInfo" and isinstance(valor, dict):
            secao(" GPS")
            lat = lon = None
            lat_ref = lon_ref = ""
            dados = {}
            for gps_id, gps_val in valor.items():
                nome = GPSTAGS.get(gps_id, f"GPS_{gps_id}")
                dados[nome] = gps_val
                linha(nome, str(gps_val), GREEN)

            # Monta link Google Maps
            if "GPSLatitude" in dados and "GPSLongitude" in dados:
                def to_deg(d):
                    return d[0] + d[1] / 60 + d[2] / 3600

                lat = to_deg(dados["GPSLatitude"])
                lon = to_deg(dados["GPSLongitude"])
                if dados.get("GPSLatitudeRef") == "S":  lat = -lat
                if dados.get("GPSLongitudeRef") == "W": lon = -lon
                maps_url = f"https://maps.google.com/?q={lat:.6f},{lon:.6f}"
                linha("Google Maps", maps_url, MAGENTA)
            rodape()

    return True


def extrair_png_metadata(imagem):
    info = imagem.info
    if not info:
        return False
    secao(" METADADOS PNG")
    for chave, valor in info.items():
        val_str = str(valor)
        if len(val_str) > 45:
            val_str = val_str[:45] + "…"
        linha(chave, val_str)
    rodape()
    return True


def main():
    banner()

    try:
        imagem = Image.open(CAMINHO)
    except FileNotFoundError:
        erro(f"Arquivo não encontrado: {CAMINHO}")
        sys.exit(1)
    except Exception as e:
        erro(f"Não foi possível abrir a imagem: {e}")
        sys.exit(1)

    ok(f"Arquivo carregado → {CAMINHO}\n")

    informacoes_basicas(imagem)

    tem_exif = extrair_exif(imagem)

    tem_png = False
    if imagem.format == "PNG":
        tem_png = extrair_png_metadata(imagem)

    if not tem_exif and not tem_png:
        aviso("Nenhum metadado encontrado.")
        aviso("Imagens enviadas por WhatsApp têm metadados removidos.")
        aviso("Transfira por cabo USB ou Google Fotos para preservar EXIF.")

    print(f"{GRAY}{'─' * W}{RESET}")
    print(f"{GRAY}  análise concluída.{RESET}\n")


if __name__ == "__main__":
    main()