#!/usr/bin/env python3
import sys
from datetime import datetime

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

from league_client_api import _auto_detect_token_port
from lobby_manager import LobbyManager


def log(msg: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")


def main():
    log("롤 클라이언트 감지 중...")
    token, port = _auto_detect_token_port()
    if not token or not port:
        log("롤 클라이언트를 찾을 수 없습니다. 롤을 실행한 뒤 다시 시도하세요.")
        sys.exit(1)

    log(f"연결됨 (port={port})")

    lobby = LobbyManager(token, port)

    log("감시 시작 (종료: Ctrl+C)")
    try:
        lobby.start(poll_interval=2.0, log_fn=log)
    except Exception as e:
        log(f"[오류] 비정상 종료: {e}")


if __name__ == "__main__":
    main()
