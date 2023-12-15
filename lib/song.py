from config import CONN, CURSOR

class Song:
    # instantiate the class
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
        
    # define class method to create table
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        
        # execute the statement
        CURSOR.execute(sql)
        
    # method to save a song instance to the table
    def save(self):
        sql = """
            INSERT INTO songs (name, album) 
            VALUES (?, ?)
        """
        
        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()
        
        # grab the ID of newly inserted row and assign it to be the value of id attribute
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        
    # method to create a new Song instance and save it
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song