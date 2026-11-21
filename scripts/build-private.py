"""Build the read-only REA deployment. Requires Python 3 and Pandoc."""
from html import escape
from pathlib import Path
import re
from shutil import copy2, copytree, rmtree
from subprocess import run

root = Path(__file__).resolve().parents[1]
dist = root / "dist"
documents = (
    "FICHA-TECNICA", "LICENCIAMENTO", "CREDITOS-E-REFERENCIAS",
    "PRIVACIDADE", "TERMOS-DE-USO", "ACESSIBILIDADE",
    "REGISTRO-DE-FONTES-E-LICENCAS", "COMO-CITAR", "AUDITORIA-DE-PENDENCIAS",
    "GUIA-DE-PREENCHIMENTO", "GUIA-DE-EDICAO", "GUIA-DE-VALIDACAO-FINAL", "MODELO-DE-AUTORIZACAO",
)
if dist.exists():
    rmtree(dist)
dist.mkdir()
for name in ("index.html", "404.html", "palacio-trigonometrico.html", "favicon.ico", "CITATION.cff", "sitemap.xml"):
    copy2(root / name, dist / name)
for name in ("assets", "conteudos", "estudar", "explorar", "jogar", "jogos", "materiais", "praticar", "professores", "sobre"):
    copytree(root / name, dist / name)
(dist / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")

def document_link(match):
    name = match[1]
    if name not in documents:
        raise ValueError(f"Documento não incluído na edição de consulta: {name}")
    return f'href="{name.lower()}.html"'

docs_dir = dist / "documentos"
docs_dir.mkdir()
for filename in ("index.html", "historico-trigtest-46c1ea4.zip"):
    copy2(root / "documentos" / filename, docs_dir / filename)
for name in documents:
    source = root / "documentos" / f"{name}.md"
    title = escape(source.read_text(encoding="utf-8").splitlines()[0].removeprefix("# "))
    rendered = run(
        ["pandoc", "--from=gfm-raw_html", "--to=html5", "--wrap=none", str(source)],
        check=True, capture_output=True, text=True, encoding="utf-8",
    ).stdout
    rendered = re.sub(r'href="([A-Z-]+)\.md"', document_link, rendered)
    rendered = rendered.replace('href="../CITATION.cff"', 'href="../CITATION.cff" download')
    rendered = rendered.replace("@@@@", '<span class="token">@@@@</span>')
    rendered = rendered.replace("<table>", '<div class="document-table" tabindex="0" role="region" aria-label="Tabela com rolagem horizontal"><table>').replace("</table>", "</table></div>")
    (docs_dir / f"{name.lower()}.html").write_text(f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex,nofollow">
  <title>{title} | TrigPure Interative</title>
  <link rel="icon" href="../assets/logo-trigonometria.svg" type="image/svg+xml">
  <link rel="stylesheet" href="../assets/rea.css">
</head>
<body>
<a class="skip-link" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header"><div class="wrap header-row">
  <a class="brand" href="../index.html"><img class="brand-logo" src="../assets/logo-trigonometria.svg" width="42" height="42" alt=""><span>TrigPure <small>Interative</small></span></a>
</div></header>
<main id="conteudo" class="wrap document-page">
  <nav aria-label="Localização no site"><a href="../sobre/index.html">Sobre</a> / <a href="index.html">Documentos</a></nav>
  <article>
{rendered}  </article>
  <a class="btn btn-primary" href="index.html">Voltar aos documentos</a>
</main>
</body>
</html>
""", encoding="utf-8")
