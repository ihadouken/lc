class Codec:
    def __init__(self):
        # Hashmaps to store mappings between long and short urls.
        self.encode_map = {}
        self.decode_map = {}
        self.base = 'http://tinyurl.com/'

        # Custom base62 charset to encode urls. Every character has an integer
        # identifier.
        self.charset = {}

        # 0-9 (10 characters)
        for i in range(0, 10):
            self.charset[i] = str(i)
        val = i

        # a-z (26 characters)
        for i in range(ord('a'), ord('z')+1):
            self.charset[val] = chr(i)
            val += 1

        # A-Z (26 characters)
        for i in range(ord('A'), ord('Z')+1):
            self.charset[val] = chr(i)
            val += 1

        self.charset_size = val

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_map:
            # Get the next available short url via the size of the Hashmap.
            # When the mapsize exceeds 9, use the lowercase alphabets. After
            # exceeding 35, use the uppercase alphabets. After we exhaust all
            # characters in the charset for a position, we increment the
            # position to its left by 1 and reset the position to the first
            # character i.e. '0'. If a position doesn't exist, it implicitly
            # means that it contains the first i.e. '0' character.
            mapsize = len(self.encode_map) + 1
            shortUrl = []

            # Use the order of appearance of a url to encode it. Example:
            # 1st url = '1', 2nd url = '2', ... 60th url = 'z', 61th url = '10'
            # and so on.
            while mapsize:
                shortUrl.append(self.charset[mapsize % self.charset_size])
                mapsize //= self.charset_size

            shortUrl.reverse()
            shortUrl = ''.join(shortUrl)

            # Add the new mapping to the hashmaps.
            self.encode_map[longUrl] = shortUrl
            self.decode_map[shortUrl] = longUrl

        return self.base + self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        # Remove base url and get the original long url via decode_map.
        shortUrl = shortUrl.split('/')[-1]
        return self.decode_map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
