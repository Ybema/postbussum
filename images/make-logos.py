import os

brands = [
    ("philips-hue", "Philips Hue", "#1C1C1C", "#FFFFFF"),
    ("gira", "Gira", "#000000", "#FFFFFF"),
    ("jung", "Jung", "#E2001A", "#FFFFFF"),
    ("busch-jaeger", "Busch-Jaeger", "#003DA5", "#FFFFFF"),
    ("abb", "ABB", "#FF000F", "#FFFFFF"),
    ("eglo", "Eglo", "#0066B2", "#FFFFFF"),
    ("steinhauer", "Steinhauer", "#4A4A4A", "#FFFFFF"),
    ("highlight", "Highlight", "#222222", "#FFFFFF"),
    ("romi", "It's about RoMi", "#B8860B", "#FFFFFF"),
    ("good-mojo", "Good MoJo", "#2E8B57", "#FFFFFF"),
    ("lucide", "Lucide", "#1A1A1A", "#FFFFFF"),
    ("trio", "Trio Lighting", "#333399", "#FFFFFF"),
    ("freelight", "Freelight", "#333333", "#FFFFFF"),
    ("holtkotter", "Holtkötter", "#1A1A1A", "#FFFFFF"),
    ("masterlight", "Masterlight", "#8B0000", "#FFFFFF"),
    ("present-time", "Present Time", "#333333", "#FFFFFF"),
    ("artisans", "Artisans", "#5C3317", "#FFFFFF"),
]

for slug, name, bg, fg in brands:
    width = max(140, len(name) * 9 + 40)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="44" viewBox="0 0 {width} 44">
  <rect width="{width}" height="44" rx="4" fill="{bg}"/>
  <text x="{width//2}" y="27" font-family="Arial,sans-serif" font-size="13" font-weight="700" fill="{fg}" text-anchor="middle" letter-spacing="0.5">{name}</text>
</svg>'''
    with open(f"brand-{slug}.svg", "w") as f:
        f.write(svg)
    print(f"Created brand-{slug}.svg")

print("Done")
