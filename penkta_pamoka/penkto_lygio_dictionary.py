# Try creating 5 lvl structure like one here: link from an empty dictionary:

my_basketbal_list = {
    "Kaunas": {
        "Club_name": "Zalgiris",
        "Personel": {
            "Team_members": 12,
            "Support_personel": {
                "towel_guys": 3,
                "staff": {
                    "Active": 3,
                    "Unactive": 77,
                    "Banned": {
                        "Due_rules_restriction": 3,
                        "Policy_breach": 4,


                    }
                }
            }

        },
    },
    "Vilnius": {
    "Club_name": "Rytas",
    "Personel": {
    "Team_members": 12,
    "Support_personel": 3,
    }
    }
    
}

print(my_basketbal_list["Kaunas"])
print(my_basketbal_list["Kaunas"]["Personel"]["Support_personel"]["staff"]["Banned"])
