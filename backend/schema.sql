CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    location TEXT NOT NULL,          -- where it was lost or found
    date TEXT NOT NULL,
    photo_url TEXT,
    finder_id TEXT,
    question TEXT                    -- the finder's verification question
);
