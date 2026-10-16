#!/usr/bin/env python3
"""生成 Hello, World! 可视化横幅 (SVG)。

无第三方依赖，纯标准库。运行后会得到 hello_banner.svg，
可在 README 中直接以图片形式嵌入，作为本仓库的"可视化"产物。

用法:
    python visualize.py
"""

OUTPUT = "hello_banner.svg"
VERSION = "v0.2.0"
ORG = "华中科技大学数字社会研究中心"


def build_svg() -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="360" viewBox="0 0 800 360" font-family="-apple-system, 'Segoe UI', 'Microsoft YaHei', sans-serif">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#1f6feb"/>
      <stop offset="100%" stop-color="#6e40c9"/>
    </linearGradient>
  </defs>
  <rect width="800" height="360" rx="24" fill="url(#bg)"/>
  <text x="400" y="158" text-anchor="middle" font-size="58" font-weight="700" fill="#ffffff">Hello, World!</text>
  <text x="400" y="214" text-anchor="middle" font-size="22" fill="#dbeafe">Git 工作流可视化演示 · {VERSION}</text>
  <text x="400" y="288" text-anchor="middle" font-size="20" fill="#e9d5ff">{ORG}</text>
</svg>
'''


def main() -> None:
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(build_svg())
    print(f"已生成 {OUTPUT}（{VERSION} · {ORG}）")


if __name__ == "__main__":
    main()
