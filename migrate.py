import database


def migrate():
    database.init_db()
    conn = database.get_db_connection()
    try:
        approved_count = conn.execute(
            "SELECT COUNT(*) FROM fondas WHERE status = 'approved'"
        ).fetchone()[0]
        print(f"Migracion completada: {approved_count} fondas aprobadas disponibles.")
    finally:
        conn.close()


if __name__ == "__main__":
    migrate()
