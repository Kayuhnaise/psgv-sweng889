from pathlib import Path
from app import load_report
import app

def test_load_report(tmp_path):
    report = tmp_path / "sample.txt"
    report.write_text(
        "AI assists software engineering.",
        encoding="utf-8"
    )

    text = load_report(report)

    assert text == "AI assists software engineering."



def test_main_creates_wordcloud_file(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    report = tmp_path / "report.txt"
    report.write_text("AI assists software engineering.", encoding="utf-8")

    app.main()

    output_file = tmp_path / "output" / "wordcloud.png"
    assert output_file.exists()
    assert output_file.stat().st_size > 0

    captured = capsys.readouterr()
    assert "Word cloud created: output/wordcloud.png" in captured.out