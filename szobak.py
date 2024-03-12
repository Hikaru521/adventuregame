from enemyk import zombie
import random

class Room:
    def __init__(self, y, x, message, enemy, is_unlocked = False):
        self.y = y
        self.x = x
        self.message = message
        self.is_unlocked = is_unlocked
        self.enemy = enemy

    def is_this(self, y, x):
        return self.x == x and self.y == y

rooms = {"szoba3_2": Room(3, 2, "\n-------------------------------------STORY--------------------------------------\n2043-at irunk, pár éve a földön egy furcsa virus ütötte fel a fejét\n"
              "amelyben a holtak új éltre keltek és az élőkre támadtak.\n"
              "A nagyhatalmak tehetetlenségükben bevetették az atomrakétákat\nezért a föld nagy része lakhatatlanná vált, a túlélők száma nagyon kevés.\n"
              "Ezek egyike vagy te is! Eredeti szakmádat nézve biológus vagy,\naz atom csapásokat egy földalatti bunkerben vészelted át ahol éppen dolgoztál.\n"
              "Egy nap hatalmas robbanás rázza meg az egész labort, lassan magadhoz térsz,\nhalvány villogó fények, nagy füst és furcsa halk robbanás zajai hallatszódnak.\n"
              "Tovább tudsz haladni előre amerre egy folyosót látsz vagy\njobbra amerre hallodtál valami furcsa és rémisztő hangot. A döntés a tiéd!\n"
              "--------------------------------------------------------------------------------\n", None ,  True),
         "szoba3_4": Room(3, 4, "\n--------------------------------------------------------------STORY----------------------------------------------------------------\n"
                                "A furcsa hang egy romos helyiségbe vezetett téged ahova szépen óvatosan belépve látod hogy a romok túloldalán katonák beszélgetnek.\n"
                                "Nem tűnnek neked emberinek, a beszélgetést hallva egyre biztosabb vagy abban hogy nem emberekkel van dolgod.\n"
                                "A beszédükön hallatszódik hogy nem emberi nyelven kommunikálnak. Észre vesznek téged és harcba keveredsz velük!\n"
                                "-----------------------------------------------------------------------------------------------------------------------------------\n",
                          zombie("soldier", 50, random.randrange(25, 30))),
         "szoba3_6": Room(3, 6, "\n-----------------------------------------------------STORY------------------------------------------------------\n"
                                "Beléptél egy étkezőnek tűnő alig felismerhető helyiségbe!\n"
                                "Próbálsz fedezéket találni vagy valami támpontot amitől kezdve nyugodtan elindulhatsz felfedezni a szobát.\n"
                                "Az étkező konyha részét átkutatva egy kis élelemhez jutsz így gyorsan energia vissza nyerésének érdekében eszel.\n"
                                "Étkezés után kicsit körülnézel.\n"
                                "Az asztalok között találsz egy vérfoltot amiből arra tudsz következtetni hogy valamilyen állat van a közeledben.\n"
                                "Tudod hogy nem egy szobában van veled de következtetni tudsz rá hogy valahol körülötted lévő szobákban lehet.\n"
                                "Haladsz tovább keresve az állat nyomait hátha biztonságot nyújtó társad lehet belőle és nem ellenség.\n"
                                "----------------------------------------------------------------------------------------------------------------\n",None ),
         "szoba2_2":Room(2,2, "\n-------------------------------------STORY--------------------------------------"
                              "\nBeléptél a hosszú, egyenes és sötét folyosóra.\nEgy gyenge éppen merülőben lévő lámpával próbálsz átjutni a törmelékes folyosón.\n"
                              "A másik végén fényt látsz és úgy gondolod a nap fényét látod!\n"
                              "--------------------------------------------------------------------------------",None ),
         "szoba2_4": Room(2, 4, "\n-----------------------------------------------STORY-----------------------------------------------"
                                "\nBeléptél egy koszos, poros, romos raktárba aminek lyukacsos falain átlátva látod túloldalt a fényt.\n"
                                "Mielőtt a fény után mennél kicsit körbe nézel a raktárban. Nagyon sok nyitott dobozt látsz.\n"
                                "Kutakodsz a dobozok között tárgyak után,\nde sajnos egy pár törött üvegen és az omladozó fal darabjain kívül nem találsz mást!\n"
                                "Elindulsz tovább jobb szerencsében reménykedve!\n"
                                "---------------------------------------------------------------------------------------------------\n",None ),
         "szoba2_6": Room(2, 6, "\n----------------------------------------------STORY-----------------------------------------------\n"
                                "A szoba elejéből ami egy irodának tűnik, látod hogy éppen menne ki valaki és az állata a szobából.\n"
                                "Megpróbálsz utánuk osonkodni, de nem megy mivel a romok ropognak ahogy a súlyodat rájuk helyezed,\nígy a titokzatos ember állata meghall téged."
                                " A mostmár tisztán látható sötét zöld szőrű,\npiros szemű, habzó szájú élőlény egy kutya és már feléd is fut."
                                "Harcba keveredsz az élőlénnyel!\n"
                                "--------------------------------------------------------------------------------------------------\n",
                          zombie("kutya", 75, random.randrange(20, 34))),
         "szoba1_2":Room(1,2, "\n------------------------------------------------STORY-----------------------------------------------\n"
                              "A következő szobába érve furcsa morgás szerű hangokra leszel figyelmes.\n"
                              "Körbe nézel, egy garázsban vagy aminek ajtaja láthatóan el van fedve valami szilárd anyaggal.\n"
                              "A morgó hangot hallván gyorsan bemenekülsz a garázsban álló lepukkant autó alá.\n"
                              "Elég gyorsan kiderül hogy milyen állat morog mivel meglátod a lábát így rájössz ez bizony egy medve.\n"
                              "A medve kiszagolt téged, nagyon rossz helyzetben vagy. Megpróbálsz gyorsan kibújni a kocsi alól,\n"
                              "de nem sikerül jól és a medve a fellök. Harcba keveredsz a medvével!\n"
                              "----------------------------------------------------------------------------------------------------\n",
                         zombie("medve", 100, random.randrange(30, 33))),
         "szoba1_4":Room(1, 4, "\n------------------------------------------------STORY-----------------------------------------------\n"
                               "Egy kisebb folyosó végére érve egy orvosi szobát találsz.\n"
                               "Ellátod sebeidet a szobában talált elsősegély ládában talált dolgokkal.\n"
                               "Elláttad sebeidet viszont véres lettél így figyelned kell hogy nehogy kiszagoljon valamilyen állat.\n"
                               "A szobába lépve nem tudod képzelted e de láttál egy ember elmenni a tőled jobbra lévő udvarra.\n"
                               "Ha képzelted ha nem utána mész mivel kíváncsi vagy magadat csapod be vagy tényleg jól láttad.\n"
                               "Rossz megérzésekkel kezdessz el menni a titokzatos ember utána!\n"
                               "----------------------------------------------------------------------------------------------------\n",None ),
         "szoba1_6":Room(1, 6, "\n----------------------------------------------------STORY----------------------------------------------------\n"
                               "A titokzatos alak után sietve látod ahogyan éppen az udvar közepén áll és rád néz!\n"
                               "El fog egy nagyon nagyon rossz érzés de mégis megszólítod. Az alak egy szót se válaszol,\n"
                               "mindössze csak felnevet és azonnal rád támad. Támadása előtt látod hogy nem emberi\n"
                               "de nem is zombinak néz ki, valahol a kettő között lehet. Lehet magát alakította át félig ember félig zombivá?\n"
                               "A harc megkezdődik, a kémikus rád támad!\n"
                               "-------------------------------------------------------------------------------------------------------------\n",
                         zombie("kemikus_boss", 200, random.randrange(20, 35)))}

print()