#stored procedure based id generation , inspired by instagram

#lets imagine instagram has 500 logical db shards inside each physical server

'''Example
create database insta2;

create table insta2.photos(
    id bigint not null default insta2.next_id(); <- next_id() is the stored procedure that will generate id inside the database
)

What is the advantage of generating ids inside a database? 
-> this is better than having auto incremental int ids because we can put our custom logic in

CREATE OR REPLACE FUNCTION 
    insta2.next_id(OUT result bigint) AS $$
Declare
    epoch bigint := 1672531200 //epoch utc for jan 1 2023
    counter bigint
    now_ms bigint
    shard_id := 2
BEGIN 
    -- Get the total row count from your existing table and increment by 1
    SET @counter := (SELECT COUNT(*) + 1 FROM my_database.pictures);
    
    now_ms := timestamp in ms (utc)
    result := (now_ms - epoch) << 23;
    result := result | (shared_id << 10);
    result := result | (counter)
END
'''

import mysql.connector
import time


# Step 1: Connect to the MySQL database
def connect_to_db():
    try:
        connection = mysql.connector.connect(
                host="localhost",
                user="my_user",
                password="my_password",
                database="my_database"
        )
        return connection
    except ValueError as e:
        print(str(e))
    

# Step 2: Write a stored procedure
def create_stored_procedure(connection):
    cursor = connection.cursor()
    
    procedure_id_query = """
      CREATE PROCEDURE next_id(OUT param1 BIGINT)
        BEGIN
            DECLARE epoch BIGINT DEFAULT 1672531200;
            DECLARE counter BIGINT;
            DECLARE now_ms BIGINT;
            SET @shard_id = 2;

            -- Simulate the 'NEXTVAL' function using a user-defined variable
            SET @counter := (SELECT COUNT(*) + 1 FROM my_database.pictures);

            SET now_ms = UNIX_TIMESTAMP(NOW(3)) * 1000;

            SET @result = (now_ms - epoch) << 23;
            SET @result = @result | (@shard_id << 10);
            SET @result = @result | @counter;
            -- Explicitly convert @result to SIGNED BIGINT
            SET @result = CAST(@result AS SIGNED);
            SET @result_decimal = CONV(@result, 2, 10);
            SET param1 = @result_decimal;
        END;
    """
    
    procedure_insert_query = """
        CREATE PROCEDURE insert_picture(IN p_url VARCHAR(255))
        BEGIN
            
            -- Call the function 'next_id' to generate the ID
            CALL next_id(@id);
            
            -- Insert the ID and URL into the pictures table
            INSERT INTO pictures (id, url) VALUES (@id, p_url);
        END
    """

    cursor.execute(procedure_id_query)
    cursor.execute(procedure_insert_query)
    connection.commit()
    cursor.close()

# Example usage:

def create_table(connection):
    cursor = connection.cursor()

    try:
        create_table_query = '''
       CREATE TABLE IF NOT EXISTS pictures (
            id BIGINT,
            url VARCHAR(255)
        );
        '''
        cursor.execute(create_table_query)
        connection.commit()
        print("Table 'pictures' created successfully.")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        connection.commit()
        cursor.close()


def insert_data(connection,p_url):
    cursor = connection.cursor()

    try:
        # Call the stored procedure 'insert_picture'
        cursor.callproc('insert_picture', [p_url])
        connection.commit()
        print("Data inserted successfully.")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        connection.commit()
        cursor.close()
        


try:
    connection = connect_to_db()
    
    # create_table(connection)
    # print("Tablee created successfully.")

    # create_stored_procedure(connection)
    # print("Stored procedure created successfully.")
    
    insert_data(connection,"vineet.com")
    insert_data(connection,"vineet2.com")
    insert_data(connection,"vineet3.com")

    if connection.is_connected():
        connection.close()

except mysql.connector.Error as error:
    print("Error: {}".format(error))


