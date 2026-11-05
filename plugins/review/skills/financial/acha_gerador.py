"""Acha o script que gera uma planilha, para a /review:financial.

Procura o nome do arquivo e o radical sem extensão (gerador costuma montar f"{nome}.xlsx")
em todo *.py sob a raiz, pulando as pastas da fonte única de exclusões do workspace.
Avisa quando o script é mais novo que a planilha: o código revisado pode não ser o que
gerou o entregável.

Uso: python acha_gerador.py <planilha> <raiz>   (imprime o JSON)
"""
import ast
import fnmatch
import json
import sys
from datetime import datetime
from pathlib import Path

# Fonte única de exclusões do workspace, se ele tiver uma: scripts/exclusoes_comuns.py na raiz
# informada ou numa pasta acima dela. None = procurar; os testes trocam por um caminho fixo.
FONTE_EXCLUSOES = None
# projeto encerrado costuma morar numa pasta "antigos", e gerador de lá não é o vigente
PASTAS_EXTRA = {"antigos"}
# usada só onde o workspace não tem fonte única de exclusões
PASTAS_PADRAO = {
    ".venv", "venv", "node_modules", "__pycache__", ".git", ".claude", "graphify-out",
    "_backups_projeto", "_quarentena_faxina", "ferramentas", "dist", ".next", "_wt_*", "_perfil_*",
}


def _fonte_exclusoes(raiz: Path) -> Path:
    if FONTE_EXCLUSOES is not None:
        return Path(FONTE_EXCLUSOES)
    for pasta in (raiz, *raiz.parents):
        candidata = pasta / "scripts" / "exclusoes_comuns.py"
        if candidata.exists():
            return candidata
    return raiz / "scripts" / "exclusoes_comuns.py"


def _pastas_puladas(raiz: Path) -> set[str]:
    # Lê PASTAS_DESCARTAVEIS sem executar o arquivo: ele mora no workspace revisado, que pode ser
    # de terceiros. Só literal (dict, set, list, tuple) é aceito; qualquer outra forma cai no padrão.
    fonte = _fonte_exclusoes(raiz)
    if not fonte.exists():
        return PASTAS_PADRAO | PASTAS_EXTRA
    try:
        arvore = ast.parse(fonte.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError, OSError):
        return PASTAS_PADRAO | PASTAS_EXTRA
    for no in arvore.body:
        if isinstance(no, ast.Assign) and any(getattr(t, "id", None) == "PASTAS_DESCARTAVEIS" for t in no.targets):
            try:
                valor = ast.literal_eval(no.value)
            except ValueError:
                break
            if isinstance(valor, (dict, set, list, tuple)) and all(isinstance(v, str) for v in valor):
                return set(valor) | PASTAS_EXTRA
            break
    return PASTAS_PADRAO | PASTAS_EXTRA


def _pulada(partes: tuple[str, ...], padroes: set[str]) -> bool:
    return any(fnmatch.fnmatch(p, padrao) for p in partes for padrao in padroes)


def candidatos(planilha: Path, raiz: Path) -> list[dict]:
    planilha, raiz = Path(planilha), Path(raiz)
    padroes = _pastas_puladas(raiz)
    nomes = (planilha.name, planilha.stem)
    mtime_planilha = planilha.stat().st_mtime
    achados = []
    for script in raiz.rglob("*.py"):
        rel = script.relative_to(raiz)
        if _pulada(rel.parts[:-1], padroes):
            continue
        texto = script.read_text(encoding="utf-8", errors="replace")
        if not any(n in texto for n in nomes):
            continue
        for i, linha in enumerate(texto.splitlines(), start=1):
            if any(n in linha for n in nomes):
                mtime = script.stat().st_mtime
                achados.append({
                    "script": rel.as_posix(),
                    "linha": i,
                    "trecho": linha.strip(),
                    "mtime_script": datetime.fromtimestamp(mtime).strftime("%d/%m/%Y %H:%M"),
                    "mais_novo_que_planilha": mtime > mtime_planilha,
                })
                break
    return sorted(achados, key=lambda a: a["script"])


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    print(json.dumps(candidatos(Path(sys.argv[1]), Path(sys.argv[2])), ensure_ascii=False, indent=1))
