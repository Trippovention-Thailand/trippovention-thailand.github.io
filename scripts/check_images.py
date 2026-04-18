"""Check that images referenced in HTML pages are accessible via HTTP."""
import urllib.request
import re

BASE = "http://127.0.0.1:8765"
PAGES = ["/index.html", "/destinations.html", "/packages/singapore/index.html",
         "/packages/india/goa/romantic_goa_sunset_escape.html"]

IMG_PATTERN = re.compile(r'src="([^"]*assets/images/[^"]+)"')


def main():
    for page in PAGES:
        html = urllib.request.urlopen(BASE + page).read().decode("utf-8")
        img_paths = IMG_PATTERN.findall(html)

        broken = 0
        for img_path in img_paths[:20]:
            clean = img_path
            page_dir = page.rsplit("/", 1)[0]
            if clean.startswith("../"):
                parts = page_dir.split("/")
                while clean.startswith("../"):
                    clean = clean[3:]
                    parts = parts[:-1]
                clean = "/".join(parts) + "/" + clean

            url = BASE + ("/" if not clean.startswith("/") else "") + clean
            try:
                code = urllib.request.urlopen(url).getcode()
                if code != 200:
                    broken += 1
                    print(f"  BROKEN {page} -> {img_path} ({code})")
            except Exception as e:
                broken += 1
                print(f"  BROKEN {page} -> {img_path} ({e})")

        print(f"{page}: {len(img_paths)} images found, {broken} broken")


if __name__ == "__main__":
    main()
