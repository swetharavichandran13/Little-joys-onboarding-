# Little Joys onboarding: animated cover-flow prototype

Automatically playing, landscape (1920 x 1080, 30 fps) walkthrough of the nine-screen Little Joys onboarding,
looped three times, built from the exported Figma screens.

## Preview in a browser
Open `index.html` in Chrome or Edge. It plays automatically and loops. No build step.

## Adjust timings
Everything is in the `CFG` block at the top of `index.html`: screen hold times, cover-flow speed and scale,
blink timing, gummy jumps, age-picker keyframes, scroll keyframes (Screens 4 and 7),
carousel tap times (Screens 5 and 6), and the annotation copy (`LAB`).

## Render the MP4
```
pip install playwright numpy opencv-python-headless scipy
playwright install chromium
python3 render.py 2        # 2 = number of parallel workers; needs ffmpeg
```
Output: `LittleJoys_onboarding_landscape.mp4` (not committed; it is large).

## Rebuild the cut-out assets (optional)
`prep_all.py` regenerates `a/` and `b/` (eyelid patches, gummies, age-picker pieces, carousel slides, scroll pages)
from the original Figma exports. Edit the `U` path at the top to point at your exports.

## Notes
- Screen 6 first slide uses the corrected export (first indicator dot active).
- Carousels use the three supplied slides each; the indicators show four dots, so a fourth slide is still missing.
- `archive_index_before_refinement.html` is the previous version, kept for reference.
