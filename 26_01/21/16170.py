from datetime import datetime, timezone

now = datetime.now(timezone.utc)
print(now.year)
print(f"{now.month:02d}")
print(f"{now.day:02d}")
