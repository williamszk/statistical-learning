
# https://www.youtube.com/watch?v=ZmUjf3gL1VU&ab_channel=Dagster
# https://dagster.io/blog/dagster-crash-course-oct-2022


cd youtube-dagster/230310_01
dagster project scaffold --name my-dagster-project
cd my-dagster-project
pip install -e '.[dev]'

# Unable to find any timezone configuration
timedatectl
ls -l /etc/localtime
ls /usr/share/zoneinfo/

apt update
apt upgrade -y
apt install systemd -y

# https://stackoverflow.com/a/51317300/8782077

apt install tzdata -y

# Configuring tzdata
# ------------------

# Please select the geographic area in which you live. Subsequent configuration questions will narrow this down by presenting a list
# of cities, representing the time zones in which they are located.

#   1. Africa   3. Antarctica  5. Arctic  7. Atlantic  9. Indian    11. US
#   2. America  4. Australia   6. Asia    8. Europe    10. Pacific  12. Etc
# Geographic area: 2

# Please select the city or region corresponding to your time zone.

#   1. Adak                     33. Cancun         65. Guyana                97. Metlakatla               129. Resolute
#   2. Anchorage                34. Caracas        66. Halifax               98. Mexico_City              130. Rio_Branco
#   3. Anguilla                 35. Cayenne        67. Havana                99. Miquelon                 131. Santa_Isabel
#   4. Antigua                  36. Cayman         68. Hermosillo            100. Moncton                 132. Santarem
#   5. Araguaina                37. Chicago        69. Indiana/Indianapolis  101. Monterrey               133. Santiago
#   6. Argentina/Buenos_Aires   38. Chihuahua      70. Indiana/Knox          102. Montevideo              134. Santo_Domingo
#   7. Argentina/Catamarca      39. Ciudad_Juarez  71. Indiana/Marengo       103. Montreal                135. Sao_Paulo
#   8. Argentina/Cordoba        40. Coral_Harbour  72. Indiana/Petersburg    104. Montserrat              136. Scoresbysund
#   9. Argentina/Jujuy          41. Costa_Rica     73. Indiana/Tell_City     105. Nassau                  137. Shiprock
#   10. Argentina/La_Rioja      42. Creston        74. Indiana/Vevay         106. New_York                138. Sitka
#   11. Argentina/Mendoza       43. Cuiaba         75. Indiana/Vincennes     107. Nipigon                 139. St_Barthelemy
#   12. Argentina/Rio_Gallegos  44. Curacao        76. Indiana/Winamac       108. Nome                    140. St_Johns
#   13. Argentina/Salta         45. Danmarkshavn   77. Inuvik                109. Noronha                 141. St_Kitts
#   14. Argentina/San_Juan      46. Dawson         78. Iqaluit               110. North_Dakota/Beulah     142. St_Lucia
#   15. Argentina/San_Luis      47. Dawson_Creek   79. Jamaica               111. North_Dakota/Center     143. St_Thomas
#   16. Argentina/Tucuman       48. Denver         80. Juneau                112. North_Dakota/New_Salem  144. St_Vincent
#   17. Argentina/Ushuaia       49. Detroit        81. Kentucky/Louisville   113. Nuuk                    145. Swift_Current
#   18. Aruba                   50. Dominica       82. Kentucky/Monticello   114. Ojinaga                 146. Tegucigalpa
#   19. Asuncion                51. Edmonton       83. Kralendijk            115. Panama                  147. Thule
#   20. Atikokan                52. Eirunepe       84. La_Paz                116. Pangnirtung             148. Thunder_Bay
#   21. Atka                    53. El_Salvador    85. Lima                  117. Paramaribo              149. Tijuana
#   22. Bahia                   54. Ensenada       86. Los_Angeles           118. Phoenix                 150. Toronto
#   23. Bahia_Banderas          55. Fort_Nelson    87. Lower_Princes         119. Port-au-Prince          151. Tortola
#   24. Barbados                56. Fortaleza      88. Maceio                120. Port_of_Spain           152. Vancouver
#   25. Belem                   57. Glace_Bay      89. Managua               121. Porto_Acre              153. Virgin
#   26. Belize                  58. Godthab        90. Manaus                122. Porto_Velho             154. Whitehorse
#   27. Blanc-Sablon            59. Goose_Bay      91. Marigot               123. Puerto_Rico             155. Winnipeg
#   28. Boa_Vista               60. Grand_Turk     92. Martinique            124. Punta_Arenas            156. Yakutat
#   29. Bogota                  61. Grenada        93. Matamoros             125. Rainy_River             157. Yellowknife
#   30. Boise                   62. Guadeloupe     94. Mazatlan              126. Rankin_Inlet
#   31. Cambridge_Bay           63. Guatemala      95. Menominee             127. Recife
#   32. Campo_Grande            64. Guayaquil      96. Merida                128. Regina
# Time zone: 135


# Current default time zone: 'America/Sao_Paulo'
# Local time is now:      Fri Mar 10 10:47:03 -03 2023.
# Universal Time is now:  Fri Mar 10 13:47:03 UTC 2023.
# Run 'dpkg-reconfigure tzdata' if you wish to change it.


# This solved my problem with timezone!

pip install -e '.[dev]'

# Software defined assets - SDA




