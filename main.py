import feedparser
import argparse

# parsing the arguments
parser = argparse.ArgumentParser(description="How to use rsscli:")
parser.add_argument("articles", metavar="L", type=int, nargs="+",
        help="An integer to specify the amount of articles displayed")
parser.add_argument("feed", metavar="F", type=str,
        help="A string which contains the feed url")

args = parser.parse_args()
print(args.accumulate())

feed = feedparser.parse("https://news.ycombinator.com/rss")
print(feed.entries[0].link)

