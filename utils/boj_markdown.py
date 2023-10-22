"""
BOJ.md line generator
"""
import sys
import os
import argparse
import requests
import json

BOJ = "https://www.acmicpc.net"
ENDPOINT = "https://solved.ac/api/v3"
parser = argparse.ArgumentParser()
parser.add_argument("--problem", type=int, help="problem id")
args = parser.parse_args()


def get_problem_info(
        problem_id: int,
    ) -> str | None:
    """
    Get problem info from solved.ac
    """
    url = f"{ENDPOINT}/problem/show?problemId={problem_id}"
    response = json.loads(requests.get(
        url=url
    ).content)
    if not isinstance(response, dict):
        return None
    if (title := response.get("titleKo")) is None:
        return None
    # TODO: DATE and RATE of contirbution are not supported fileds in solved.ac API
    return f"[BOJ {problem_id} {title}]({BOJ}/problem/{problem_id}) - Solved at [DATE], rated [RATE]"


if __name__ == "__main__":
    pID = args.problem
    if pID is None:
        print("Problem ID is required!", flush=True)
        pID = int(input("Problem ID: "))
    if (info := get_problem_info(pID)) is None:
        print("Problem not found!", flush=True)
        sys.exit(1)
    print(info, flush=True)
