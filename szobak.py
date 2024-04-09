from enemyk import zombie
import random
from dialog import Dialog

class Room:
    def __init__(self, y, x, story_t, message, story_a, enemy, is_unlocked = False):
        self.y = y
        self.x = x
        self.story_t = story_t
        self.message = message
        self.story_a = story_a
        self.is_unlocked = is_unlocked
        self.enemy = enemy

    def is_this(self, y, x):
        return self.x == x and self.y == y

#Az összes szobánál a message-nél ki lett törölve a Dialog hogy ne kelljen mindig végig várni. Mindenhova a zárójel elé írd vissza!
rooms = {"szoba3_2": Room(3, 2, "\n-------------------------------------STORY--------------------------------------",(
                                       "2043-at irunk, pár éve a földön egy furcsa virus ütötte fel a fejét",
                                        "amelyben a holtak új éltre keltek és az élőkre támadtak.",
                                        "A nagyhatalmak tehetetlenségükben bevetették az atomrakétákat",
                                        "ezért a föld nagy része lakhatatlanná vált, a túlélők száma nagyon kevés.",
                                        "Ezek egyike vagy te is! Eredeti szakmádat nézve biológus vagy,",
                                        "az atom csapásokat egy földalatti bunkerben vészelted át ahol éppen dolgoztál.",
                                        "Egy nap hatalmas robbanás rázza meg az egész labort, lassan magadhoz térsz,",
                                        "halvány villogó fények, nagy füst és furcsa halk robbanás zajai hallatszódnak.",
                                        "Tovább tudsz haladni előre amerre egy folyosót látsz vagy",
                                        "jobbra amerre hallodtál valami furcsa és rémisztő hangot. A döntés a tiéd!"),
                          "--------------------------------------------------------------------------------",None ,  True),
         "szoba3_4": Room(3, 4, "\n-------------------------------------STORY--------------------------------------" ,(
                                "A furcsa hang egy romos helyiségbe vezetett téged ahova szépen óvatosan belépve látod hogy a romok túloldalán katonák beszélgetnek.",
                                "Nem tűnnek neked emberinek, a beszélgetést hallva egyre biztosabb vagy abban hogy nem emberekkel van dolgod.",
                                "A beszédükön hallatszódik hogy nem emberi nyelven kommunikálnak. Észre vesznek téged és harcba keveredsz velük!",),
"--------------------------------------------------------------------------------",
                          zombie("soldier", 50, random.randrange(25, 30))),
         "szoba3_6": Room(3, 6, "\n-------------------------------------STORY--------------------------------------", (
                                "Beléptél egy étkezőnek tűnő alig felismerhető helyiségbe!",
                                "Próbálsz fedezéket találni vagy valami támpontot amitől kezdve nyugodtan elindulhatsz felfedezni a szobát.",
                                "Az étkező konyha részét átkutatva egy kis élelemhez jutsz így gyorsan energia vissza nyerésének érdekében eszel.",
                                "Étkezés után kicsit körülnézel.",
                                "Az asztalok között találsz egy vérfoltot amiből arra tudsz következtetni hogy valamilyen állat van a közeledben.",
                                "Tudod hogy nem egy szobában van veled de következtetni tudsz rá hogy valahol körülötted lévő szobákban lehet.",
                                "Haladsz tovább keresve az állat nyomait hátha biztonságot nyújtó társad lehet belőle és nem ellenség."),
                          "----------------------------------------------------------------------------------------------------------------",None ),
         "szoba2_2":Room(2,2, "\n-------------------------------------STORY--------------------------------------" ,(
                              "Beléptél a hosszú, egyenes és sötét folyosóra.",
                              "Egy gyenge éppen merülőben lévő lámpával próbálsz átjutni a törmelékes folyosón.",
                              "A másik végén fényt látsz és úgy gondolod a nap fényét látod!",),
                         "--------------------------------------------------------------------------------",None ),
         "szoba2_4": Room(2, 4,"\n-----------------------------------------------STORY-----------------------------------------------", (
                                "Beléptél egy koszos, poros, romos raktárba aminek lyukacsos falain átlátva látod túloldalt a fényt.",
                                "Mielőtt a fény után mennél kicsit körbe nézel a raktárban. Nagyon sok nyitott dobozt látsz.",
                                "Kutakodsz a dobozok között tárgyak után,",
                                "de sajnos egy pár törött üvegen és az omladozó fal darabjain kívül nem találsz mást!",
                                "Elindulsz tovább jobb szerencsében reménykedve!",),
                          "---------------------------------------------------------------------------------------------------",None ),
         "szoba2_6": Room(2, 6,"\n----------------------------------------------STORY-----------------------------------------------", (
                                "A szoba elejéből ami egy irodának tűnik, látod hogy éppen menne ki valaki és az állata a szobából.",
                                "Megpróbálsz utánuk osonkodni, de nem megy mivel a romok ropognak ahogy a súlyodat rájuk helyezed,",
                                "így a titokzatos ember állata meghall téged.",
                                " A mostmár tisztán látható sötét zöld szőrű,",
                                "piros szemű, habzó szájú élőlény egy kutya és már feléd is fut.",
                                "Harcba keveredsz az élőlénnyel!",),"--------------------------------------------------------------------------------------------------",
                          zombie("kutya", 75, random.randrange(20, 34))),
         "szoba1_2":Room(1,2,"\n------------------------------------------------STORY-----------------------------------------------" ,(
                              "A következő szobába érve furcsa morgás szerű hangokra leszel figyelmes.",
                              "Körbe nézel, egy garázsban vagy aminek ajtaja láthatóan el van fedve valami szilárd anyaggal.",
                              "A morgó hangot hallván gyorsan bemenekülsz a garázsban álló lepukkant autó alá.",
                              "Elég gyorsan kiderül hogy milyen állat morog mivel meglátod a lábát így rájössz ez bizony egy medve.",
                              "A medve kiszagolt téged, nagyon rossz helyzetben vagy. Megpróbálsz gyorsan kibújni a kocsi alól,",
                              "de nem sikerül jól és a medve a fellök. Harcba keveredsz a medvével!",),
                         "----------------------------------------------------------------------------------------------------",
                         zombie("medve", 100, random.randrange(30, 33))),
         "szoba1_4":Room(1, 4,"\n------------------------------------------------STORY-----------------------------------------------" ,(
                               "Egy kisebb folyosó végére érve egy orvosi szobát találsz.",
                               "Ellátod sebeidet a szobában talált elsősegély ládában talált dolgokkal.",
                               "Elláttad sebeidet viszont véres lettél így figyelned kell hogy nehogy kiszagoljon valamilyen állat.",
                               "A szobába lépve nem tudod képzelted e de láttál egy ember elmenni a tőled jobbra lévő udvarra.",
                               "Ha képzelted ha nem utána mész mivel kíváncsi vagy magadat csapod be vagy tényleg jól láttad.",
                               "Rossz megérzésekkel kezdessz el menni a titokzatos ember utána!",),
                         "----------------------------------------------------------------------------------------------------",None ),
         "szoba1_6":Room(1, 6, "\n----------------------------------------------------STORY----------------------------------------------------", (
                               "A titokzatos alak után sietve látod ahogyan éppen az udvar közepén áll és rád néz!",
                               "El fog egy nagyon nagyon rossz érzés de mégis megszólítod. Az alak egy szót se válaszol,",
                               "mindössze csak felnevet és azonnal rád támad. Támadása előtt látod hogy nem emberi",
                               "de nem is zombinak néz ki, valahol a kettő között lehet. Lehet magát alakította át félig ember félig zombivá?",
                               "A harc megkezdődik, a kémikus rád támad!",),"-------------------------------------------------------------------------------------------------------------",
                         zombie("Kémikus", 200, random.randrange(20, 35)))}

print()