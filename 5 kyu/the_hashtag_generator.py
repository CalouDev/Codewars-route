generate_hashtag = lambda s: "#" + s.title().replace(" ", "") if s != "" and len(s) < 140 else False
