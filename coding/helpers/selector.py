# The MIT License (MIT)
# Copyright © 2024 Yuma Rao
# Copyright © 2023 Opentensor Foundation
# Copyright © 2024 Macrocosmos

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import random


class Selector:
    def __init__(self, seed=None):
        self.seed = seed
        self.rng = random.Random(seed)

    def __call__(self, items, weights=None):
        return self.rng.choices(items, weights=weights)[0]


class PageRankSelector(Selector):
    """Preferentially chooses the items at the top of the list, under the assumption that they are more important."""

    def __init__(self, seed=None, alpha=0.85):
        super().__init__(seed)
        self.alpha = alpha

    def __call__(self, items):
        weights = [self.alpha**i for i in range(len(items))]
        return self.rng.choices(items, weights=weights)[0]


class SimilaritySelector(Selector):
    """Chooses the item most similar to the query."""

    def __init__(self, seed=None, similarity_fn=None):
        super().__init__(seed)
        self.similarity_fn = similarity_fn

    def __call__(self, query, items):
        return max(items, key=lambda item: self.similarity_fn(query, item))


class TopSelector(Selector):
    """Chooses the top item."""

    def __init__(self, seed=None):
        super().__init__(seed)

    def __call__(self, items):
        return items[0]


if __name__ == "__main__":
    selector = Selector(seed=42)
    items = range(10)
    item = selector(items)

    assert item in items, "Selector should return one of the items"
