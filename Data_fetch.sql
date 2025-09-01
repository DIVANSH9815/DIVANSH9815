DROP TABLE IF EXISTS users;

-- 2) Naya table banao
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
);

-- 3) Kuch dummy data insert karo
INSERT INTO users (username, password) VALUES 
('admin', 'admin123'),
('testuser', 'test@456'),
('divansh', 'mysecurepass');

-- 4) Data check karo
SELECT * FROM users;

-- 5) Username aur password ek sath dekhne ke liye (jaise tumne chaha tha)
SELECT username || '=' || password AS user_info FROM users LIMIT 3;
