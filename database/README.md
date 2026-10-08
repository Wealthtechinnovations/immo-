# Database

Migrations are ordered and transactional where PostgreSQL permits. Production execution requires backup/restore procedure and migration runner selected later. Rollbacks are development aids, not a substitute for backup. No destructive automatic rollback in production.
