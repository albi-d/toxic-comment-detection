def get_severity(proba_toxic: float):
    """
    Tentukan tingkat keparahan berdasarkan probabilitas toxic (0.0 – 1.0).

    Returns: dict dengan keys: level, label, emoji, color, bg, border, desc
    """
    pct = proba_toxic * 100

    if pct < 40:
        return {
            "level"  : "aman",
            "label"  : "AMAN",
            "emoji"  : "✅",
            "color"  : "#16a34a",
            "bg"     : "#f0fdf4",
            "border" : "#86efac",
            "badge_bg": "#dcfce7",
            "badge_color": "#15803d",
            "desc"   : "Komentar ini tidak mengandung bahasa kasar",
        }
    elif pct < 70:
        return {
            "level"  : "perhatian",
            "label"  : "PERLU PERHATIAN",
            "emoji"  : "⚠️",
            "color"  : "#d97706",
            "bg"     : "#fffbeb",
            "border" : "#fcd34d",
            "badge_bg": "#fef3c7",
            "badge_color": "#b45309",
            "desc"   : "Komentar ini berpotensi mengandung bahasa yang kurang sopan",
        }
    else:
        return {
            "level"  : "toxic",
            "label"  : "SANGAT TOXIC",
            "emoji"  : "🚨",
            "color"  : "#dc2626",
            "bg"     : "#fff5f5",
            "border" : "#fca5a5",
            "badge_bg": "#fee2e2",
            "badge_color": "#b91c1c",
            "desc"   : "Komentar ini terdeteksi mengandung bahasa kasar yang kuat",
        }


def severity_label(proba_toxic: float) -> str:
    """Shortcut — hanya return label string."""
    return get_severity(proba_toxic)["label"]
