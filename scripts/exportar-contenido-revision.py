"""Exporta el desarrollo existente a TXT para revisión sin modificar sus fuentes."""

from html.parser import HTMLParser
from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]


class EditorialText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.in_article = False
        self.article_count = 0
        self.skip = 0
        self.parts = []
        self.counts = {"paragraphs": 0, "headings": 0, "list_items": 0}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and "content" in attrs.get("class", "").split():
            self.in_article = True
            self.article_count += 1
        if not self.in_article:
            return
        if tag in {"style", "script", "svg"}:
            self.skip += 1
        if self.skip:
            return
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
            self.counts["headings"] += 1
        elif tag in {"p", "blockquote", "figure", "figcaption", "div", "ul", "ol", "table"}:
            self.parts.append("\n\n")
            if tag == "p":
                self.counts["paragraphs"] += 1
        elif tag == "li":
            self.parts.append("\n- ")
            self.counts["list_items"] += 1
        elif tag == "tr":
            self.parts.append("\n")
        elif tag in {"th", "td"}:
            self.parts.append(" | ")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "img":
            self.parts.append("\n[Recurso gráfico: " + attrs.get("alt", attrs.get("src", "imagen")) + "]\n")

    def handle_endtag(self, tag):
        if not self.in_article:
            return
        if tag in {"style", "script", "svg"} and self.skip:
            self.skip -= 1
            return
        if self.skip:
            return
        if tag == "article":
            self.in_article = False
        elif tag in {"p", "h1", "h2", "h3", "h4", "h5", "h6", "figcaption", "div", "table"}:
            self.parts.append("\n\n")

    def handle_data(self, data):
        if self.in_article and not self.skip:
            self.parts.append(re.sub(r"\s+", " ", data))

    def output(self):
        text = "".join(self.parts)
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r" *\n *", "\n", text)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def main():
    blocks = [
        "GESTIÓN DE PROYECTOS ÁGILES\nContenido existente reunido para revisión\n\n"
        "Archivo auxiliar generado desde los cinco contenido.html. Conserva el desarrollo "
        "textual y el orden actual; no es una versión revisada ni un entregable final. "
        "Las listas se representan con guiones y las tablas con separadores. "
        "Las figuras conservan sus pies y las imágenes su descripción cuando existe. "
        "Los gráficos, su texto interno, enlaces y formato visual deben consultarse en las fuentes y el Word."
    ]
    inventory = []
    for number in range(1, 6):
        source = ROOT / "entregables" / f"MODULO {number}" / "Contenido" / "contenido.html"
        html = source.read_text(encoding="utf-8-sig")
        parser = EditorialText()
        parser.feed(html)
        parser.close()
        text = parser.output()
        if parser.article_count != 1 or not text:
            raise ValueError(f"Cuerpo editorial inválido en {source}")
        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
        title = re.sub(r"<[^>]*>", "", title_match[1]).strip() if title_match else "Contenido"
        blocks.append(f"MÓDULO {number}: {title}\nFuente: {source.relative_to(ROOT)}\n\n{text}")
        inventory.append({"module": number, "source": str(source.relative_to(ROOT)),
                          "words_in_export": len(text.split()), **parser.counts})
    target = ROOT / "CONTENIDO-COMPLETO-REVISION.txt"
    target.write_text("\n\n" + ("\n\n" + "=" * 72 + "\n\n").join(blocks) + "\n", encoding="utf-8")
    qa = ROOT / ".qa" / "revision-contenido"
    qa.mkdir(parents=True, exist_ok=True)
    (qa / "inventario-txt.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(target), "modules": inventory}, ensure_ascii=True))


if __name__ == "__main__":
    main()
