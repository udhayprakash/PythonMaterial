import argparse
import asyncio
import itertools
import pprint
from decimal import Decimal
from typing import List, Tuple

import httpx

YAHOO_FINANCE_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}"


async def fetch_price(ticker: str, client: httpx.AsyncClient) -> Tuple[str, Decimal]:
    print(f"Making request for {ticker} price")
    response = await client.get(YAHOO_FINANCE_URL.format(ticker))
    print(f"Received results for {ticker}")
    price = response.json()["chart"]["result"][0]["meta"]["regularMarketPrice"]
    return ticker, Decimal(price).quantize(Decimal("0.01"))


async def fetch_all_prices(tickers: List[str]) -> List[Tuple[str, Decimal]]:
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(
            *map(
                fetch_price,
                tickers,
                itertools.repeat(client),
            )
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--tickers",
        nargs="+",
        help="List of tickers separated by a space",
        required=True,
    )
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(fetch_all_prices(args.tickers))
    pprint.pprint(result)


# USAGE:
# py o_async_requests.py -t VTSAX VTIAX IJS VSS AAPL ORCL GOOG MSFT FB
