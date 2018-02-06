def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "1.Get your own details\n"
        print "2.Get details of a user by username\n"
        print "3.Get your own recent post\n"
        print "4.Get the recent post of a user by username\n"
        print "5.Like recent post of a user\n"
        print "6.Delete negative comment for a user\n"
        print "7.Exit"
        choice = raw_input("Enter you choice: ")
        if choice == "1":
            self_info()
        elif choice == "2":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_info(insta_username)
        elif choice == "3":
            get_own_post()
        elif choice == "4":
            insta_username = raw_input("Enter the username of the user: ")
            get_user_post(insta_username)
        elif choice == "5":
            insta_username = raw_input("Enter the username of the user: ")
            like_a_post(insta_username)
        elif choice == "6":
            insta_username = raw_input("Enter the username of the user: ")
            post_a_comment(insta_username)
        elif choice == "7":
            insta_username = raw_input("Enter the username of the user: ")
            delete_negative_comment(insta_username)
        elif choice == "8":
            exit()
        else:
            print "wrong choice"
