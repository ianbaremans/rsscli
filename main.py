import feedparser
import argparse
import webbrowser

# parsing the arguments
parser = argparse.ArgumentParser(description="How to use rsscli:")
parser.add_argument("articles", metavar="L", type=int, nargs="+",
        help="An integer to specify the amount of articles displayed")
parser.add_argument("feed", metavar="F", type=str,
        help="A string which contains the feed url")

args = parser.parse_args()

feed = feedparser.parse(args.feed)
articles = args.articles[0]

for i in range(0, articles):
    print(feed.entries[i].title+": "+feed.entries[i].link)
    # TODO: make the titles clickable links

