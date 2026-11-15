CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    found_at TEXT NOT NULL,          -- where it was lost or found (was: location)
    date TEXT NOT NULL,
    photo_url TEXT,
    finder_id TEXT,
    question TEXT                    -- the finder's verification question
);
