from threading import Thread
from .scheduler import start_scheduler
from . import dashboard


def main() -> None:
    scheduler_thread = Thread(target=start_scheduler, daemon=True)
    scheduler_thread.start()
    dashboard.render()


if __name__ == "__main__":
    main()
