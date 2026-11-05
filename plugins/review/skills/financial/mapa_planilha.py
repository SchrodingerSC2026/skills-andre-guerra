"""Mapa de uma planilha para a /financial-review: tem fórmula? de onde cada fórmula puxa?

Só lê, e lê uma CÓPIA em pasta temporária: a planilha pode estar aberta no Excel ou já
entregue a alguém, e a revisão nunca grava nela.

Uso: python mapa_planilha.py <planilha>   (imprime o JSON)
"""
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

from openpyxl import load_workbook

# 'Aba com espaço'!A1 | Aba!$A$1 | A1:B9 ; a aba é opcional
_REF = re.compile(
    r"(?:(?P<aba>'[^']+'|[A-Za-z_][\w.]*)!)?"
    r"(?P<cel>\$?[A-Z]{1,3}\$?\d+(?::\$?[A-Z]{1,3}\$?\d+)?)"
)
_TEXTO = re.compile(r'"[^"]*"')


def _referencias(formula: str, aba: str) -> list[str]:
    sem_texto = _TEXTO.sub('""', formula)
    refs = []
    for m in _REF.finditer(sem_texto):
        inicio = m.start()
        # pula nome de função colado (ex.: LOG10) e pedaço de identificador
        if inicio > 0 and (sem_texto[inicio - 1].isalnum() or sem_texto[inicio - 1] == "_"):
            continue
        dona = m.group("aba") or (f"'{aba}'" if " " in aba else aba)
        ref = f"{dona}!{m.group('cel').replace('$', '')}"
        if ref not in refs:
            refs.append(ref)
    return refs


def mapear(caminho: Path) -> dict:
    pasta = Path(tempfile.mkdtemp())
    try:
        copia = pasta / Path(caminho).name
        shutil.copyfile(caminho, copia)
        wb = load_workbook(copia, read_only=True, data_only=False)
        abas, dependencias = {}, {}
        for ws in wb.worksheets:
            formulas = valores = linhas = 0
            for linha in ws.iter_rows():
                linhas += 1
                for c in linha:
                    v = c.value
                    if v is None:
                        continue
                    if isinstance(v, str) and v.startswith("="):
                        formulas += 1
                        dependencias[f"{ws.title}!{c.coordinate}"] = _referencias(v, ws.title)
                    else:
                        valores += 1
            abas[ws.title] = {"formulas": formulas, "valores": valores, "linhas": linhas}
        wb.close()
        tipo = "formula" if any(a["formulas"] for a in abas.values()) else "valor"
        return {"tipo": tipo, "abas": abas, "dependencias": dependencias}
    finally:
        shutil.rmtree(pasta, ignore_errors=True)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(mapear(Path(sys.argv[1])), ensure_ascii=False, indent=1))
