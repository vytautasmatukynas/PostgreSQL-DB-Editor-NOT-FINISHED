import psycopg2

import prettytable

import sql_db

USER = "xxxx"
PSW = "1111"

while True:
    user = input("Enter user: ")
    psw = input("Enter password: ")

    params = sql_db.conn_postgre

    if user == f"{USER}" and psw == f"{PSW}":

        def print_table():
            try:
                while True:
                    question = input("\nDo you want to print table yes/no? Or quit?\n"
                                     "y/n/exit: ")

                    if question == "y":
                        table_name = input("\nEnter table name: ")

                        prettytable1 = prettytable.PrettyTable()

                        conn = psycopg2.connect(**params)
                        cur = conn.cursor()
                        cur.execute("""SELECT * FROM {} ORDER BY id""".format(table_name))
                        query = cur.fetchall()

                        list_headers = [i[0] for i in cur.description]
                        # print(list_headers)

                        prettytable1.field_names = list_headers
                        # print(list_headers)

                        for data in query:
                            list_data = list(data)
                            # print(list_data)
                            prettytable1.add_row(list_data)

                            print(prettytable1)

                        conn.close()

                        ask_action()
                        break

                    elif question == "n":
                        ask_action()
                        break

                    elif question == "exit":
                        quit()

                    else:
                        print("\nPlease enter valid selection.")
                        continue

            except:
                print("\nPlease enter valid name.\n")
                print_table()


        def delete_row():
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            question = input("\nDelete row? y/n: ")

            if question == "n":
                print_table()

            elif question == "y":
                table_name = input('\nIf you want to go back type "back", else - Enter table name: ')

                if table_name == "back":
                    print_table()

                else:
                    id_number = int(input('\nEnter ID number: '))

                    cur.execute("""DELETE FROM {} WHERE ID=%s""".format(table_name), (id_number,))
                    conn.commit()
                    conn.close()

            else:
                print("\nPlease enter valid selection")


        def add_row():
            print("\nNot yet... S0RRY AMIGO!")


        def alter_add_column():
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            question = input("\nAdd column? y/n: ")

            if question == "n":
                print_table()

            elif question == "y":
                table_name = input('\nIf you want to go back type "back", else - Enter table name: ')

                cur.execute("""SELECT * FROM {} ORDER BY id""".format(table_name))
                list_headers = [i[0] for i in cur.description]
                print(list_headers)

                column_name = input('\nIf you want to go back type "back", else - Enter column name: ')
                column_type = input('If you want to go back type "back", else - Enter column type: ').upper()

                if table_name == "back" or column_name == "back" or column_type == "back":
                    print_table()

                else:
                    cur.execute(
                        """ALTER TABLE {} ADD COLUMN IF NOT EXISTS {} {}""".format
                        (table_name, column_name, column_type))
                    conn.commit()
                    conn.close()

            else:
                print("\nPlease enter valid selection.")


        def alter_drop_column():
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            question = input("\nDelete column? y/n: ")

            if question == "n":
                print_table()

            elif question == "y":
                table_name = input('\nIf you want to go back type "back", else - Enter table name: ')

                cur.execute("""SELECT * FROM {} ORDER BY id""".format(table_name))
                list_headers = [i[0] for i in cur.description]
                print(list_headers)

                column_name = input('\nIf you want to go back type "back", else - Enter column name: ')

                if column_name == "back" or table_name == "back":
                    print_table()

                else:
                    cur.execute("""ALTER TABLE {} DROP COLUMN {}""".format(table_name, column_name))
                conn.commit()
                conn.close()

            else:
                print("\nPlease enter valid selection.")


        def ask_action():
            while True:
                question = str(input("\nDo you want to delete(row), add(column), drop(column), print(table) or quit?\n"
                                     "rm row/mk row/rm cl/mk cl/print/exit: "))

                if question == "rm row":
                    delete_row()
                    print_table()
                    break

                elif question == "mk row":
                    add_row()
                    print_table()
                    break

                elif question == "rm cl":
                    alter_drop_column()
                    print_table()
                    break

                elif question == "mk cl":
                    alter_add_column()
                    print_table()
                    break


                elif question == "print":
                    print_table()
                    break

                elif question == "exit":
                    quit()
                    break

                else:
                    print("\nPlease enter valid selection.")
                    continue


        print_table()
        break

    else:
        print("\nPlease enter valid user/password.\n")
        continue
