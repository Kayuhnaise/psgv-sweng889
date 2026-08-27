from app import generate_wordcloud, load_report


def test_load_report(tmp_path):
    report = tmp_path / "sample.txt"
    report.write_text(
        "AI assists software engineering.",
        encoding="utf-8"
    )

    text = load_report(report)

    assert text == "AI assists software engineering."

def test_generate_wordcloud_creates_output_file(tmp_path):
    output = tmp_path / "wordcloud.png"

    generate_wordcloud("docker software engineering testing", output)

    assert output.exists()
    assert output.stat().st_size > 0
    assert output.read_bytes().startswith(b"\x89PNG")