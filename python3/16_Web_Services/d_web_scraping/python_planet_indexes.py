from bs4 import BeautifulSoup
from security import safe_requests


def main():
    resp = safe_requests.get("http://planetpython.org", timeout=60)

    soup = BeautifulSoup(resp.text)

    sources = soup.find_all("h3", {"class": "post"})
    titles = [source.find_next_sibling("h4").text for source in sources]
    dates = [
        d.text
        for d in soup.select("p em a")
        if (d.text.upper().endswith(" AM") or d.text.upper().endswith(" PM"))
    ]

    for i, (s, t, d) in enumerate(zip(sources, titles, dates), 1):
        print(f"{i} - {s.text}\n{t}\n{d}\n")


if __name__ == "__main__":
    main()
