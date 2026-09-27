import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    return f"https://youtu.be/{video_id.group(1)}"  if (video_id := re.search(r"<iframe\b[^>]*?\bsrc\s*=\s*['\"]https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)", s)) else None


if __name__ == "__main__":
    main()
