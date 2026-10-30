"""Construye las páginas a partir de la plantilla y el JSON del banco.

Uso: python3 tools/build.py
Genera:
  dist/a320-qbank.html  -> página autónoma (abrir con doble clic, datos embebidos)
  dist/artifact.html    -> fragmento para publicar como Artifact de claude.ai
"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
tpl = open(os.path.join(root, 'src', 'app.template.html'), encoding='utf-8').read()
data = json.load(open(os.path.join(root, 'data', 'a320_dgac_qbank.json'), encoding='utf-8'))
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
frag = tpl.replace('/*__DATA__*/null', blob)
os.makedirs(os.path.join(root, 'dist'), exist_ok=True)
open(os.path.join(root, 'dist', 'artifact.html'), 'w', encoding='utf-8').write(frag)
head, body = frag.split('<header', 1)
page = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        + head + '</head>\n<body>\n<header' + body + '\n</body>\n</html>\n')
open(os.path.join(root, 'dist', 'a320-qbank.html'), 'w', encoding='utf-8').write(page)
print('ok', len(frag)//1024, 'KB')
