test = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

inp = """cmpmbppqmqsqzzrrswrrnqrnqqjzjvzzqvzvjvnnlclrrjhrrrnggmgwwdhhfttmmjrjzrzrhrbrgbrbsbjbcjjvpjjcvjvttfwffjtffqqqldqllhthhljhllfffbfbzbczzznmznnrrtgrgppdcppdfpfjjrggpjgjwgjwgghdggzzshzhrhttmhhdqhqsqgglhljjbggjhggfsfvfggrmggwwbwvvwssqtqzqlqvlqqvtthjhjrjssclscsszhzbztbbdhdbbqfbqqvdqdjjjspsqslsnlljnljjhttdtbdttjpjggtfftlldpdzzqhzqqcwwvggmgmppmhpmpddgjjbzbmzmllndldblbwbswsbbmzzwnnpdndzznmnjnjmnnzwwrqwrqrvqvqmmbmhmzzdqqfnqqgnqqfppmnnqzzvvcfclcrrzfzrzttchttshsphshddrgdggvwgvwwjjzbbprrgwrrcttwbwpwfffqppwnpwpqwwwbmwwjrjprrrsfrfdfrddvdzvzqzgzmgmpgpmmpspdssdlsldsdwssgzgddttqpphllvbvccjzjppffsjsbbvnbvbttgwtgtftzzlhzzjvzvsvtsttfrfrsswpwnwccqtqrqqrhqhjhccpfpgpjgpprnprrscctddqmdqqncqctqqrpqrprwpwnwnrnccmfmdfmfdfnfdnnphhbhttsszgssvhhprprnrsrrvggdllvfvrvbrbsrbrpphhqbbhllpttjmttrstszzwllbsbzzgmzgzbzcbcbjcbbjdjpjtttwggqhhpzpzszqqzhqqhrhlrrrvnrnqrqgrqggzccnnjrrcmmzvmmvtmtltvvlzlmmbnmmbbclljnjhhbjbhbjbbfcbfcfbbqwwftfhttwvwhhwfwcffwvwmmwtwftfjttwdtwdtwttqnttmdtdjtdjjlzjzhjhwwnbbmdmhhjmhmjjwmmpsmmhrrfnnqrqjrrpmpjpzpbzpztppswsmsnnlnppscsgcgsccsfcctbtcctvcvhvjhhccppbrbcrbrmbmvmllnmllgfgmgdmmslmlrmllhttgrrsttlmmnrrrlqqsjjddzzsbsdbbrjbjvbbfwwwglljplpglltlztzvtzzmbzbmbmcchlchcnhccbhhhzrrglgmgwwwwrddvmmvdvvpjpnpspmpsmpsscrrphpdhdllrsspcspsqslsspbbmcbmmdhdwhwpphfhmmfhmhjmjrrhtrtffsddwsddwccvncczlzjzdjzddszdsstgtbthhjhddwppvhvvvwrvwrrpspjpvjjsmsccszzgpzzmjzmzvmvrmmgbglgppbfppvvqffgdgtgpgdgnghhbhgbbpbdbrrjrtjtggvzzvttwbwlbwbttrbttvdttpctcrtrccddfrrmqqjrqqsvqsqzsslnlggmrggnllvdvbvmbmsmwmfmvvdwvwbbnddvfvzzjppbpgpvgppblbzznsscwssqppgbbfwwfmfzzqqgnnjnffvbfvbbfllbhlltvtnvnbnsnddcjcbjbbjpbbhhjghhqjjlttnmmhwmhwwddlppsjppgtthllsclcvvlfvvvlzvlvcccrhrrvqrvvzrvzrrmqqbtbnnwssvhvtttnsttrnnghgdggmgdmmnbnhbhdbddvppvhvlvttzmttljlflvfvpfpwffqbffjllnvlltslsttrvrdrmddtwdwmmlplhlnlffmzzrssvsgsffzjfjcffrcrppzfzbbtltjljtjftfmmmrjmjqmjqmjqmjqjsqqhzzhdhrrcwwbcltfjdgmhvmqmmsclsdgmdqzcvzznwgtdbzgvlpzvdqrvwpmndtzmdpznnplmbvvmffdpbjztvzpwffvqbwmvbmtwjrdpngrftvgznmtzwzmsrvpgpzjcdwvnqplfgncgcdtjbhcqztgqpdhwlmrjbzhcfhnzqmpzzghzpfzbgwmlqztnbdnntgdcfssgzqndhfwdtrbpzbmqjgjflmcllscjnnnrzzsjhnwptjlbhpcwwhsvqqlvjzghnwvzmwtbjgwfgmpdfcjfswvqzwdbnvlwfbmdcjvgjcdhjfbjccsjqrgdrhrjnhgpvvfjqvfwqpgmgfsbsnlrfnbtpzljmzrjmjlldgbvvwbnpqgsnzzmswtwgshdlwhsttdjlhnnlgbprwltbppttctttftrmbjccvwtljqffrcpwnwjgcwjnhmphfsnbfdnfbvzqqlwbnjjdvplrjbflcrwjtrngwzznzhsmnwzfbpjrdmjlwzvrvrblrscjlrmswjpbrtjjbsgzwjnfwwgmnbbppqfnlmfsbpwbdnjmrcvqdhhvrrvmghlbbpfsqzsnbjvrvthnrhlttsnlbgvsdvsmncdglrgpsqjqthnlrhnzpnnjgvrnmdnrtjbmlppfppnmgjhtbzpztdmclgbqjzsgfjllplpnnmjhgpcfcpcmbnwjsdmfmrqvqvjfsrnqhbrzdvwcsmmjvqpjnzbgrhwcwggvvjzbrswplgvbbqhdlqptzjvzcznspjbpvfmgbcfjbgmztmqtlzmzzzpmcdmmvhvnphpcfwcmwqwwqvmwpwhhnspmhrdmjblzhhlphwldfclsfjbzhjglvllldnmtjtwqtztfcvjdngslhnsmmlwlpzdbrrthtwfpjfvfljddplfgnhcnwwmmpgwwspnsprsvprccwvvljwbqwrzqjmwfrnnjbrfsrglnrwdfnsswqwsbpplgnfnvvvhqwmtgsdwmvnzmbjpbscdtcrmsllljwlntjzpwqvvnznmfddtgrmqbdsczhtvjdwrwvjccrqnjlnqbvqhhvnmqmrmnqllcjzcjgzwctrntjsnhrwmcqzrwzzqgqlmbqczlgtmtwlztclhwcjsgbdlfrppwrpbnpgsjfhprvzjwnpdwsjwmdcbmljclcgcnsqcpzgvrrbnnhjhblgnpcbzbcdmgjmpmpcwwdngmggmfqcjcwrzblsfmrslbblhdlwjqrrgtnvcfsccbdgnjcztrblrwbrvdzcnnshwzzvgcqwpqmjzhzlllbtzmcqpnwwqqlcjtrrzfmdpmpblmwztwqdgbmtfggjwnmffzvszgdmhfvflthzmwqgqvgmldzpbwbdvrjldhbnzsthqsczttbbthzgzmmrcmzmzmjfrhbtmsbqrbnsnzzfpvwlwpszdptljqphrdznhbwbfdfhsrqnmlqdcdgbrbsmgwwbbjsmwhzgmqtmfbndzlmlvmrrvrmqbjqbhhqtvvgbhbmsrtljwmtnhtpwjvlrgqljvgpsfrwgdfbcwlmvfdrrlgwvvzvcftwpjhcplgwvqbzftjfbmmcpvrrsvbnwqdhtlsfcjzlrmwvgvgwpbffsrrpdpssqhqrqdglnwcqznzlqqvjzpsdnpwfqtfjqhqwvlfpwrqqmntcnnbfprlwrfdwstvbpjmjdbcdffmwvqbsdnvcgrtccvcfzpwjscmrtbbjjnmlcztbldfnwbqcpqlshthrcbdrfldcmhtgwrgqhnnglbzgdgglzjbgjtdvgzgrspjtbhpmzvpplgjpjbthmjtwqqzsslnfrtmpznbqvmccqccrtdvrssmdgrptsjglvrmlcwfllptczvpgwbdfbrnpzdzmpfjwdhqlsqlzlzrwcsmhcmjhhfhfvcdrzhsmqbwcfshslsnswpslbjnrzqllwbnddhrngmjqtnvhrjpcpmggvgqbwtwcmbvhnwggdrzfgmhhvpqzbvlghsvgmhngwdsrwlzffbpzqmfzvbhbjvqlcswhctpcqnptrvlwblnvpfbzsjnsdjnhqbzddsnthhcfbcvmqgfmvztlcwjbmdtgvgwqbqgdrvbgbnbcnqwzfzqpsgbvtwlphgvqlzshndcbffzcbllgzrzrnhdvqnvtndhcdslqbbhcdftlmnltmsmgfcgvmpbsljdbthjtqlfbmczznwcvfcsnftsnpzcwfqbfhjpswzfzfswfgtzplppsglsdncblddsmftmfdmmnsjjgg"""