import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_search_index_matches_glossary_anchors() -> None:
    glossary = (ROOT / "GLOSSARY.md").read_text(encoding="utf-8")
    html = (ROOT / "docs" / "glossary.html").read_text(encoding="utf-8")
    anchors = set(re.findall(r'<a id="([^"]+)"', glossary))
    raw = html.split('<script type="application/json" id="glossary-index">', 1)[1]
    raw = raw.split("</script>", 1)[0]
    indexed = {item["id"] for item in json.loads(raw)}
    assert indexed == anchors
    assert "desk.py" not in html
    assert "launch.bat" not in html
    assert "(glossary.html)" not in glossary
    assert "https://htmlpreview.github.io/?https://raw.githubusercontent.com/pedramgoshATgmail/EVALATHAN/main/docs/glossary.html" in glossary
    assert 'id="archly"' in html
    assert "assets/glossary/archly.png" in html
    assert "Rubric stem" in html
    assert "GLOSSARY.md#user-content-" not in html
    assert "scrollIntoView" in html
